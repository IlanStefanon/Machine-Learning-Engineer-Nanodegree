# Machine-Learning-Engineer-Nanodegree
Predicting Boston Housing Prices
Model Evaluation & Validation Project

Project Description

You want to be the best real estate agent out there. In order to compete with other agents in your area, you decide to use machine learning. You are going to use various statistical analysis tools to build the best model to predict the value of a given house. Your task is to find the best price your client can sell their house at. The best guess from a model is one that best generalizes the data.
For this assignment your client has a house with the following feature set: [11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]. To get started, use the example scikit implementation. You will have to modify the code slightly to get the file up and running.
When you are done implementing the code please answer the following questions in a report with the appropriate sections provided.

Questions and Report Structure

1) Statistical Analysis and Data Exploration
```
Number of data points?
Number of features?
Minimum and maximum housing prices?
Mean and median Boston housing prices?
Standard deviation?
```
The dataset has the following characteristics :
Number of data points : 506
Number of features : 13
Minimum and maximum housing prices : 5 to 50 (thousands of dollars)
Mean and median Boston housing prices : 22.5 and 21.2
Standard deviation : 9.2
The number of data points is relatively small. We'll have to take into account this when we'll split the data
into training/testing set. The testing set should not be too small. The standard deviation is not too big if
we compare it to the minimum and maximum housing prices. It means that there is not a lot of dispersions
( not too much outliers). We'll don't have to clean the data.

2) Evaluating Model Performance
```
Which measure of model performance is best to use for predicting Boston housing data? Why do you think this measurement most appropriate? Why might the other measurements not be appropriate here?
Why is it important to split the data into training and testing data? What happens if you do not do this?
Which cross validation technique do you think is most appropriate and why?
What does grid search do and why might you want to use it?
```
Several model performance is possible with regression :
* Mean Absolute Error (MAE). Easiest regression metric to understand. It assigns equal weight to the
data.
* Mean Squared Error (MSE). This metric "`punishes"' larger errors (outliers) and is useful in the real
world.
* Coefficient of determination (R squared). It's a rescaling of MSE.
* Root Mean Squared Error (RMSE). It's close to MSE, with the advantage to represent a real value (thousands dollars).

In our case, we'll use the standard metric RMSE. It makes an excellent general purpose metric.
It's important to split the data into training and testing data to be able to predict future data. Maximizing
training performance only will cause overly complex model that won't generalize to new data. For this
reason, it should use a testing data to estimate the model trains by the train data.
But train/test split will provide a high variance estimate since changing which data to be in train/test bag
can change the performance of the model. So is even better to create several train/test splits under the same
data and average the results together. It's the goal of the cross-validation.
I have used cross_validation.train_test_split( X, y, test_size=0.4, random_state=0). 
I choose the test size to 33 percent of the total size to be sure to don't have too high variance on the test
set. Finally, the model used (decision trees) for regression provided Scikit-learn is a function with several
parameters. To be able to nd the best combination of parameters it's possible to use Grid search. It's
an approach to tune the parameters automatically. It methodically builds and evaluate the model for each
combination of parameters specied in a grid. In this project, only max_depth is tuned:

3) Analyzing Model Performance
```
Look at all learning curve graphs provided. What is the general trend of training and testing error as training size increases?
Look at the learning curves for the decision tree regressor with max depth 1 and 10 (first and last learning curve graphs). When the model is fully trained does it suffer from either high bias/underfitting or high variance/overfitting?
Look at the model complexity graph. How do the training and test error relate to increasing model complexity? Based on this relationship, which model (max depth) best generalizes the dataset and why?
```

4) Model Prediction
```
Model makes predicted housing price with detailed model parameters
Compare prediction to earlier statistics
```

