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
#bar graph of means of the four populations 
#make new DF with 5 columns (one for each region)


#scatter plot
a=ggplot(datafile,aes(x="region", y="observations"))+geom_jitter(size=0.01)+theme_classic()
a+xlab("Region")+ylab("Observation")

































































































