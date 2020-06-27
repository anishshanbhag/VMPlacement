import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import boto3
import botocore

BUCKET_NAME = 'myvmdata' # replace with your bucket name

s3 = boto3.resource('s3')

s3.Bucket(BUCKET_NAME).download_file('vmServer_map.csv','vmServer_map.csv')

for i in range(1,5):
    s3.Bucket(BUCKET_NAME).download_file('vm' + str(i) + 'whole.csv', 'vm' + str(i) + 'whole.csv')

df1 = pd.read_csv("vm1whole.csv")
df2 = pd.read_csv("vm2whole.csv")
df3 = pd.read_csv("vm3whole.csv")
df4 = pd.read_csv("vm4whole.csv")
df = pd.read_csv("vmServer_map.csv")

list1 = [df1, df2, df3, df4]
list_1 = []
list_2 = []

for i in range(4):
    if df["server"][i] == 1:
        list_1.append(list1[i])
    else:
        list_2.append(list1[i])

cpu1 = 0
mem1 = 0
cpu2 = 0
mem2 = 0
for i in list_1:
    cpu1 += i['Cpu'].max()
    print("CPU1", i['Cpu'].max())
    mem1 += i['Mem'].max()
    print("MEM1", i['Mem'].max())

for i in list_2:
    cpu2 += i['Cpu'].max()
    print("CPU2", i['Cpu'].max())
    mem2 += i['Mem'].max()
    print("MEM2", i['Mem'].max())

height1 = [cpu1, mem1]
height2 = [cpu2, mem2]

bars = ('CPU', 'MEMORY')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height1,width=0.15,color="green")
plt.bar(y_pos+0.15,height2,width=0.15,color="blue")

green_patch = mpatches.Patch(color="green",label="server1")
blue_patch = mpatches.Patch(color="blue",label="server2")

# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.legend(handles=[green_patch,blue_patch])

# Show graphic
plt.show()
