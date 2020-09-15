# importing pandas module  
import pandas as pd 
  
# reading csv file from url  
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
   
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
  
# creating new column for len 
# passing values through str.len() 
data["Name Length"]= data["Name"].str.len() 
  

# converting to string dtype 
data["Salary"]= data["Salary"].astype(str) 
  
# passing values 
data["Salary Length"]= data["Salary"].str.len() 
  
# converting back to float dtype 
data["Salary"]= data["Salary"].astype(float) 

# display 
print(data)