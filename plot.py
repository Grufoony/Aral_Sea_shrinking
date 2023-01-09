import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Define the data
years = [1977,1987,1998,2006,2010,2013,2014,2015,2019,2021]
areas = [1,
0.760251506,
0.540277577,
0.309543081,
0.274938302,
0.198319318,
0.143275427,
0.174682423,
0.13417339,
0.13754441]

years = np.array(years).reshape((-1,1))

# Fit the data
model = LinearRegression()
model.fit(years, areas)
q = model.intercept_
m = model.coef_

# Plot
plt.plot(years, areas, 'bo')
plt.plot(years, [-0.02216*x + 44.7826 for x in years])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Years', fontsize=15)
plt.ylabel('Shrinking ratio', fontsize=15)
plt.legend(['Data','Fit line'], fontsize=12)
plt.savefig('./tex/linear_plot.pgf')
