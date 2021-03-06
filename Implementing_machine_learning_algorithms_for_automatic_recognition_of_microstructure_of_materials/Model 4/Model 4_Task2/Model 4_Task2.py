from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
from keras.utils.np_utils import to_categorical
from keras import optimizers
from keras import layers
import numpy
import pandas as pd

seed = 7
numpy.random.seed(seed)

X = pd.read_csv('Dataset/Train_Data.csv')
X = numpy.asarray(X)
X = numpy.float32(X)

Y = pd.read_csv('Dataset/Train_Labels.csv')
Y = numpy.asarray(Y)
Y = numpy.int32(Y)

kfold = StratifiedKFold(n_splits=8,shuffle=True, random_state=seed)
k_fold = kfold.split(X, Y)
cvscores = []
Y = to_categorical(Y, num_classes=3)
for train, test in k_fold:
    #create model
    model = Sequential()
    model.add(Dense(200, input_dim=2048, activation='relu'))
    model.add(Dense(3,activation='softmax'))
    #compile model
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    #fit model
    model.fit(X[train], Y[train], epochs=500, batch_size=100, validation_split=0.1, verbose=2)
    #evaluate model
    scores = model.evaluate(X[test], Y[test], verbose=2) 
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
#save the trained model    
model.save('Model4_Task2.h5')
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
