import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Ram", "Hari", "Shyam", "Nirmal", "Eva"],
    "Age": [23, 25, 30, 22, 29],
    "City": ["Kathmandu", "Lalitpur", "Bhaktapur", "Pokhara", "Biratnagar"]
}
df = pd.DataFrame(data,index = [1,2,3,4,5])
print("Original DataFrame:")
print(df)
df.iloc[1, 1] = 26
df.iloc[0:3, 1] = [24, 27, 31]
print('After modifying:\n',df)

print('Slicing using loc:\n',df.loc[2:4])