from main import units, town_colors, legend_elements, chart_data_path
from common import ehp
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn

title = 'Ehp vs 0 attack, basic versions'
chart_name = title
state = 'basic'

units_basic = units.query(f"state == '{state}'")

units_basic = units_basic.assign(ehp=units_basic.apply(ehp.e_hp, axis=1))


units_plot = units_basic[["name", "ehp", "fraction", "tier"]]
units_plot.sort_values(inplace=True, by='ehp', ascending=False)
fig = plt.figure(figsize=(14, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1)


for i in range(len(units_plot)):
    unit = units_plot.iloc[i]
    ax.barh(width=unit["ehp"], color=town_colors[unit["fraction"]], y=unit["name"], align='center')
ax.set_xlabel('Effective health', fontsize=12)
ax.set_ylabel('Unit', fontsize=12)
ax.set_title(title, fontsize=14)
ax.set_yticklabels(labels=units_plot["name"], fontsize=6)
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))
plt.show()