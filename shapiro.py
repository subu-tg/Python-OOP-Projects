#%%
from scipy.stats import shapiro, anderson
import numpy as np

#%%
data = [4.2, 5.1, 5.9, 6.3, 5.7, 5.8, 6.1]
data = list(range(22))
data = np.random.lognormal(mean=0, sigma=1, size=22)
data = np.random.standard_cauchy(size=22)
data = np.random.poisson(lam=3, size=22)
# data = np.random.uniform(low=0, high=1, size=22)
# data = np.random.normal(loc=0, scale=1, size=22)

#%%
stat, p = shapiro(data)
result = anderson(data, dist='norm')

#%%
print(data)
print(f"Shapiro-Wilk Test Statistic: {stat}")
print(f"P-value: {p}")

if p > 0.05:
    print("Data appears to be normally distributed.")
else:
    print("Data does NOT appear to be normally distributed.")
# The Shapiro-Wilk test is a statistical test that checks the null hypothesis that a sample comes from a normally distributed population.
# %%
