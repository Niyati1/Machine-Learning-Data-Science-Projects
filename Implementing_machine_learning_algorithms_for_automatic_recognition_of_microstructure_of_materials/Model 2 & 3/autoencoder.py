from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose

from keras.models import Model
from keras import backend as K
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard


input_img = Input(shape=(128,128,1))

print(input_img.shape)
#create autoencoder model

x = Conv2D(8, (5, 5), activation='relu', padding="same")(input_img)
print(x.shape)
x = MaxPooling2D((2, 2), padding='same')(x)
print(x.shape)
x = Conv2D(16, (5, 5), activation='relu', padding="same")(x)
print(x.shape)
x = MaxPooling2D((2, 2), padding='same')(x)
print(x.shape)
encoded = Conv2D(32, (5, 5),strides= (4,4), activation='relu', padding="same")(x)
print(encoded.shape)

x = Conv2DTranspose(32, (5, 5), strides= (4,4), activation='relu', padding="same")(encoded)
print(x.shape)
x = UpSampling2D((2, 2))(x)
print(x.shape)
x = Conv2DTranspose(16, (5, 5), strides= (1,1), activation='relu', padding="same")(x)
print(x.shape)
x = UpSampling2D((2, 2))(x)
print(x.shape)
decoded = Conv2DTranspose(1, (5, 5), strides= (1,1), activation='relu', padding="same")(x)
print(decoded.shape)



df = pd.read_csv('Dataset/all.csv')
x_train, x_test = train_test_split(df, test_size=0.10)
x_train = np.asarray(x_train)
x_test = np.asarray(x_test)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

x_train = np.reshape(x_train,  (len(x_train),128,128,1)) 
x_test = np.reshape(x_test, (len(x_test), 128,128,1)) 

autoencoder = Model(input_img, decoded)
en = Model(input_img, encoded)
#compile model
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
#fit the model
autoencoder.fit(x_train, x_train,
                epochs=50,
                batch_size=250,
                shuffle=True,
                validation_data=(x_test, x_test))
#save the trained encoder and decoder weights so that they can be used as a feature extractor.
autoencoder.save('model_new.h5')
en.save('model_en.h5')
