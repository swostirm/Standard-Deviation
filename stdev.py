import csv
import math

with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0

    for x in data:
        total+=int(x)

    mean=total/n  
    
    return(mean)
squared_list=[]

for n in data:
    a=int(n)-mean(data)
    a=a**2
    squared_list.append(a)
    
sum=0

for x in squared_list:
    sum+=x
result=sum/(len(data)-1)

stdev=math.sqrt(result)

print(stdev)
