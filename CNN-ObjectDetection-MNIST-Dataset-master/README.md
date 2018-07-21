# CNN-ObjectDetection-MNIST-Dataset

This project implements convolutional neural network for classification of MNIST dataset using tesnsorflow. The model is trained and saved. The architecture of the network is as follows:

Input (28,28) -> Conv (5,5,32) -> maxpool (5,5) -> conv (5,5,64) -> maxpool (2,2) -> FC (1024) -> Droput (0.2) -> Softmax (10)

Accuracy: 98.15% Loss: 0.053.

The saved model is then used for detection and classifying multiple digits in same image. 
The file cnn_tensorflow_mnist.ipynb is for training of the model and mnist_object_detection.ipynb is for testing the trained model on multiple digits in same image. The object detection is done using OpenCV library.
