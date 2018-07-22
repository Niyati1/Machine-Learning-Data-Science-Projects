# Classification of Mammographic mass dataset using SVM

This project includes build 4 different svm models and performance of each model is compared.
There are few missing values in the dataset, which are changed as follows:

Dataset 1 <- discards the rows with Null values
Dataset 2 <- replace the Null values with -1

Model 1:
 - Dataset 1 is used
 - SVM model is build with kernel="linear" and degree="1"
 - accuracy achieved: 82.77%
 
Model 2:
 - Dataset 1 is used
 - SVM model is build with kernel="polynomial" and degree="2"
 - accuracy achieved: 65.66%
 
Model 3:
 - Dataset 2 is used
 - SVM model is build with kernel="linear" and degree="1"
 - accuracy acheived: 83.25%
 
Model 4:
 - Dataset 2 is used
 - SVM model is build with kernel="polynomial" and degree="2"
 - accuracy achieved: 75.86%
