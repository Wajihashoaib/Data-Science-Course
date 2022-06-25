import pandas as pd
#Reading dataset
csv_file = pd.read_csv('sports_event.csv')

csv_file.info()
#information of dataset 

print(csv_file.head())
#checking from top

print(csv_file.tail())
#checking from last row
#last row containing two null values in 'CID' and in 'EID' column

df =csv_file.dropna()
#dropna() removes the row that contains NULL values.

df.to_csv('Quiz03.csv')
#creating a file and send data of df to it.