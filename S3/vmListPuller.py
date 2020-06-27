import boto3
import botocore
import csv
import os

BUCKET_NAME = 'myvmdata' # replace with your bucket name
KEY = 'vmServer_map.csv' # replace with your object key

s3 = boto3.resource('s3')

def pullVMList():
        arr=[]
        try:
                s3.Bucket(BUCKET_NAME).download_file(KEY, 'vmServer_map.csv')
                print("File Downloaded in vm ListPuller")
        except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                        print("The vmServer_map does not exist.")
        csvfile= open("vmServer_map.csv")
        readCSV= csv.reader(csvfile,delimiter=',')
        for row in readCSV:
                if row[1]=='1':
                        arr.append(row[0])
                        
        os.remove("vmServer_map.csv")
        return arr




