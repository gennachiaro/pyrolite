#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:36:13 2019

@author: gennachiaro
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyrolite.plot import pyroplot
from pyrolite.plot.spider import spider
from pyrolite.geochem.ind import common_elements


#els = common_elements
df = pd.read_excel('/users/gennachiaro/Documents/Vanderbilt/Research/Ora Caldera/Trace Elements/Spider Plots/SpiderPlots.xlsx')

print (df)

from pyrolite.geochem.norm import get_reference_composition

ref = get_reference_composition("Chondrite_MS95")

MS95 = rc["Chondrite_MS95"]


normdf = MS95.normalize(df)

ax = spider(normdf.values, color="k")



ax = normdf.pyroplot.spider(color="k")

#ax.set_ylabel("Abundance / Chondrite")




# This behaviour can be modified (see spider docs) to provide filled ranges:
ax = spider(normdf.values, mode="fill", color="k", alpha=0.5)
# or, alternatively directly from the dataframe:
ax = normdf.pyroplot.spider(mode="fill", color="k", alpha=0.5)
ax.set_ylabel("Abundance")


# The plotting axis can be specified to use exisiting axes:
fig, ax = plt.subplots(2, 1, sharex=True, sharey=True, figsize=(10, 6))


normdf.pyroplot.spider(ax=ax[0], color="k")
normdf.pyroplot.spider(ax=ax[1], mode="fill", color="k", alpha=0.5)

plt.tight_layout()





