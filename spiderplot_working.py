#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:36:13 2019

@author: gennachiaro
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pyrolite.plot
from pyrolite.plot.spider import spider

#read in data
df = pd.read_csv('/users/gennachiaro/Documents/Vanderbilt/Research/Ora Caldera/Trace Elements/Rare Earth Elements/REE_Mean_Normalized.csv', index_col=0)

#set values
MG = df.loc[['ORA-2A-001','ORA-2A-005','ORA-2A-018','ORA-2A-031','ORA-2A-032','ORA-2A-035','ORA-2A-040']]
VCCR = df.loc [['ORA-5B-402','ORA-5B-404A','ORA-5B-404B','ORA-5B-405','ORA-5B-406','ORA-5B-407','ORA-5B-408-SITE2','ORA-5B-408-SITE7','ORA-5B-408-SITE8','ORA-5B-409','ORA-5B-411','ORA-5B-412A-CG','ORA-5B-412B-CG','ORA-5B-413','ORA-5B-414-CG','ORA-5B-415','ORA-5B-416','ORA-5B-417']]
FG = df.loc [['ORA-5B-410','ORA-5B-412A-FG','ORA-5B-412B-FG','ORA-5B-414-FG']]
FGCP = df.loc[['ORA-2A-002_Type1','ORA-2A-002_Type2','ORA-2A-002','ORA-2A-003','ORA-2A-016_Type1','ORA-2A-016-Type2','ORA-2A-016-Type3','ORA-2A-016-Type4','ORA-2A-023','ORA-2A-024','MINGLED1-ORA-2A-024','MINGLED2-ORA-2A-024','MINGLED3-ORA-2A-024']]

#plot diagrams
MG.pyroplot.spider(color="green",alpha = 0.5, mode = "fill")

VCCR.pyroplot.spider(color="red",alpha = 0.5, mode = "fill")

FG.pyroplot.spider(color="purple",alpha = 0.5, mode = "fill")

FGCP.pyroplot.spider(color="blue",alpha = 0.5, mode = "fill")


#set background
sns.set_style("darkgrid")


#plot graph
plt.show()