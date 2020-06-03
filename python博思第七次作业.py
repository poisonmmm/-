import pandas as pd

content = pd.read_csv("CombinedCyclePowerPlant.csv")
print(content)
df = pd.DataFrame(data=content)
print(df.iloc[:, 1:3])
print(df["PE"])
print(df.iloc[10:21, 1:4])
