
R version 3.3.2 (2016-10-31) -- "Sincere Pumpkin Patch"
Copyright (C) 2016 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

[Previously saved workspace restored]

> mammogram1.df <- read.csv("mammographic_masses.csv") # Read data from given csv file and load it into a dataframe
> mammogram2.df <- mammogram1.df[complete.cases(mammogram1.df),] # Removes the rows with NULL values if any
> summary(mammogram2.df)
     Birads            Age            Shape           Margin         Density         Severity     
 Min.   : 0.000   Min.   :18.00   Min.   :1.000   Min.   :1.000   Min.   :1.000   Min.   :0.0000  
 1st Qu.: 4.000   1st Qu.:46.00   1st Qu.:2.000   1st Qu.:1.000   1st Qu.:3.000   1st Qu.:0.0000  
 Median : 4.000   Median :57.00   Median :3.000   Median :3.000   Median :3.000   Median :0.0000  
 Mean   : 4.394   Mean   :55.78   Mean   :2.782   Mean   :2.813   Mean   :2.916   Mean   :0.4855  
 3rd Qu.: 5.000   3rd Qu.:66.00   3rd Qu.:4.000   3rd Qu.:4.000   3rd Qu.:3.000   3rd Qu.:1.0000  
 Max.   :55.000   Max.   :96.00   Max.   :4.000   Max.   :5.000   Max.   :4.000   Max.   :1.0000  
> library(e1071) # library used for building the svm model
> model_1 <- svm(Severity~., data= mammogram2.df, kernel = "linear", type="C") # create a linear classifier to classify the data based on Severity attribute/feature
> summary(model_1)

Call:
svm(formula = Severity ~ ., data = mammogram2.df, kernel = "linear", type = "C")


Parameters:
   SVM-Type:  C-classification 
 SVM-Kernel:  linear 
       cost:  1 
      gamma:  0.2 

Number of Support Vectors:  339

 ( 169 170 )


Number of Classes:  2 

Levels: 
 0 1



> accuracy_model_1 <- (sum(mammogram2.df$Severity == fitted(model_1))*100)/nrow(mammogram2.df) # calculate the accuracy of model_1
> accuracy_model_1
[1] 82.77108
> model_2 <- svm(Severity~., data= mammogram2.df, kernel="polynomial", degree=2, type="C-classification") # create new svm model with degree 2
> summary(model_2)

Call:
svm(formula = Severity ~ ., data = mammogram2.df, kernel = "polynomial", degree = 2, type = "C-classification")


Parameters:
   SVM-Type:  C-classification 
 SVM-Kernel:  polynomial 
       cost:  1 
     degree:  2 
      gamma:  0.2 
     coef.0:  0 

Number of Support Vectors:  735

 ( 366 369 )


Number of Classes:  2 

Levels: 
 0 1



> accuracy_model_2 <- (sum(mammogram2.df$Severity == fitted(model_2))*100)/nrow(mammogram2.df) # calculate the accuracy of model_2
> accuracy_model_2
[1] 65.66265
> mammogram3.df <- replace(mammogram1.df, is.na(mammogram1.df),-1) # Instead of deleting the rows with NA values, replace the NA values with -1
> model_3 <- svm(Severity~., data = mammogram3.df, kernel="linear",type="C") # a linear svm model of degree 1 for mammogram 3 datatset
> accuracy_model_3 <- (sum(mammogram3.df$Severity == fitted(model_3))*100)/nrow(mammogram3.df) # calculate the accuracy of model_3
> accuracy_model_3
[1] 83.24662
> model_4 <- svm(Severity~., data = mammogram3.df, kernel="polynomial",degree=2,type="C-classification") # a svm model of degree 2 for mammogram 3 datatset
> summary(model_4)

Call:
svm(formula = Severity ~ ., data = mammogram3.df, kernel = "polynomial", degree = 2, type = "C-classification")


Parameters:
   SVM-Type:  C-classification 
 SVM-Kernel:  polynomial 
       cost:  1 
     degree:  2 
      gamma:  0.2 
     coef.0:  0 

Number of Support Vectors:  852

 ( 427 425 )


Number of Classes:  2 

Levels: 
 0 1



> accuracy_model_4 <- (sum(mammogram3.df$Severity == fitted(model_4))*100)/nrow(mammogram3.df) # calculate the accuracy of model_4
> accuracy_model_4
[1] 75.85848
