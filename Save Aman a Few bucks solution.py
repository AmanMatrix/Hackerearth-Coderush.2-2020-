Fare=[]
sectorConnectionsStr=input()
listSecCon=sectorConnectionsStr.split(" ")
i=0
for values in listSecCon:
    listSecCon[i]=int(values)
    i+=1
    if int(values)==listSecCon[0]:
        if listSecCon[0]>=1 and listSecCon[0]<=50000:pass
        else:exit()
    if int(values)==listSecCon[1]:
        if listSecCon[1]>=1 and listSecCon[1]<=500000:pass
        else:exit()
ABFare=[]
i=0
while(i<listSecCon[1]):
    ABFare.append(input())
    i+=1
i=0
for A_B_Fare in ABFare:
    ABFare[i]=A_B_Fare.split(" ")
    i+=1
for newSplit in ABFare:
    i=0
    for vals in newSplit:
        newSplit[i]=int(vals)
        i+=1
cacheList1=[]
i=0
for someVals in ABFare:
    if someVals[0]==1:
        cacheList1.append([someVals[1],someVals[2]])
    else:pass
    i+=1
cacheList2=[]
while(1):
    for secs in cacheList1:
        if secs[0]==listSecCon[0]:
            Fare.append(secs[1])
        elif secs[0]<listSecCon[0]:
            for someVals in ABFare:
                if someVals[0]==secs[0]:
                    if someVals[2]-secs[1]<0:
                        someVals[2]=secs[1]
                    else:pass
                    cacheList2.append([someVals[1],(someVals[2]-secs[1])+secs[1]])  
                else:pass
        else:exit()
    cacheList1=cacheList2
    cacheList2=[]
    if len(cacheList1)==0:
        break
if len(Fare)==0:
    print("-1")
else:
    print(min(Fare))