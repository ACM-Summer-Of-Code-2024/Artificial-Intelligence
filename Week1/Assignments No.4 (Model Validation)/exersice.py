import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())


#----------exersice 1----------
# Import the train_test_split function
from sklearn.model_selection import train_test_split

# use function
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)


#----------exersice 2----------
# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X,train_y)


#----------exersice 3----------
# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)
# print the top few validation predictions
print(val_predictions[:5])
# print the top few actual prices from validation data
print(val_y[:5])


#----------exersice 4----------
from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_predictions, val_y)

# uncomment following line to see the validation_mae
print(val_mae)
