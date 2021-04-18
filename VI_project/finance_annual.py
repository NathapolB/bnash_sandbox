import pandas as pd

df = pd.read_csv('C:/Users/BNash/Desktop/BNASH/Investment/Stock Analysis/Database/raw/Radar/ADVANC.BK.csv')
print(df.loc[1:10])
df['date2'] = df['Date'].str.slice(0, 7)
print(df.loc[1:10])
df = df.drop_duplicates(subset=['date2'], keep = 'last')
print(df)