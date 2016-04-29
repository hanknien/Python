# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:12:43 2016

@author: Administrator
"""

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
from WindPy import *
import matplotlib.pyplot as plt
w.start()

start=w.tdaysoffset(0,date.today()).Data[0][0]
end=w.tdaysoffset(0,date.today()).Data[0][0]
hourstart=timedelta(9.5/24)#代表21:00:00
hourend=timedelta(15.0/24.0)#代表16:00:00

product=["510050.SH","IH00.CFE",\
         "510300.SH","IF00.CFE",\
         "510500.SH","IC00.CFE"    
        ]
        
fig=plt.figure(figsize=(10,10))
w.wsq("000001.SZ", "rt_pre_close")
for j in range(3):
    diff=[]
    data=[]
    ax=fig.add_subplot(3,1,j+1)
    temp3=len(w.wsi(product[0],"close",start+hourstart,\
              end+hourend).Times)
    data=pd.DataFrame(np.zeros((temp3,2)))
    for i in range(2):
        temp=w.wsi(product[2*(j)+i],"close",start+hourstart,\
              end+hourend)
        temp2=np.array(temp.Data).T/w.wsq(product[2*j+i],"rt_pre_close").Data[0][0]
        data[i]=pd.DataFrame(temp2)
    diff=(data[0]-data[1])*100
    diff.index=temp.Times
    diff=diff.dropna()
    
    ax.plot(diff)
    ax.set_xticks([0,60,120,180,240])
    ax.set_yticklabels(['%.2f'%m for m in ax.get_yticks().tolist()]) 
    ax.set_title("%s %s-%s Sprd"%(end.date(),product[2*(j)],product[2*j+1]))
