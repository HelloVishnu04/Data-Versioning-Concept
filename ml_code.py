import pandas as pd
import os


# create a sample DataFrame with column names

data = { "Name": ['Alice', 'Bob', 'Charlie'],
         "Age": [25, 30, 35],
         "City": ['New York', 'Los Angeles', 'Chicago'] 
 }
df = pd.DataFrame(data)

# ading a new row to the DataFrame for V2
# new_row_loc = {'Name': 'V2', 'Age': 20, 'City' : 'City1'}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exists at the roo level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)    

# define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")
