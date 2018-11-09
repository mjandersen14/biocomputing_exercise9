"""
Created on Fri Nov  2 10:37:18 2018

@author: marissaandersen
"""
#Question 1
import pandas as pd
data=pd.read_csv("GPA.txt", header=0, sep=",")

from plotnine import *
a=ggplot(data,aes(x="GPA", y="Attendence"))+geom_point()+theme_classic()
a+xlab("Grade Point Average (GPA)")+ylab("Attendence (days)")+stat_smooth(method="lm")



#Question 2 
import pandas as pd 
datafile=pd.read_csv("data.txt", header=0, sep=",")
from plotnine import *
#Bargraph
n=pd.DataFrame(columns=['North'])
s=pd.DataFrame(columns=['South'])
e=pd.DataFrame(columns=['East'])
w=pd.DataFrame(columns=['West'])
for i in range(0,len(datafile)):
    if  datafile.iloc[i,0]=='north':
        N=datafile.iloc[i,1]
        n=n.append({'North':N},ignore_index=True)
    elif datafile.iloc[i,0]=='south':
        S=datafile.iloc[i,1]
        s=s.append({'South':S},ignore_index=True)
    elif datafile.iloc[i,0]=='east':
        E=datafile.iloc[i,1]
        e=e.append({'East':E},ignore_index=True)
    else:
        W=datafile.iloc[i,1]
        w=w.append({'West':W},ignore_index=True)
all=pd.concat([n,s,e,w],axis=1,sort=True) 
meannorth=sum(all.North)/len(all)
meansouth=sum(all.South)/len(all)
meaneast=sum(all.East)/len(all)  
meanwest=sum(all.West)/len(all)

means=pd.DataFrame(columns=["Region","Mean"])
means=means.append({"Region":'North',"Mean":meannorth},ignore_index=True)
means=means.append({"Region":'South',"Mean":meansouth},ignore_index=True)
means=means.append({"Region":'East',"Mean":meaneast},ignore_index=True)
means=means.append({"Region":'West',"Mean":meanwest},ignore_index=True)
print (means)
d=ggplot(means)+theme_classic()+xlab("Region")+ylab("Mean")
d+geom_bar(aes(x="Region",y="Mean"), stat="identity")





#Scatter plot
a=ggplot(datafile,aes(x="region", y="observations"))+geom_jitter(size=0.01)+theme_classic()
a+xlab("Region")+ylab("Observation")































































