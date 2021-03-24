import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dynamic_programming_performance.txt')

ax = plt.gca()

df.plot(kind='line',x="Size",y="Time",ax=ax,legend=None)

plt.ylabel("Time (s)")
plt.title('Performance of dynamic_programming.py')
plt.show()
