# Crafting training sets

To build a machine learning model, it is crucial to first understand your variables and determine which variable you want your model to predict. This variable is called the dependent variable, while the other variables that help predict it are called independent variables. Exploratory data analysis can help identify the relationship between the dependent and independent variables.

For instance, consider a dataset on students with variables such as height, mock exam results, and national exam results. Plotting mock exam results against national exam results shows a roughly linear relationship, indicating that mock exam results can help predict national exam performance. However, height has no strong relationship with academic performance and can be excluded from the model.

To train a machine learning algorithm, we create a training set that includes the dependent variable and all relevant independent variables. The algorithm will try to predict the dependent variable for each row based on the independent variables, then adjust its understanding of the process based on how accurate its predictions are. This process enables the algorithm to learn the patterns in the training set.

We also need a test set to validate the model's accuracy in predicting the dependent variable. The test set is not used for training and is independent of the training set. By comparing the predicted values to the actual values in the test set, we can evaluate the model's performance and make improvements if necessary.
