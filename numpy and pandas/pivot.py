import pandas as pd
df = pd.read_csv(r'C:\Users\SauroN\Data Analytics Mind risers\sample2.csv')
print(df.head())
print(df.info())
# print(pd.pivot_table(df,index="Roll No."))