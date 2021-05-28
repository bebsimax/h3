from main import units, town_colors, legend_elements, chart_data_path
from common import average_damage
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn

title = 'Average damage per unit, basic versions'
chart_name = title
state = 'basic'

units_basic = units.query(f"state == '{state}'")

units_basic = units_basic.assign(avg_dmg=units_basic.apply(average_damage.avg_dmg, axis=1))


units_plot = units_basic[["name", "avg_dmg", "fraction", "tier"]]
units_plot.sort_values(inplace=True, by='avg_dmg', ascending=False)
fig = plt.figure(figsize=(14, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1)


for i in range(len(units_plot)):
    unit = units_plot.iloc[i]
    ax.barh(width=unit["avg_dmg"], color=town_colors[unit["fraction"]], y=unit["name"], align='center')
ax.set_xticks(list(range(0, int(max(units_plot["avg_dmg"])) + 1, 5)))
ax.set_xlabel('Average damage', fontsize=16)
ax.set_ylabel('Unit', fontsize=16)
ax.set_title(title, fontsize=18)
ax.set_yticklabels(labels=units_plot["name"], fontsize=8)
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))
plt.show()