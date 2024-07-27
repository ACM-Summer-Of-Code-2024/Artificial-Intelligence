#exersice 1
# Import the train_test_split function
from sklearn.model_selection import train_test_split

# use function
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

#exersice 2
# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X,train_y)

#exersice 3
# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)
# print the top few validation predictions
print(val_predictions[:5])
# print the top few actual prices from validation data
print(val_y[:5])


#exersice 4
from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_predictions, val_y)

# uncomment following line to see the validation_mae
print(val_mae)
