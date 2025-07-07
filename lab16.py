import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import random

'''
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
'''

'''
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
'''

'''
x = random.normal(size=(2, 3))
print(x)
'''

'''
x = random.normal(loc=5, scale=10, size=(3, 3)) # Draw a 3 by 3 array of random samples from a normal distribution with mean 5 and standard deviation 10
print(x)
print(np.std(x))
print(np.mean(x))
'''

'''
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
'''

'''
x = random.binomial(n=10, p=0.5, size=10) # Draw 10 samples from a binomial distribution with 10 trials and 0.5 probability of success for each trial
print(x)
'''

'''
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()
'''

'''
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
'''

'''
sns.distplot(random.normal(loc=50, scale=5, size=10), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=10), hist=False, label='binomial')
plt.show()
'''

'''
x = random.poisson(lam=2, size=10) # Draw 10 samples from a Poisson distribution with expected number of events 2
print(x)
'''

'''
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
'''

'''
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
'''

'''
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()
'''

'''
x = random.uniform(size=(2, 3))# Draw a 2 by 3 array of random samples from a uniform distribution over [0, 1) where 0 is low and 1 is high set by default. hight and low are upper and lower boundary of interval respectively
print(x)
'''

'''
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
'''

'''
x = random.logistic(loc=1, scale=2, size=(2, 3)) x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
'''

'''
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
'''

'''
x = random.exponential(scale=2, size=(2, 3))
print(x)
'''

'''
x = random.chisquare(df=2, size=(2, 3))
print(x)
'''