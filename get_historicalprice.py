# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:53:24 2016

@author: T450
"""
import pandas as pd
from WindPy import *
w.start()
alldata=[]
product=["AU1306.SHF","AU1312.SHF","AU1406.SHF","AU1412.SHF","AU1506.SHF","AU1512.SHF","AU1606.SHF","AU1612.SHF"]
lastdate=w.wsd(product, "lasttrade_date", date.today(),date.today(), "").Data[0]
lastdate[-1]=date.today()-timedelta(1)
for i in range(2,len(product)):
    
    temp=w.wsi(product[i], "close", lastdate[i-2], lastdate[i]+timedelta(1), "periodstart=09:00:00;periodend=15:00:00")
    data=pd.DataFrame(temp.Data[0],index=temp.Times,columns=[product[i]])
    alldata.append(data)


