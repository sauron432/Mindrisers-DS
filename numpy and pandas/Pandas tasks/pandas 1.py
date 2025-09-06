import pandas as pd
data = {"Employee Name":["John","Kate","Leo"],
        "Department":["IT","HR","Sales"],
        "Salary":[50000,55000,6000]}
df = pd.DataFrame(data)
print(df)