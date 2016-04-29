# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:18:48 2016

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:57:02 2016

@author: T450
"""

import numpy as np
import pandas as pd
import WindPy
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from WindPy import *
w.start()

start=w.tdaysoffset(-1,date.today()).Data[0][0]
end=w.tdaysoffset(0,date.today()).Data[0][0]
hourstart=timedelta(0.875)#代表21:00:00
hourend=timedelta(0.667)#代表16:00:00
temp2=[]
temp=[]
#找主力和次主力合约
productlist=["AU","AG","CU","NI","RU","RB"]
product=[]
for i in range(6):
    contract=Series(np.zeros(9))
    volume=Series(np.zeros(9))
    for j in range(9):
        contract[j]="%s0%s.SHF"%(productlist[i],j)
        data=w.wsd(contract[j], "volume",start,start,"").Data[0][0]
        if data is None:
            data=0
        volume[j]=Series(data)
        volume.sort(ascending=False)
    product.append(contract[volume.index[0]])
    product.append(contract[volume.index[1]])
    
    
fig=plt.figure(figsize=(20,10))

for j in range(6):
    ax=fig.add_subplot(3,2,j+1)
    temp3=len(w.wsi(product[j],"close",start+hourstart,\
              end+hourend).Times)
    data=pd.DataFrame(np.zeros((temp3,2)))
    for i in range(2):
        
        temp=w.wsi(product[2*(j)+i],"close",start+hourstart,\
              end+hourend)
        temp2=np.array(temp.Data).T
        data[i]=pd.DataFrame(temp2)
    diff=data[0]-data[1]
    diff.index=temp.Times
    diff=diff.dropna()
    
    ax.plot(diff)
    ax.set_xticks([0,60,120,180,240,300,360,420,480])
    
    ax.set_title("%s %s-%s Sprd[%s/%s]"%(end.date(),product[2*(j)],product[2*j+1],diff.quantile(0.05),diff.quantile(0.95)))
