# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('files/csv_simple_write.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['phone_number'])

# Print out country column as Pandas DataFrame
print(cars[['phone_number']])

# Print out DataFrame with country and drives_right columns
print(cars[['phone_number', 'country']])