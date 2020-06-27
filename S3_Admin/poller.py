import os.path
import time
import pandas as pd
import csv
from os import path
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import numpy as np
from keras.models import load_model
from GetDates import getDates

def getActualData(i):
        actual_data = pd.read_csv("testing.csv")
        actualApp = open("actualAppData"+str(i)+".csv", "w")
        read = csv.reader(actualApp, delimiter=',')

def train(i):
        print("In train")
        #test_df = pd.read_csv("testing.csv")
        csvfile= open("appData"+str(i)+".csv")
        readCSV= csv.reader(csvfile,delimiter=',')
        arr=[]
        next(readCSV)
        z=1
        for row in readCSV:
                if z==10:
                        getDates(int(row[0]),int(row[1]),int(row[2]),int(row[3]))
                        print(row)
                arr.append(row)
                z=z+1
        getActualData(i)
        test_df = pd.read_csv("testing.csv")
        dataframe=pd.DataFrame(arr,columns=['date','month','year','day','usage1','usage2'])
        print(dataframe)
        #train_X = dataframe.drop(columns=['usage'])
        #train_X = dataframe.drop(columns=['usage'])

        #train_X = dataframe[['day']]
        #train_y = dataframe[['usage']]
        train_X = dataframe[['date','day']]
        #train_X = train_X.iloc[1:]

        train_y = dataframe[['usage1','usage2']]
        #train_y = train_y.iloc[1:]
        print(train_y)

        model = load_model('Usage_Prediction'+str(i)+'.h5')
        #print(train_X)
        model.fit(train_X, train_y, validation_split=0.2, epochs=30)
        model.save('Usage_Prediction'+str(i)+'.h5')
                        #print(row)
        #print(readCSV)
        os.remove("appData"+str(i)+".csv")
        print(dataframe)

        print("Training Done , Waiting for the next file")
        test_y_predictions = model.predict(test_df)
        print(test_df)
        print(test_y_predictions)
        usage1Max=0
        usage2Max=0
        temp=[]
        for i in range(len(test_y_predictions)):
                temp.append(test_y_predictions[i][0])
        usage1Max=max(temp)
        temp=[]
        for i in range(len(test_y_predictions)):
                temp.append(test_y_predictions[i][1])
        usage2Max=max(temp)


        print(str(usage1Max)+'    '+str(usage2Max))

        predictionResult=[]
        predictionResult.append(usage1Max)
        predictionResult.append(usage2Max)

        return predictionResult
        

