#----------exersice 1 ----------
import pandas as pd

#load and read our dataset
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)


#----------exersice 2 ----------
#describe our dataset with Pandas DataFrame feature
kaka = pd.DataFrame.describe(home_data)
print(kaka)

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 14
