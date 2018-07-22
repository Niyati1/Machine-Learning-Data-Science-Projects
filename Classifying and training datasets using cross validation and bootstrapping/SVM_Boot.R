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
 
>  # Partition the data for train set and test set. The partition function takes the dataset and the spilt parameter as input. 
>  partition <- function(dataframeip.df,a)
+  {
+  if(a<0 | a>1) {
+  stop("Value of a should be between 0 and 1")
+  }
+  no_of_rows <- nrow(dataframeip.df);
+  random_no <- no_of_rows * a;
+  test_rows <- sample(nrow(dataframeip.df),random_no);
+  df1 <- dataframeip.df[test_rows,];
+  df2 <- dataframeip.df[-test_rows,];
+  return (list(df1,df2));
+  }  
> 
> #best_svm function is used for creating and training the svm model on train set and then evaluate the performance of the trained model on test set.
> #best_svm function takes the dataset, split parameter, degree vector and cost vector as an input. Degree and cost vectors can include multiple values and the best_svm model will use all different combinations of degree and cost function to return the best accuracy 
> best_svm <- function(dataframeip.df,alpha,d,c)
+ {
+ acc1 <- 0;
+ test_rows <- partition(dataframeip.df,alpha);
+ df1 <- test_rows[[1]];
+ df2 <- test_rows[[2]];
+ k <- 1
+ 
+ 
+ library(e1071);
+ for(i in d) {
+ for(j in c) {
+ model <- svm( Class~.,data = df1, kernel="polynomial", degree=i,type="C-classification",cost=j); 
+ x <- sum(df2$Class == predict(model,df2))
+ y <- nrow(df2)
+ acc <- (x*100)/y
+ if(acc > acc1) {
+ acc1 <- acc;
+ d1 <- i;
+ c1 <- j;
+ }
+ }
+ }
+ 
+ list_best <- list("Degree"=d1,"Cost"=c1,"Accuracy"=acc1);
+ return(list_best)
+ 
+ } 
> 
> # Execute function best_svm for car dataset 

> cardataset <-read.csv("car.csv", header = FALSE)
> a = 0.8
> degree <- c(1, 2, 3, 4)
> cost <- c(0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0)
> n = 10
> for (i in (1:10)){
+  best_fit <- best_svm(cardataset, a, degree, cost)
+  }  
> 
> #output. The best accuracy of 100% is achieved for degree 3 cost 1000
>  Degree  Cost  Accuracy
>  2       10000 99.42197
>  2       100   98.84393
>  3       1000  100
>  3       1000  99.42197
>  3       1000  99.71098
>  2       1000  99.71098
>  3       1000  100
>  2       1000  99.71098
>  3       1000  100
>  2       1000  99.42197
> 
> # Test the function for other value
> 
>  best_svm(d,0.8,2,100000)
> # $Degree
> # [1] 2
> # $Cost
> # [1] 100000
> # $Accuracy
> # [1] 100
> 
> 
> #best.svm.cross fucntion is used for training the model using cross validation technique.
> #best.svm.cross function takes dataset, degree, cost, and number of folds (n) as an input 
> best.svm.cross <- function(dataframeip.df,d,c,n)
+ {
+ acc1 <- 0;
+ library(e1071);
+ for(i in d) {
+ for(j in c) {
+ model <- svm( Class~.,data = dataframeip.df, kernel="polynomial", degree=i,type="C-classification",cost=j,cross = n);
+     acc <- model$tot.accuracy;
+ if(acc > acc1){
+ acc1 <- acc;
+ d1 <- i
+ c1 <- j
+ }
+ }
+ }
+ message("Model average accuracy : ",model$tot.accuracy);
+ list_best <- list("Degree"=d1,"Cost"=c1,"Accuracy"=acc1);
+ return(list_best);
+ 
+ }
> 
>
> #testing the best.svm.cross fucntion on breast cancer dataset. The best accuracy of  96.56% is achieved for degree 1 and cost 10
> Breast_cancerdataset <-read.csv("breast-cancer-wisconsin.csv", header = FALSE)
> degree <- c(1, 2, 3, 4)
> cost <- c(0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0)
> n <- 10
> best_fit = best.svm.cross(Breast_cancerdataset,degree,cost,CV_folds)
> best_fit
> # Model average accuracy : 91.9885550786838
> # $Degree
> # [1] 1
> # $Cost
> # [1] 10
> # $Accuracy
> # [1] 96.56652
> 
> # bootstrap function computes and returns the upper bound and lower bound for the confidence interval
> bootstrap <- function(dataframeip.df,model,p,n)
+ {
+ err <- vector(,n)
+ 
+ for(i in 1:n)
+ {
+ dnew <- dataframeip.df[sample(nrow(dataframeip.df),replace=T),]
+ predict <- fitted(model)
+ cm <- table(dnew$Class,predict(model,dnew))
+ err[i] <- (cm[1,1] + cm[2,2])/length(predict) * 100
+ 
+ }
+ err <- sort(err)/100
+ p <- p *100;
+ start <- n-p;
+ lb <- err[start];
+ ub <- err[p-1];
+ print(lb)
+ print(ub)
+ }
> 
> # boostrap function is tested on breast cancer dataset
> p <- 0.90
> n <- 100
> new_model <- svm(Diagnosis~., data = Breast_cancerdataset	, kernel="polynomial", degree = 1 ,type = "C-classification",cost=10, cross = 10)
> bootstrap(df,new_model,p,n)
> #Below are the upper bound and lower bound for the accuracy confidence intervals
> # LB : 0.9670959
> # UB : 0.9799714
> 
