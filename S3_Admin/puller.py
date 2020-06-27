import boto3
import botocore
import time
import os
import csv
from poller import train
from placementAlgo import getBestFit
from placementAlgo import push

BUCKET_NAME = 'myvmdata' # replace with your bucket name

s3 = boto3.resource('s3')

def pull(i):
        print("In puller")
        try:
                s3.Bucket(BUCKET_NAME).download_file('vm'+str(i)+'.csv', 'appData'+str(i)+'.csv')
                print("Downloaded file  "+str(i))
        except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                        print("The object does not exist.vm file "+str(i))
                        time.sleep(10)
                        pull(i)


def writeToFile(arr):
        with open("PredictionFile.csv","w") as my_csv:
                csvWriter = csv.writer(my_csv,delimiter=',')
                csvWriter.writerows(arr)

def writePlacement(arr):
        with open("vmServer_map.csv","w") as my_csv:
                csvWriter = csv.writer(my_csv,delimiter=',')
                csvWriter.writerows(arr)

def delete_prev_data():
        for i in range(1,5):
                os.remove("appData"+str(i)+".csv")                        

while True:
        arr=[]
        
        for i in range(1,5):
                pull(i)
                #os.system('python poller.py')
                a=train(i)
                arr.append([i,int(a[0]),int(a[1])])
                obj = s3.Object("myvmdata", "vm"+str(i)+".csv")
                obj.delete()
                print("Deleted file "+str(i))
        print(arr)
        writeToFile(arr)
        print("Prediction File generated")
        res=getBestFit()
        temp=[]
        for k in res:
                i=k[0]
                for tempDict in k[1]:
                        temp.append([int(tempDict["vm_id"]),int(i)])
        writePlacement(temp)
        print("Created VMMap file")
        push()
        print("Uploaded VMMap file")
        # delete_prev_data()
        time.sleep(30)
        
