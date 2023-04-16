# The Trust would like to start investing in Residential real estate. You are tasked with determining the market price of a house given a set of features. You will analyze and predict housing prices using attributes or features such as square footage, number of bedrooms, number of floors, and so on
import pandas as pd
import numpy as np
import sys

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f



file_path = '/Users/v/Documents/Coursera/Data Analysis/kc_house_data.csv'
df = pd.read_csv(file_path, header=None)
headers = ['id','date','price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
df.columns = headers

# print(df.head(5))

# print(df[['price','bedrooms']].describe())

df.replace("?", np.nan, inplace=True)
missing_data = df.isnull()
# print(missing_data.head(5))

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    
sys.stdout = orig_stdout
f.close()
