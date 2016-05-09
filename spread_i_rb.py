# -*- coding: utf-8 -*-
"""
Created on Fri May 06 13:00:05 2016

@author: Administrator
"""
mapar=10
mapar1=20
stdpar=2
multiplier1=100
multiplier2=10
lot1=1
lot2=2
# I vs RB spread
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

spread=pd.read_csv('C:\Users\T450\Documents\Python Code\spread_i_rb.csv',sep=',')
spread=spread.fillna(method='pad')
date=spread.Time.str.split(' ').str[0]
spread['date']=date
spread['ratio']=spread.I/spread.RB
temp=pd.DataFrame(np.zeros([len(spread),4]),columns=['ma','stdd','signal','dailypl'])
spread=pd.merge(spread,temp,right_index=True,left_index=True)
spread['ma']=np.zeros(len(spread))


ma=[]
k=0
m=1
for i in range(len(spread)):
#for i in range(450):   
    if k>mapar-1:
        spread.loc[i,'ma']=spread['ratio'][i-mapar:i].mean()
        spread.loc[i,'stdd']=spread['ratio'][i-mapar:i].std()
#        if spread['ratio'][i]<spread['ma'][i]-stdpar*spread['stdd'][i]:
#            spread.loc[i,'signal']="B"
#        elif spread['ratio'][i]>spread['ma'][i]+stdpar*spread['stdd'][i]:
#            spread.loc[i,'signal']="S"
#        else:
#            spread.loc[i,'signal']=spread['signal'][i-1]
#            
#        if spread['signal'][i-1]=="B":
#            spread.loc[i,'dailypl']=lot1*multiplier1*(spread['I'][i]-spread['I'][i-1])\
#                                    -lot2*multiplier2*(spread['RB'][i]-spread['RB'][i-1])
#        elif spread['signal'][i-1]=="S":
#            spread.loc[i,'dailypl']=-lot1*multiplier1*(spread['I'][i]-spread['I'][i-1])\
#                                    +lot2*multiplier2*(spread['RB'][i]-spread['RB'][i-1])
        if m>mapar1-1:
            spread.loc[i,'slope']=(spread['ma'][i-(mapar1-mapar-1)]-spread['ma'][i])/(mapar1-mapar)
        
    if i<>len(spread)-1:
        if spread.date[i]!=spread.date[i+1]:
            k=0
            m=1
        else:
            k+=1
            m+=1




#a=np.cumsum(spread['dailypl'])
#plt.plot(a)
    
#spread['ma']=ma
#spread['std']=std