import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
roll_no = list(range(1,51))
marks = [random.randint(1, 100) for _ in range(50)]

sample_df = pd.DataFrame({"Rollno": roll_no , "Marks":marks})
print(sample_df.head())

print(sns.lineplot(x = "Rollno" , y = "Marks" , data=sample_df))
print(plt.title("Student Marks"))
