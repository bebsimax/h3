from main import units, town_colors, chart_data_path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from common import ehp


current_attack = 10
ehp.ATTACK = current_attack

title = f'Numbers of units killed with dmg = max health, attacker Attack = {current_attack}'
chart_name = title
state = 'upgraded'

units_basic = units.query(f"state == '{state}'")

units_basic = units_basic.assign(e_hp=units_basic.apply(ehp.e_hp_coef, axis=1))

units_plot = units_basic[["name", "e_hp", "fraction", "tier"]]
units_plot.sort_values(inplace=True, by='e_hp', ascending=False)
fig = plt.figure(figsize=(14, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1)


for i in range(len(units_plot)):
    unit = units_plot.iloc[i]
    ax.barh(width=unit["e_hp"], color=town_colors[unit["fraction"]], y=unit["name"], align='center')
ax.set_xlabel('eHP', fontsize=16)
ax.set_ylabel('Unit', fontsize=16)
ax.set_title(title, fontsize=18)
ax.set_yticklabels(labels=units_plot["name"], fontsize=5)
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))
#plt.grid()
plt.show()


