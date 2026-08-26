# By: Nahil Nigar
# ai helped generate the sample production csv and explained how curve_fit works under
# the hood, i put the actual script together and tested it myself.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('sample_production.csv')
print(data.head())
print(data.describe())

t = data['month'].values
q = data['rate_bbl'].values

def arps(t, qi, di, b):
    return qi*(1+b*di*t)**(-1/b)

guess=[800,0.1,0.5]  # rough starting point, doesnt need to be exact

params,_ = curve_fit(arps, t, q, p0=guess, maxfev=5000)
qi,di,b = params

print('qi:',qi)
print('di:',di)
print('b:',b)

fit = arps(t,qi,di,b)

plt.figure(figsize=(7,5))
plt.scatter(t,q,label='observed',color='orange')
plt.plot(t,fit,label='fitted curve',color='blue')
plt.xlabel('Month')
plt.ylabel('Rate (bbl/month)')
plt.title('Decline Curve Fit')
plt.legend()
plt.grid(True)
plt.savefig('decline_curve_fit.png')
plt.show()

# stretching it out 10 yrs to get a rough EUR number
future_t = np.arange(0,120)
future_q = arps(future_t,qi,di,b)
eur=future_q.sum()
print('EUR (10yr):', round(eur),'bbl')

plt.figure(figsize=(7,5))
plt.plot(future_t,future_q,color='green')
plt.xlabel('Month')
plt.ylabel('Rate (bbl/month)')
plt.title('10 Year Production Forecast')
plt.grid(True)
plt.savefig('decline_curve_forecast.png')
plt.show()

print('done')
