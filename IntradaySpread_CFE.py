# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:57:02 2016

@author: T450
"""

import numpy as np
import pandas as pd
import WindPy
from pandas import Series,DataFrame
from WindPy import *
import matplotlib.pyplot as plt
w.start()

temp2=[]
temp=[]
product=["IF00.CFE","IF01.CFE",\
         "IH00.CFE","IH01.CFE",\
         "IC00.CFE","IC01.CFE"
        ]
fig=plt.figure(figsize=(20,10))

for j in range(3):
    ax=fig.add_subplot(3,1,j+1)
    temp3=len(w.wsi(product[0],"close",datetime.today()-timedelta(1)).Times)
    data=pd.DataFrame(np.zeros((temp3,2)))
    for i in range(2):
        temp=w.wsi(product[2*(j)+i],"close",datetime.today()-timedelta(1))
        temp2=np.array(temp.Data).T
        data[i]=pd.DataFrame(temp2)
    diff=data[0]-data[1]
    diff.index=temp.Times
    diff=diff.dropna()
    
    ax.plot(diff)
    ax.set_xticks([0,60,120,180,240])
    ax.set_title("%s %s-%s Sprd[%s/%s]"%(date.today(),product[2*(j)],product[2*j+1],diff.quantile(0.1),diff.quantile(0.9)))

