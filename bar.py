import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("cpu_disk_data6.csv")
list_1 = []
list_1.append(df[:10])
list_1.append(df[10:20])
list_1.append(df[20:30])
cpu = 0
mem = 0
for i in list_1:
    cpu+=i['usage1'].max()
    mem+=i['usage2'].max()
 

height = [cpu, mem]
bars = ('A', 'B')
y_pos = np.arange(len(bars))
print(y_pos)
# Create bars
plt.bar(y_pos, height)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()
