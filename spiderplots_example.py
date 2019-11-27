#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:58:44 2019

@author: gennachiaro
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyrolite.plot import pyroplot
from pyrolite.plot.spider import spider
from pyrolite.geochem.ind import common_elements

np.random.seed(82)
# create some example data
els = common_elements(cutoff= 90)
ys = np.random.rand(3, len(els))
ys = np.exp(ys)
df = pd.DataFrame(data=ys, columns=els)

ax = spider(df.loc[0, :].values, color="k")


# or, alternatively directly from the dataframe:
ax = df.loc[0, :].pyroplot.spider(color="k")
ax.set_ylabel("Abundance")

# This behaviour can be modified (see spider docs) to provide filled ranges:
ax = spider(df.values, mode="fill", color="k", alpha=0.5)

# or, alternatively directly from the dataframe:
ax = df.pyroplot.spider(mode="fill", color="k", alpha=0.5)
ax.set_ylabel("Abundance")


# The plotting axis can be specified to use exisiting axes:
fig, ax = plt.subplots(2, 1, sharex=True, sharey=True, figsize=(10, 6))
ax[0].set_ylabel("Abundance")

df.pyroplot.spider(ax=ax[0], color="k")
df.pyroplot.spider(ax=ax[1], mode="fill", color="k", alpha=0.5)

plt.tight_layout()


# spiders are most commonly used to disply normalised abundances. This is easily
# accomplished using pyrolite.norm:
from pyrolite.geochem.norm import get_reference_composition

rc = get_reference_composition("Chondrite_PON")
normdf = df.pyrochem.normalize_to("Chondrite_MS95",units="ppm")

ax = spider(normdf.values, color="k")

# or, alternatively directly from the dataframe:
ax = normdf.pyroplot.spider(color="k")

ax.set_ylabel("Abundance / Chondrite")