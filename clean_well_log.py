# By: Nahil Nigar
# used AI a bit to help understand the lasio/pandas functions, get a sample las file to
# test with, and help work through the cleaning logic. wrote and ran everything myself after.

import lasio
import pandas as pd
import matplotlib.pyplot as plt

log = lasio.read('sample_well.las')
data = log.df()
data = data.reset_index()

print(data.head())
print(data.info())
print(data.describe())
print(data.isna().sum())

# las files use -999.25 as their "no data" number, swapping it out
data = data.replace(-999.25, pd.NA)

# GR shouldnt really go past ~300, saw a value of 9999 in describe() earlier so filtering that junk out
data = data[(data['GR']>0) & (data['GR']<300)]

data = data.ffill()
data=data.dropna()

print('rows left:', len(data))

plt.figure(figsize=(6,8))
plt.plot(data['GR'], data['DEPT'], color='green')
plt.gca().invert_yaxis()
plt.xlabel('Gamma Ray (API)')
plt.ylabel('Depth (ft)')
plt.title('Gamma Ray vs Depth')
plt.grid(True)
plt.savefig('gr_vs_depth.png')
plt.show()

print('saved plot')
