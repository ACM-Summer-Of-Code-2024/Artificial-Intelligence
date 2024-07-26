## Summary
### in continuation of [this](https://github.com/ACM-Summer-Of-Code-2024/AI-Group7-NoName/blob/main/Assignments%20No.2%20(Basic%20Data%20Exploration%20)/summary.md)
+ see all columns of our dataset with ==> `dataset_name.columns`
+ drop not-avaible in data set with ==> `dataset_name.dropna(axis=0)`
+ select desire column in dataset with ==> `variable_name = dataset_name.columns_name`
+ Choosing "Features" with ==> `list_of_features = ['columns1', 'columns2', 'columns3', 'columns4', 'columns5']`
+ limit our dataset with choosed featurs with ==> `variable_name = dataset_name[list_of_features]`
+ import decision tree model from sklearn with ==> `from sklearn.tree import DecisionTreeRegressor`
+ make model with ==> `model_name = DecisionTreeRegressor(random_state=1)`
+ fit model with ==> `model_name.fit(dataset_name[list_of_features], dataset_name.columns_name)`
+ prediction with model with ==> `model_name.predict(dataset_name[list_of_features].head())`
