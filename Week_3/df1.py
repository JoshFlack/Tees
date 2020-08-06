import pandas as pd
import math as ma
import random as ran
import matplotlib.pyplot as plt

df = pd.read_csv("weight-height-data.csv")


whrs=[]


for i, row in df.iterrows():
    whrs.append(row["Weight"]/row["Height"])
  #  whrs.append(whr)

df["WHR"] = whrs

#df.to_csv("data_output.csv")
plt.scatter (df["Weight"],df["WHR"])
plt.show()
