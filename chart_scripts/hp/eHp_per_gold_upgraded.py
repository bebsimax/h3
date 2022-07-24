from main import units, town_colors, chart_data_path
import pandas as pd
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import seaborn as sns
import os
from common import ehp
# FIXME: not negative values?
ehp.ATTACK = 40
gold = 1
tiers = (1, 7)
state = "upgraded"
title = f'eHp per {gold} gold - units upgraded vs {ehp.ATTACK} attack'
chart_name = title

units_basic = units.query(f"state == '{state}'")

units_basic = units_basic.assign(eHP=units_basic.apply(ehp.e_hp, axis=1))
units_basic = units_basic.assign(eHP_per_gold=gold/units_basic["gold_cost"] * units_basic["eHP"])

units_plot = units_basic[["name", "eHP_per_gold", "fraction", "tier"]]
units_plot.sort_values(inplace=True, by='eHP_per_gold', ascending=False)
fig = plt.figure(figsize=(14, 8), dpi=150)
ax = fig.add_subplot(1, 1, 1)

for i in range(len(units_plot)):
    unit = units_plot.iloc[i]
    ax.barh(width=unit["eHP_per_gold"], color=town_colors[unit["fraction"]], y=unit["name"], align='center')
ax.tick_params(axis='x', labelsize=5)
ax.set_xlabel(f'eHP per {gold} gold', fontsize=8)
ax.set_ylabel('Unit', fontsize=8)
ax.set_title(title, fontsize=8)
ax.set_yticklabels(labels=units_plot["name"], fontsize=4.8)


fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))
plt.show()
