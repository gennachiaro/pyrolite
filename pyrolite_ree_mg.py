
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pyrolite.plot
from pyrolite.plot import pyroplot
from pyrolite.plot.spider import REE_v_radii
from pyrolite.geochem.ind import REE, get_ionic_radii
from pyrolite.geochem.norm import get_reference_composition, all_reference_compositions

# import chondrite data
chondrite = get_reference_composition("Chondrite_MS95")
CI = chondrite.set_units("ppm")

fig, ax = plt.subplots(1)

for name, ref in list(all_reference_compositions().items())[::2]:
    if name != "Chondrite_MS95":
        ref.set_units("ppm")
        ref.comp.pyrochem.REE.pyrochem.normalize_to(CI, units="ppm").pyroplot.REE(
            unity_line=True, ax=ax, label=name
        )

ax.set_ylabel("X/X$_{Chondrite}$")
ax.legend(frameon=False, facecolor=None, loc="upper left", bbox_to_anchor=(1.0, 1.0))
plt.show()