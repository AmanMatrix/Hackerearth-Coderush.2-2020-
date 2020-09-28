Fare=[]
sectorConnectionsStr=input()
listSectorsConnections=sectorConnectionsStr.split(" ")
i=0
for values in listSectorsConnections:
    listSectorsConnections[i]=int(values)
    i+=1
    if int(values)==listSectorsConnections[0]:
        if listSectorsConnections[0]>=1 and listSectorsConnections[0]<=50000:pass
        else:exit()
    if int(values)==listSectorsConnections[1]:
        if listSectorsConnections[1]>=1 and listSectorsConnections[1]<=500000:pass
        else:exit()
ABFare=[]
i=0
while(i<listSectorsConnections[1]):
    ABFare.append(input())
    i+=1
i=0
for SectorFare in ABFare:
    ABFare[i]=SectorFare.split(" ")
    i+=1
for strFare in ABFare:
    i=0
    for vals in strFare:
        strFare[i]=int(vals)
        i+=1
cacheList1=[]
i=0
for SectorFare1 in ABFare:
    if SectorFare1[0]==1:
        cacheList1.append([SectorFare1[1],SectorFare1[2]])
    else:pass
    i+=1
cacheList2=[]
while(1):
    for secs in cacheList1:
        if secs[0]==listSectorsConnections[0]:
            Fare.append(secs[1])
        elif secs[0]<listSectorsConnections[0]:
            for SectorFare1 in ABFare:
                if SectorFare1[0]==secs[0]:
                    if SectorFare1[2]-secs[1]<0:
                        SectorFare1[2]=secs[1]
                    else:pass
                    cacheList2.append([SectorFare1[1],(SectorFare1[2]-secs[1])+secs[1]])  
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