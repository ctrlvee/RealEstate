# The Trust would like to start investing in Residential real estate. You are tasked with determining the market price of a house given a set of features. You will analyze and predict housing prices using attributes or features such as square footage, number of bedrooms, number of floors, and so on
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns

#send to output.txt
# orig_stdout = sys.stdout
# f = open('output.txt', 'w')
# sys.stdout = f
# ##

file_path = '/Users/v/Documents/Coursera/Data Analysis/kc_house_data.csv'
df = pd.read_csv(file_path, header=None)
headers = ['id','date','price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
df.columns = headers
# df.drop(columns=['id'])


df.replace("?", np.nan, inplace=True)


bins = np.linspace(min(df["sqft_living"]), max(df["sqft_living"]), 4)

group_names = ['Low', 'Medium', 'High']

df['sqft_living-binned'] = pd.cut(df['sqft_living'], bins, labels=group_names, include_lowest=True )
values = df['sqft_living-binned'].value_counts() 

# fig = plt.figure(figsize = (10, 5))
# plt.bar(group_names, values, width=0.6)
# plt.title('Living Sqft')
# plt.xlabel('Sqft')
# plt.ylabel('Count')

print(df['id'])
# print(df[['bedrooms', 'bathrooms', 'floors', 'grade']].corr())

#
df.describe().to_csv("house_stats.csv")



sns.regplot(x='bedrooms', y='price', data=df, marker='o', color='red', scatter_kws={"s":2})
plt.ylim(0,)
plt.title('Bedrooms vs Price')
print(df[['bedrooms','price']].corr())




#send to output.txt   
# sys.stdout = orig_stdout
# f.close()

# import matplotlib.pyplot as plt
# height = [189, 185, 195, 149, 189, 147, 154, 
#           174, 169, 195, 159, 192, 155, 191, 
#           153, 157, 140, 144, 172, 157, 181, 
#           182, 166, 167]
  
# plt.hist(height, edgecolor="red", bins=5)
# plt.show()