# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:18:15 2016

@author: T450
"""
import numpy as np
import pandas as pd
import WindPy
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from WindPy import *
w.start()


hourstart=timedelta(0.375)#代表21:00:00
hourend=timedelta(0.667)#代表16:00:00
temp2=[]
temp=[]
#找主力和次主力合约
productlist=["AU","AG","CU","NI","RU","RB"]
product=[]
period=[]

for m in range(-500,0):
    start=w.tdaysoffset(m,date.today()).Data[0][0]
    print m
    allcontract=[]
    for i in range(6):
        contract=[]
        volume=Series(np.zeros(12)) 
        for k in range(12):
            if (k+1)<10:
               contract.append("%s0%sM.SHF"%(productlist[i],k+1))
            else:
               contract.append("%s%sM.SHF"%(productlist[i],k+1)) 
            
        volume=Series(w.wsd(contract, "volume",start,start,"").Data[0])
#            if data is None:
#                data=0
        
        volume.sort(ascending=False)
        allcontract.append(contract[volume.index[0]])
        allcontract.append(contract[volume.index[1]])
    product.append(allcontract)
#        period.append(start.date())
    
    
#fig=plt.figure(figsize=(20,10))
#
#for j in range(6):
#    ax=fig.add_subplot(3,2,j+1)
#    temp3=len(w.wsi(product[0],"close",start+hourstart,\
#              end+hourend).Times)
#    data=pd.DataFrame(np.zeros((temp3,2)))
#    for i in range(2):
#        temp=w.wsi(product[2*(j)+i],"close",start+hourstart,\
#              end+hourend)
#        temp2=np.array(temp.Data).T
#        data[i]=pd.DataFrame(temp2)
#    diff=data[0]-data[1]
#    diff.index=temp.Times
#    diff=diff.dropna()
#    
#    ax.plot(diff)
#    ax.set_xticks([0,60,120,180,240,300,360,420,480])
#    ax.set_title("%s %s-%s Sprd[%s/%s]"%(start.date(),product[2*(j)],product[2*j+1],diff.quantile(0.05),diff.quantile(0.95)))
