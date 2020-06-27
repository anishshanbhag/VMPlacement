import pandas as pd
import csv
import numpy as np
import time
import os
from pusher import push
from vmListPuller import pullVMList

csvfile= open("vm1whole.csv")
csvfile2= open("vm2whole.csv")
csvfile3= open("vm3whole.csv")
csvfile4= open("vm4whole.csv")


readCSV= csv.reader(csvfile,delimiter=',')
readCSV2= csv.reader(csvfile2,delimiter=',')
readCSV3= csv.reader(csvfile3,delimiter=',')
readCSV4= csv.reader(csvfile4,delimiter=',')

c=0
arr=[]
arr2=[]
arr3=[]
arr4=[]



#for row in readCSV and row2 in readCSV2 and row3 in readCSV3 and row4 in readCSV4:
while True:
	row=next(readCSV)
	row2=next(readCSV2)
	row3=next(readCSV3)
	row4=next(readCSV4)
	if c!=10:
		arr.append(row)
		arr2.append(row2)
		arr3.append(row3)
		arr4.append(row4)
		c=c+1
	else:
		vmList=pullVMList()
		print(vmList)
		print("abcdefshgduycfhbscnklkmlwes")
		#df=pd.DataFrame(arr,columns=['date','month','year','day','usage'])
		df=pd.DataFrame(arr,columns=['date','month','year','day','usage1','usage2'])
		print(df)
		#os.system('python pusher.py')
		if '1' in vmList:
		        df.to_csv('AppData_1.csv',index=False) 
		        push('1')
		        
		#df=pd.DataFrame(arr2,columns=['date','month','year','day','usage'])
		df=pd.DataFrame(arr2,columns=['date','month','year','day','usage1','usage2'])
		print(df)
		#os.system('python pusher.py')
		if '2' in vmList:
		        df.to_csv('AppData_2.csv',index=False) 
		        push('2')
		        
		#df=pd.DataFrame(arr3,columns=['date','month','year','day','usage'])
		df=pd.DataFrame(arr3,columns=['date','month','year','day','usage1','usage2'])
		print(df)
		#os.system('python pusher.py')
		if '3' in vmList:
		        df.to_csv('AppData_3.csv',index=False) 
		        push('3')
		        
		#df=pd.DataFrame(arr4,columns=['date','month','year','day','usage'])
		df=pd.DataFrame(arr4,columns=['date','month','year','day','usage1','usage2'])
		print(df)
		#os.system('python pusher.py')
		if '4' in vmList:
		        df.to_csv('AppData_4.csv',index=False) 
		        push('4')
		        
		print("Uploaded file")
		time.sleep(30)
		arr=[]
		arr2=[]
		arr3=[]
		arr4=[]
		c=0
					
