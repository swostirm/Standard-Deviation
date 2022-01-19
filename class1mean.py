import csv
import pandas as pd
import plotly_express as px

with open("class1.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
total=0

for x in new_data:
    total+=x

mean=total/n 
print("mean",str(mean)) 

df=pd.read_csv("class1.csv")

fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=n)])
fig.update_yaxes(rangemode="tozero")
fig.show()




