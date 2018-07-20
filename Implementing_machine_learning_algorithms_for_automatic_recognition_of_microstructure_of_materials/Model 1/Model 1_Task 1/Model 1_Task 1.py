from keras.models import Sequential
from keras.layers import Dense, Conv2D,MaxPooling2D,BatchNormalization,Flatten
from sklearn.model_selection import StratifiedKFold
from keras.utils.np_utils import to_categorical
from keras import optimizers
from keras import layers
from keras import  regularizers
import numpy
import pandas as pd
import pickle

seed = 7
numpy.random.seed(seed)

X = pd.read_csv('Dataset/all_red.csv',header=None)
X = numpy.asarray(X)
X = numpy.float32(X)
X = X.reshape(X.shape[0],16,16,3)

Y = pd.read_csv('Dataset/labels_all.csv',header=None)
Y = numpy.asarray(Y)
Y = numpy.int32(Y)
kfold = StratifiedKFold(n_splits=8,shuffle=True, random_state=seed)
k_fold = kfold.split(X, Y)
cvscores = []
Y = to_categorical(Y, num_classes=11)
for train, test in k_fold:
    
    # create model
    model = Sequential()
    model.add(Conv2D(96,(11,11),padding='same', input_shape=(16,16,3),activation='relu'))
    model.add(MaxPooling2D(3,3))
    model.add(BatchNormalization())
    model.add(Conv2D(256,(5,5),padding='same',activation='relu'))
    model.add(MaxPooling2D(3,3))
    model.add(BatchNormalization())
    model.add(Conv2D(384,(3,3),padding='same',activation='relu'))
    model.add(Conv2D(256,(3,3),padding='same',activation='relu'))
    model.add(Flatten())
    model.add(Dense(512,activation='relu'))
    model.add(Dense(128,activation='relu'))
    model.add(Dense(11,activation='softmax'))
    # Compile model
    adam = optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=2e-11, decay=0.0, amsgrad=False)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    # Fit the model
    model.fit(X[train], Y[train], epochs=50, batch_size=100, validation_split=0.1, verbose=2)
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=2) 
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
model.save('model.h5')
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
