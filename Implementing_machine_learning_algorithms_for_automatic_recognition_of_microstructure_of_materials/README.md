
# Thesis-Machine-learning-algorithms-for-microstructure-of-materials
Implementing Machine Learning Algorithms to Automate Identification of Material Microstructures

This project implements various machine learning techniques for identifying the type of material from its microstructure (Task 1) and classifying the microstructure into more general category of ferrous/non-ferrous/others (Task 2). Material microstructures from ASM micrographs database and DoITPoMS library was used for training and testing.

All the models build in this project had a different feature extraction technique, to reduce the dimension of input data. These reduced features were then connected to few hidden layers and classified.

The feature extraction technique for different models include:
1. Pre trained ResNet50 architecture
2. Encoded layer from Convolutional Autoencoders
3. Decoded/Output layer from Convolutional Autoencoders
4. PCA

Below is the brief overview of all the models build and trained in this thesis:

Model 1:

1. Feature extraction technique used: PCA
2. Hidden layer representation: reduced_feature_vectors -> conv -> maxpool -> batchnorm -> conv -> maxpool -> batchnorm -> conv -> conv -> FC -> FC -> FC -> Classified.
3. This model was trained with 8-fold cross validation technique with 50 epochs and batch size of 100 and was classified using Softmax classifier.
4. This model gave an accuracy of 58.36% +- 1.31% for Task 1 and 74.36% +- 1.8% for Task 2.

Model 2:

1. Feature extraction technique used: encoded layer from trained convolutional autoencoder.
2. Hidden layer representation of the autoencoder: (encoder) image_pixel_data -> conv -> maxpool -> conv -> maxpool -> conv
3. Model 2 did not have any additional hidden layers of its own.
4. This model was trained and classified with Random Forest Classifier
5. This model gave an accuracy of 50.35% for Task 1 and 60.53% for Task 2.

Model 3:

1. Feature extraction technique used: decoded layer from trained convolutional autoencoder.
2. Hidden layer representation of the autoencoder: (decoder) encoded_output -> convT -> upsample -> convT -> upsample -> convT
3. Model 3 did not have any hidden layers of its own.
4. This model was trained and classified using random forest classifier.
5. This model gave an accuracy of 52.96% for Task 1 and 61.27% for Task 2.

Model 4:

1. Feature extraction technique used: Pre trained ResNet50 model.
2. Hidden layer represnetation: reduced_feature_vectors -> FC -> FC -> classified.
3. This model was trained with 8-fold cross validation technique with 500 epochs and  batch size of 100 and was classified using softmax classifier.
4. This model gave an accuracy of 92.01% +- 0.54% for Task 1 and 94.31% +- 0.59% for task 2.

Using Model 4 for prediction, an Image Search Engine (ISE) was developed as a python application which can perform below 3 functions:

1. Predict the type of an input micrograph along with its prediction score.
2. Search micrographs using keywords
3. Search visually similar micrographs and predict their type.

Histogram of Oriented Gradients (HoG) was used to search for visually similar micrographs and chi-squared error was used to compare the histograms.

Looking at the results of visually similar micrographs, the important point to conclude was that even though the micrographs were visually similar, they were actually of different material type. So, a human who has no prior knowledge about the alloy microstructures would identify them as of same alloy type, but a trained neural network model was able to identify the difference in visually similar microstructures.  

This gihub repository contains the code and saved weight of all trained models (.h5 file) and also the code for ISE and a detailed thesis report. The Image Search Search engine can be executed by running the main.py file. (Pyhton 3.5 required)
