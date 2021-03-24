import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('performance.txt', sep=' ')

ax = plt.gca()
plt.ylabel("Time (s)")

df.plot(kind='line',x="Size",y="brute_force",ax=ax)
df.plot(kind='line',x="Size",y="dynamic_programming",ax=ax)

plt.title('Performance: brute_force vs dynamic_programming')
plt.show()
