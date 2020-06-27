import csv


def getPrediction():
        results = []
        with open("PredictionFile.csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
            for row in reader: # each row is a list
                results.append(row)
        return results
        
        
def getVMMap():
        results = []
        with open("vmServer_map.csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
            for row in reader: # each row is a list
                results.append(row)
        return results
        
        
#print(getPrediction())

#print(getVMMap())


def getInput():
        prediction=getPrediction()

        VMMap=getVMMap()

        start=1

        result=[]

        while True:
                #print("Finding for Server"+str(start))
                vmList=[]
                for row in VMMap:
                        if row[1]==start:
                                vmList.append(row[0])
                if len(vmList)==0:
                        break
                server=[]
                server.append(start)
                temp=[]
                for k in prediction:
                        if k[0] in vmList:
                                tempDict={}
                                tempDict["vm_id"]=k[0]
                                tempDict["cpu_usage"]=k[1]
                                tempDict["memory_usage"]=k[2]
                                temp.append(tempDict)
                server.append(temp)
                result.append(server)
                start=start+1

        return result                      
                
             


