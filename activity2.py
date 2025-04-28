import pandas as pd
df=pd.read_csv(r"C:\LPU\LPU S4\INT375 PYTHON\Cardiotocographic1.csv")
print(df.info())
print(df.head(20))
print(df.to_string())

print(df.loc[5])
df = df.dropna(subset=['DS'])
print(df)
df=df[df['LB']<150]
print(df)
df['Variance'] = df['Variance'].replace(0, df['Variance'].mode()[0])
print(df)
min_value = df['MSTV'].min()
max_value = df['MSTV'].max()
df.to_csv(r"C:\LPU\LPU S4\INT375 PYTHON\Cardiotocographic1.csv",index=False)
