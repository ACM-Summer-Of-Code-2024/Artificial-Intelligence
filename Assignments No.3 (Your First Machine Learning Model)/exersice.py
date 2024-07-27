# import pandas
import pandas as pd

# save and read dataset
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)


#----------exersice 1 ----------
# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)

#select and save desired column
y = home_data.SalePrice


#----------exersice 2 ----------
# Create the list of features we want
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# select our list of feature in dataset
X = home_data[feature_names]

# Review data
# print description or statistics from X
print(X.describe())

# print the top few lines
print(X.head())


#----------exersice 3 ----------
from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)


#----------exersice 4 ----------
#predict sales price of home using predict()
predictions = iowa_model.predict(X)
print(predictions)

#review resault 
print(home_data.SalePrice)
predictions = iowa_model.predict(X.head())
print(predictions)
