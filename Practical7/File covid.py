from operator import truediv
import os
from pickle import TRUE
from sqlite3 import Row
from tkinter import Y
import turtle
from xmlrpc.client import boolean
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #import some python library
os.chdir("F:\Python")# it can allow us to use the data even in different files 
covid_data = pd.read_csv("full_data(2).csv")# after that we can use covid_data to use full_data(2).csv
os.listdir("F:\Python")
print(os.listdir("F:\Python"))#it use to examine the way of the file is correct

covid_data.head(5)
print(covid_data.head(5))#according to print, I find that head(5)means the fisrt 5 lines' data

covid_data.info()# it can give us some basic information about this document 

covid_data.describe()
print(covid_data.describe())#the mean of new cases is 194.546773  and the standard deviation is 2083.395028
#the range of the total cases is from 0 to 777798

covid_data.iloc[9,2]
print(covid_data.iloc[9,2])

covid_data.iloc[2,0:5]#it shows the 2 column from ROW 0-5
covid_data.iloc[0:2,:]# it shows the all column from row 0-2
covid_data.iloc[0:10:2,0:5] 
print(covid_data.iloc[0:10:2,0:5]) # it show s the 0-5column from row 0,2,4,6,8 (0-10 in 2 steps)
covid_data.iloc[0:3,[0,1,3]]

my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]# this two are the same

covid_data.loc[2:4,"date"]
print(covid_data.loc[2:4,"date"])# it will show the date from row 2-4
covid_data.loc[0:81,"total_cases"]
print(covid_data.loc[0:81,"total_cases"])# it will not find what the location is from

data_gender  = covid_data[['location','total_cases']]# select the column that we need 
data_gender_re = data_gender[data_gender.notnull()]
x = data_gender_re[(data_gender['location']=='Afghanistan')] #select all the Afghanistan in the location
print(x)# show the result

#5 Examining the situation of China
a = covid_data[['date','location','new_cases','new_deaths']]# choose the row we need to select
china_new_data =  a[a['location']=='China']  # select the location is China
china_new_data_re = china_new_data[china_new_data.notnull()]
print(china_new_data)# show the data
plt.figure("4 subplot")# it can name the figure title
plt.subplot(221)
plt.boxplot(china_new_data_re[["new_cases"]],showfliers=False)# this graph is about new cases
plt.title("China new cases")

plt.subplot(222)
plt.boxplot(china_new_data_re[["new_deaths"]],showfliers=False)# this graph is about new  deaths
plt.title("China new deaths")

#the first two figure is boxplot
china_dates = china_new_data["date"]
china_new_cases = china_new_data['new_cases']# it give a defination
china_new_deaths = china_new_data['new_deaths']
plt.subplot(223)
plt.plot(china_dates, china_new_cases, 'b+')#b+, 'r+' or 'bo are different kinds of the plot (b is blue means colour + is the size)
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)# it will provide x-axis site and rotation is showed the angle
plt.title("China new cases with time going by")

plt.subplot(224)
plt.plot(china_dates,china_new_deaths,'r+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=90)
plt.title('China new deaths with time going by')
plt.show()# show the boxplot