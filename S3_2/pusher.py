import boto3




def push(num):
        s3 = boto3.client('s3')
        s3.upload_file('AppData_'+num+'.csv','myvmdata','vm'+num+'.csv')


