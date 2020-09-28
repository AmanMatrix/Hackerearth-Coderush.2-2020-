d=int(input())
valueStr=input()
value=valueStr.split(" ")
if len(value)==d and d>=2 and d<=200000:
    for stockValue in value:
        if int(stockValue)>=1 and int(stockValue)<=10**16:
            pass
        else:exit()
    diffValues=[]
    x=0
    for values1 in value:
        y=0
        for values2 in value:
            if x<y:
                diffValues.append(int(values1)-int(values2))
            else:pass
            y+=1
        x+=1
    diffValues.sort(reverse=True)
    positive=[]
    for diffs in diffValues:
        if diffs>0:
            positive.append(diffs)
        else:pass
    positive.sort()
    print(positive[0])
else:exit()
    