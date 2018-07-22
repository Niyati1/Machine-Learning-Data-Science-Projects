# Classifying and training datasets using cross validation and bootstrapping

In this project cross validation and bootstrap method is used for the classification of 2 datasets:
1. UCI car dataset
2. Wisconsin Breast Cancer dataset

Following different functions are created:

1. Function 1:  Partition
  - Takes the dataframe and split parameter as an input and partitions the data into train and test set
  
2. Function 2: best_svm
  - This function takes dataframe, split parameter, degree vector and cost vector as an input
  - The function will compute the accuracy of model with all possible combination of degree and cost 
  - returns a list containing the value of best accuracy, degree, and cost 
  - this function was tested on car dataset the best accuracy of 100% was achieved using degree 3 and cost 1000
  
3. Function 3: best_svm_cross
  - This function takes dataframe, number of folds, degree vector, and cost vector as an input
  - This function will compute the accuracy of model with all possible combination of degree and cost using cross validation technique
  - returns a list containing the value of best accuracy, degree, and cost
  - This function was tested on wisconsin breast cancer dataset and the best accuracy of 96.56% was achieved using degree 1 and cost 10
  
4. Function 4: bootstrap
  - This function takes dataframe, trained model, probability and a positive integer as an input
  - This function computes the upper bound and lower bound Confidence Intervals
  - This function was tested on wisconsin breast cancer dataset and the upper bound and lower bound were 96.70% and 97.99% respectively.
 
