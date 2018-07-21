# Imports the necessary library
import numpy as np
import tensorflow as tf

def model(features, labels, mode):
    
    input_layer = tf.reshape(features["x"],[-1,28,28,1])
    conv1 = tf.layers.conv2d(inputs=input_layer,filters=32,kernel_size=[5, 5],padding="same",activation=tf.nn.relu)
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)
    conv2 = tf.layers.conv2d(inputs=pool1,filters=64,kernel_size=[5, 5],padding="same",activation=tf.nn.relu)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)
    pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=0.2, training=mode == tf.estimator.ModeKeys.TRAIN)
    logits = tf.layers.dense(inputs=dropout, units=10)
    
    error = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    predict_classes = {
     "classes": tf.argmax(input=logits, axis=1),
     "probabilities": tf.nn.softmax(logits, name="prob")
    }
    
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
        train_op = optimizer.minimize(loss=error,global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=error, train_op=train_op)

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predict_classes)

    
   
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predict_classes["classes"])}
    return tf.estimator.EstimatorSpec(
      mode=mode, loss=error, eval_metric_ops=eval_metric_ops)
    
def main(unused_argv):
    # Load training and eval data
    mnist = tf.keras.datasets.mnist
    (train_data, train_labels),(test_data, test_labels) = mnist.load_data()
    train_data, test_data = train_data / 255.0, test_data / 255.0
    
    #convert data and labels as numoy array and as required data type
    train_data = np.asarray(train_data, dtype = np.float32)
    test_data = np.asarray(test_data, dtype = np.float32)
    train_labels = np.asarray(train_labels, dtype=np.int32)
    test_labels = np.asarray(test_labels, dtype=np.int32)
    
   
    # Create the Estimator
    mnist_classifier = tf.estimator.Estimator(model_fn=model)    

    # Set up  the logging for predictions
    tensors_to_log = {"probabilities": "prob"}
    logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=50)
    # Train the model
    train_input_fn = tf.estimator.inputs.numpy_input_fn(x={"x": train_data},y=train_labels,batch_size=300,num_epochs=50,shuffle=True)
    mnist_classifier.train(input_fn=train_input_fn,steps=5000,hooks=[logging_hook])
    
    # Evaluate the model 
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(x={"x": test_data},y=test_labels,num_epochs=1,shuffle=False)
    eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
    print(eval_results)
   
if __name__ == "__main__":
  tf.app.run()