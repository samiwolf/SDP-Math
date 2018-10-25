#http://barnesanalytics.com/bayesian-regression-with-pymc3-in-python
import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('D:/SDP Math/math/thads2013n.txt',sep=',')  #needs Data Set
df=df[df['BURDEN']>0]
df=df[df['AGE1']>0]

plt.scatter(df['AGE1'],df['BURDEN'])
plt.show()

with pm.Model() as model:
    # Define priors
    sigma = pm.HalfCauchy('sigma', beta=10, testval=1.)
    intercept = pm.Normal('Intercept', 0, sd=20)
    x_coeff = pm.Normal('x', 0, sd=20)

    # Define likelihood
    likelihood = pm.Normal('y', mu=intercept + x_coeff * df['AGE1'],
                        sd=sigma, observed=df['BURDEN'])

    # Inference!
    trace = pm.sample(3000)
pm.traceplot(trace)
plt.show()
print(np.mean([1 if obj<0 else 0 for obj in trace['x']]))