from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
from keras.utils.np_utils import to_categorical
from keras import optimizers
from keras import layers
import numpy
import pandas as pd
import pickle

seed = 7
numpy.random.seed(seed)

X = pd.read_csv('Model10Dataset/Data.csv')
X = numpy.asarray(X)
X = numpy.float32(X)

Y = pd.read_csv('Model10Dataset/Lables.csv')
Y = numpy.asarray(Y)
Y = numpy.int32(Y)


kfold = StratifiedKFold(n_splits=5,shuffle=True, random_state=seed)
k_fold = kfold.split(X, Y)
cvscores = []
Y = to_categorical(Y, num_classes=3)
for train, test in k_fold:
    
    # create model
    model = Sequential()
    model.add(Dense(100, input_dim=2048, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(Dense(50, activation='relu'))
    model.add(layers.Dropout(0.4))
    model.add(Dense(3,activation='softmax'))
    
    # Compile model
    adam = optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=2e-11, decay=0.0, amsgrad=False)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    # Fit the model
    model.fit(X[train], Y[train], epochs=500, batch_size=75, validation_split=0.1, verbose=2)
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=2) 
    #scores = model.cross_val_score(f,X[test],Y[test])
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
model.save('model10.h5')
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))
