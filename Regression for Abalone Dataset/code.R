# Code for Exercise 1 :
	func1 <- function(dataframeip.df)
	{
       d <- list(1,2,3);
	c <- list(100,10,1,0.1);
	n <- 5;
	k <- 1;
	hcv <- 0;
	hd <- 0;
	hc <- 0;
	list <- c("Degree","Cost","Cross Validated Accuracy", "Training Accuracy");
       for(i in 1 : length(d)) {
		for(j in 1 : length(c)) { 
			model <- svm( Rings~., data = dataframeip.df, kernel = "polynomial" , degree = d[i],cost = c[j],type="C-classification",cross = n);
			model1 <- svm( Rings~.,data = dataframeip.df, kernel="polynomial", degree=d[i],type="C-classification",cost=c[j]);
			x <- sum(dataframeip.df$Rings == predict(model1,dataframeip.df));
			y <- nrow(dataframeip.df);
			acc <- (x*100)/y;
			accuracy <- c(d[i],c[j],model$tot.accuracy,acc);
			if(model$tot.accuracy > hcv) {
			hcv <- model$tot.accuracy;
			hd <- d[i];
			hc <- c[j];
		}
			list <- rbind(list,accuracy)
	}}
	newmodel <- svm(Rings~.,data=dataframeip.df,kernel="polynomial",degree=hd,cost=hc,type="C-classification",cross = n);
	m <- predict(newmodel,dataframeip.df);
	n <- sum(dataframeip.df$Rings-as.numeric(m));
	average <- n/nrow(dataframeip.df);
	print(list);
	print("Combination that resulted in Highest CV is : ");
	list_best <- list("Degree"=hd,"Cost"=hc,"Accuracy"=hcv); 
	print(list_best);
	cat("Average distance of the predicted class from true class is : ",average);
	No_Of_Times_Prediction_away_from_true_rings <- (dataframeip.df$Rings-as.numeric(m));
	hist(No_Of_Times_Prediction_away_from_true_rings);
}
	

	
# Code for Exercise 2:
 
	func2 <- function(dataframeip.df) {
	BLP <- function(datatest.df,class) {
		d <- list(1,2,3);
		c <- list(100,10,1,0.1);
		n <- 5;
		hcv <- 0;
		hd <- 0;
		hc <- 0;
		hacc <- 0;
		for(i in 1 : length(d)) {
			for(j in 1 : length(c)) { 
				model <- svm( Rings~., data = datatest.df, kernel = "polynomial" , degree = d[i],cost = c[j],type="C-classification",cross = n);
				model1 <- svm( Rings~.,data = datatest.df, kernel="polynomial", degree=d[i],type="C-classification",cost=c[j]);
				x <- sum(datatest.df$Rings == predict(model1,datatest.df));
				y <- nrow(datatest.df);
				acc <- (x*100)/y;
				if(model$tot.accuracy > hcv) {
					hcv <- model$tot.accuracy;
					hd <- d[i];
					hc <- c[j];
					hacc <- acc;
				}
			}
			}
			accuracy <- c(class,nrow(datatest.df),hd,hc,hcv,hacc);
			listtest <- rbind(list,accuracy);
			return(listtest)
		}
	F_LTE_9_OR_GTE_10 = subset(dataframeip.df, Rings<=9 | Rings>=10);
	F_LTE_7_OR_E_8_9 = subset(dataframeip.df, Rings<=7 | Rings == 8 | Rings ==9);
	F_LTE_5_OR_E_6_7 = subset(dataframeip.df, Rings<=5 | Rings == 6 | Rings == 7);
	F_E_8_OR_E_9 = subset(dataframeip.df, Rings==8 | Rings==9);
	F_E_6_OR_E_7 = subset(dataframeip.df, Rings== 6 | Rings==7);
	F_E_10_11_OR_GTE_12 = subset(dataframeip.df, Rings == 10 | Rings == 11 | Rings >=12);
	F_E_12_13_OR_GTE_14 = subset(dataframeip.df, Rings ==12 | Rings == 13 | Rings>=14);
	F_E_10_OR_E_11 = subset(dataframeip.df, Rings == 10 | Rings == 11);
	F_E_12_OR_E_13 = subset(dataframeip.df, Rings ==12 | Rings ==13);
		list2 <- c("Description","Size","Degree of BLP", "Cost of BLP","Average CV accuracy of BLP","Training Accuracy with BLP");
		list1 <- BLP(F_LTE_9_OR_GTE_10,"Less than 9 VS Greater than 10");
		list <- rbind(list1);
		list1 <- BLP(F_LTE_7_OR_E_8_9,"Less than or equal to 7 VS 8 or 9" );
		list <- rbind(list1);
		list1 <- BLP(F_LTE_5_OR_E_6_7 ,"Less than or equal to 5 VS 6 or 7" );
		list <- rbind(list1);
		list1 <- BLP(F_E_8_OR_E_9 ,"Equal to 8 VS 9" );
		list <- rbind(list1);
		list1 <- BLP(F_E_6_OR_E_7 ,"Equal to 6 VS 7" );
		list <- rbind(list1);
		list1 <- BLP(F_E_10_11_OR_GTE_12 ,"Equal to 10 or 11 VS Greater than equal to 12" );
		list <- rbind(list1);
		list1 <- BLP(F_E_12_13_OR_GTE_14  ,"Equal to 12 or 13 VS Greater than equal to 14" );
		list <- rbind(list1);
		list1 <- BLP(F_E_10_OR_E_11  ,"Equal to 10 VS 11" );
		list <- rbind(list1);
		list1 <- BLP(F_E_12_OR_E_13  ,"Equal to 12 VS 13" );
		list <- rbind(list1);
			print(list);
		}

# Code For Exercise 3

func3 <- function(dataframeip.df) {
	BLP <- function(datatest.df,class) {
		d <- list(1,2,3);
		c <- list(100,10,1,0.1);
		n <- 5;
		hcv <- 0;
		hd <- 0;
		hc <- 0;
		hacc <- 0;
		for(i in 1 : length(d)) {
			for(j in 1 : length(c)) { 
				model <- svm( Rings~., data = datatest.df, kernel = "polynomial" , degree = d[i],cost = c[j],type="C-classification",cross = n);
				model1 <- svm( Rings~.,data = datatest.df, kernel="polynomial", degree=d[i],type="C-classification",cost=c[j]);
				x <- sum(datatest.df$Rings == predict(model1,datatest.df));
				y <- nrow(datatest.df);
				acc <- (x*100)/y;
				if(model$tot.accuracy > hcv) {
					hcv <- model$tot.accuracy;
					hd <- d[i];
					hc <- c[j];
					hacc <- acc;
				}
			}
			}
			accuracy <- c(class,nrow(datatest.df),hd,hc,hcv,hacc);
			listtest <- rbind(list,accuracy);
			return(listtest);
		}
		predicted_value <- c();
	F_LTE_9_OR_GTE_10 = subset(dataframeip.df, Rings<=9 | Rings>=10);
	F_LTE_7_OR_E_8_9 = subset(dataframeip.df, Rings<=7 | Rings == 8 | Rings ==9);
	F_LTE_5_OR_E_6_7 = subset(dataframeip.df, Rings<=5 | Rings == 6 | Rings == 7);
	F_E_8_OR_E_9 = subset(dataframeip.df, Rings==8 | Rings==9);
	F_E_6_OR_E_7 = subset(dataframeip.df, Rings== 6 | Rings==7);
	F_E_10_11_OR_GTE_12 = subset(dataframeip.df, Rings == 10 | Rings == 11 | Rings >=12);
	F_E_12_13_OR_GTE_14 = subset(dataframeip.df, Rings ==12 | Rings == 13 | Rings>=14);
	F_E_10_OR_E_11 = subset(dataframeip.df, Rings == 10 | Rings == 11);
	F_E_12_OR_E_13 = subset(dataframeip.df, Rings ==12 | Rings ==13);
		list2 <- c("Description","Size","Degree of BLP", "Cost of BLP","Average CV accuracy of BLP","Training Accuracy with BLP");
		
		list1 <- BLP(F_LTE_9_OR_GTE_10,"Less than 9 VS Greater than 10");
		F_LTE_9_OR_GTE_10_model <- svm(Rings~., data = F_LTE_9_OR_GTE_10, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_LTE_7_OR_E_8_9,"Less than or equal to 7 VS 8 or 9" );
		F_LTE_7_OR_E_8_9_model  <- svm(Rings~., data = F_LTE_7_OR_E_8_9, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_LTE_5_OR_E_6_7 ,"Less than or equal to 5 VS 6 or 7" );
		F_LTE_5_OR_E_6_7_model <- svm(Rings~., data = F_LTE_5_OR_E_6_7, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_E_8_OR_E_9 ,"Equal to 8 VS 9" );
		F_E_8_OR_E_9_model <- svm(Rings~., data = F_E_8_OR_E_9, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_E_6_OR_E_7 ,"Equal to 6 VS 7" );
		F_E_6_OR_E_7_model <- svm(Rings~., data = F_E_6_OR_E_7, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_E_10_11_OR_GTE_12 ,"Equal to 10 or 11 VS Greater than equal to 12" );
		F_E_10_11_OR_GTE_12_model <- svm(Rings~., data = F_E_10_11_OR_GTE_12, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		list <- rbind(list1);
		
		list1 <- BLP(F_E_12_13_OR_GTE_14  ,"Equal to 12 or 13 VS Greater than equal to 14" );
		F_E_12_13_OR_GTE_14_model <- svm(Rings~., data = F_E_12_13_OR_GTE_14, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		list1 <- BLP(F_E_10_OR_E_11  ,"Equal to 10 VS 11" );
		F_E_10_OR_E_11_model <- svm(Rings~., data = F_E_10_OR_E_11, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
		
		
		list1 <- BLP(F_E_12_OR_E_13  ,"Equal to 12 VS 13" );
		F_E_12_OR_E_13_model <-  svm(Rings~., data = F_E_12_OR_E_13, kernel = "polynomial" , degree = list1[2,3],cost = list1[2,4],type="C-classification",cross = n);
		list <- rbind(list1);
			#print(list);
			for(k in 1:nrow(dataframeip.df)) {
				pred1 <- c();
				p <- dataframeip.df[k,];
				pred <- predict(F_LTE_9_OR_GTE_10_model,p);
				pred1 <- c(pred1,predict(F_LTE_9_OR_GTE_10_model,p))
				if(pred1 <= 9) {
					pred1 <- c();
					pred <- predict(F_LTE_7_OR_E_8_9_model,p);
					pred1 <- c(pred1,predict(F_LTE_7_OR_E_8_9_model,p))
					if(pred1 <= 7) {
						pred1 <- c();
						pred <- predict(F_LTE_5_OR_E_6_7_model,p);
						pred1 <- c(pred1,predict(F_LTE_5_OR_E_6_7_model,p))
							if(pred1 <=5) {
							predicted_value <- c(predicted_value,5);
							}
							else {
								pred <- predict(F_E_6_OR_E_7_model,p);
								if(pred==6) {
									predicted_value <- c(predicted_value,6);
								} 
								else if(pred==7) {
									predicted_value <- c(predicted_value,7);
								}
							}
				
					}
					else {
						pred <- predict(F_E_8_OR_E_9_model,p);
						if(pred == 8) {
							predicted_value <- c(predicted_value,8);
						}
						else if(pred == 9) {
							predicted_value <- c(predicted_value,9);
						}
					}
				}
				
				else {
					pred1 <- c();
					pred <- predict(F_E_10_11_OR_GTE_12_model,p);
					pred1 <- c(pred1,predict(F_E_10_11_OR_GTE_12_model,p));
					if(pred == 10 | pred == 11) {
						pred <- predict(F_E_10_OR_E_11_model,p)
						if(pred == 10) {
							predicted_value <- c(predicted_value,10);
						}
						else if(pred == 11) {
							predicted_value <- c(predicted_value,11);
						}
					}
					else {
						pred1 <- c();
						pred <- predict(F_E_12_13_OR_GTE_14_model,p);
						pred1 <- c(pred1,predict(F_E_12_13_OR_GTE_14_model,p));
						if(pred == 12 | pred == 13){
							pred <- predict(F_E_12_OR_E_13_model,p);
							if(pred == 12) {
								predicted_value <- c(predicted_value,12);
							}
							else {
								predicted_value <- c(predicted_value,13);
							}
						}
						else {
							predicted_value <- c(predicted_value,14);
						}
					}
				}
			}
			xx <- sum(dataframeip.df$Rings == predicted_value);
			yy <- xx*100/nrow(dataframeip.df);
			cat("Training Accuracy is: ", yy,"\n");
			m <- predict(F_LTE_9_OR_GTE_10_model,dataframeip.df);
			n <- sum(dataframeip.df$Rings-as.numeric(m));
	average <- n/nrow(dataframeip.df);
	cat("Average distance of the predicted class from true class is : ",average);
	No_Of_Times_Prediction_away_from_true_rings <- (dataframeip.df$Rings-as.numeric(m));
	hist(No_Of_Times_Prediction_away_from_true_rings);
	
		}


# Code for Exercise-4:

func4 <- function(dataframeip.df){
	#plot(dataframeip.df);
	#plot(dataframeip.df, type="h");
	c <- list(100,10,1,0.1);
	e <- list(1.5,1,0.1);
	n <- 10;
	hmse <- 100;
	hc <- 0;
	he <- 0;
	list <- c("Degree","Cost","Epsilon","CV MSE", "MSE Over entire data");
	for(i in 1 : length(c)) {
		for(j in 1 : length(e)) { 
			model <- svm( Y~., data = dataframeip.df, kernel = "polynomial" , degree = 2,cost = c[i],epsilon=e[j],type="eps-regression",cross = n);
			model1 <- svm( Y~.,data = dataframeip.df, kernel="polynomial", degree=2,type="eps-regression",cost=c[i],epsilon=e[j]);
			m <- predict(model1,dataframeip.df);
			x <- sum((dataframeip.df$Y - as.numeric(m))*(dataframeip.df$Y - as.numeric(m)));
			y <- nrow(dataframeip.df);
			err <- (x)/y;		
			MSE <- c(2,c[i],e[j],model$tot.MSE,err);
			if(model$tot.MSE < hmse) {
			hmse <- model$tot.MSE;
			he <- e[j];
			hc <- c[i];
					}
						list <- rbind(list,MSE);
					}
	}
	
print(list);
print("Combination that resulted in Least CV MSE is : ");
	list_best <- list("Degree"=2,"Cost"=hc,"Epsilon"=he,"MSE"=hmse); 
	print(list_best);
}

# Code for Exercise 5:
	# Code for graph showing the plotted data points against the curve provided by best svm model.
	plot(datatest);
 model <- svm(Y~.,data = datatest,kernel="polynomial",degree = 2,cost=1,epsilon=0.1,type="eps-regression");
 p <- predict(model,datatest);
 points(datatest$X,p,col="red");
	# Code for plotting the SVM model using 1000 data points equally spaced between 0 and 10.
 space <- seq(from=0.01,to=10,by=0.01);
 newdatatest <- as.data.frame(space);
 colnames(newdatatest) <- c("X");
 p1 <- predict(model,newdatatest);
 points(space,p1,col="red");

# Code For Exercise 6:

	func6 <- function(dataframeip.df)
	{

	d <- list(1,2,3);
	c <- list(100,10,1,0.1);
	e <- list(1.5,1,0.1);
	n <- 5;
	hcv <- 0;
	hd <- 0;
	hc <- 0;
	hmse <- 100;
	hc <- 0;
	he <- 0;
	list <- c("Degree","Cost","Epsilon", "CV MSE");

	for(i in 1 : length(c)) {
		for(j in 1 : length(e)) {
			for(k in 1 : length(d)){
			model <- svm( Rings~., data = dataframeip.df, kernel = "polynomial" , degree = d[k],cost = c[i],epsilon=e[j],type="eps-regression",cross = n);
			
			
			MSE <- c(d[k],c[i],e[j],model$tot.MSE);
			if(model$tot.MSE < hmse){
				hmse <- model$tot.MSE;
				hd <- d[k];
				hc <- c[i];
				he <- e[j];
			}
			
			list <- rbind(list,MSE);
			
			
		}
	}
	}
	newmodel <- svm(Rings~.,data=dataframeip.df,kernel="polynomial",degree=hd,cost=hc,epsilon=he,type="eps-regression",cross = n);
	m <- predict(newmodel,dataframeip.df);
	n1 <- sum(dataframeip.df$Rings-as.numeric(m));
	average <- n1/nrow(dataframeip.df);

	print(list);
	print("Combination that resulted in Least MSE is : ");
	list_best <- list("Degree"=hd,"Cost"=hc,"Epsilon"=he,"MSE"=hmse); 
	print(list_best);
	cat("Average distance of the predicted class from true class is : ",average);
	No_Of_Times_Prediction_away_from_true_rings <- (dataframeip.df$Rings-as.numeric(m));
	hist(No_Of_Times_Prediction_away_from_true_rings);
	}