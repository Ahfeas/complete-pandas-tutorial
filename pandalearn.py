import pandas as pd
import numpy as np
# Example Pandas operations (replace with your actual code)
#data = {'col1': [10, 20, 30], 'col2': [40, 50, 60]}
#df = pd.DataFrame(data)

# Print the DataFrame
#print("DataFrame:")
#print(df)

data = {'id': [1, 2, 3,4],
    'Name': ['Alice', 'Bob', 'Charlie','afee'],
    'Age': [25, 30, 28,35],
    'City': ['New York', 'London', 'Tokyo','Berlin']}

df = pd.DataFrame(data)


print("\n -----------------------------------")
print("DataFrame:")
print(df)

print("\n print first row only")
print(df.iloc[0])

print("\n print third column only")
print(df.iloc[:, 2])