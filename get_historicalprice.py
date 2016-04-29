# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:53:24 2016

@author: T450
"""
import pandas as pd
import numpy as np
from WindPy import *
w.start()
alldata=[]
#product=["AU1306.SHF","AU1312.SHF","AU1406.SHF","AU1412.SHF","AU1506.SHF","AU1512.SHF","AU1606.SHF","AU1612.SHF"]
#product=["AG1306.SHF","AG1312.SHF","AG1406.SHF","AG1412.SHF","AG1506.SHF","AG1512.SHF","AG1606.SHF","AG1612.SHF"]
product=['CU1406.SHF','CU1407.SHF','CU1408.SHF','CU1409.SHF','CU1410.SHF','CU1411.SHF','CU1412.SHF','CU1501.SHF','CU1502.SHF','CU1503.SHF','CU1504.SHF','CU1505.SHF','CU1506.SHF','CU1507.SHF','CU1508.SHF','CU1509.SHF','CU1510.SHF','CU1511.SHF','CU1512.SHF','CU1601.SHF','CU1602.SHF','CU1603.SHF','CU1604.SHF']

lastdate=w.wsd(product, "lasttrade_date", date.today(),date.today(), "").Data[0]
lastdate[-1]=date.today()-timedelta(1)
#for i in range(2,len(product)):
#    
#    temp=w.wsi(product[i], "close,volume", lastdate[i-2], lastdate[i]+timedelta(1), "periodstart=09:00:00;periodend=15:00:00")
#   
#   #data=pd.DataFrame(temp.Data[0],index=temp.Times,columns=[product[i]])
#    data=pd.DataFrame(temp.Data[0],index=temp.Times,columns=["%s_close"%product[i]])
#    b=temp.Data[1]
#    data.loc[:,"volume"]=temp.Data[1]
#    alldata.append(data)


for i in range(3,len(product)):
    
    #temp=w.wsi(product[i], "close,volume", lastdate[i-2], lastdate[i]+timedelta(1), "periodstart=09:00:00;periodend=15:00:00")
    temp=w.wsi(product[i], "close,volume", lastdate[i-3]-timedelta(5), lastdate[i-1], "periodstart=09:00:00;periodend=15:00:00")
   
   #data=pd.DataFrame(temp.Data[0],index=temp.Times,columns=[product[i]])
    data=pd.DataFrame(temp.Data[0],index=temp.Times,columns=["%s_close"%product[i]])
    data.loc[:,"volume"]=temp.Data[1]
    alldata.append(data)
