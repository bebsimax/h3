from main import units, town_colors, chart_data_path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

tiers = (6, 7)
state = "upgraded"
title = 'gold cost of maximum growth for each town, units tiers 6-7'

units = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}"')
units["max_gold_cost"] = units.max_growth * units.gold_cost

t = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t["max_gold_cost"] = units.groupby(["fraction"])['max_gold_cost'].sum()


t = t.sort_values(by="max_gold_cost", ascending=False)

indexes = t.index.values
colors_in_order = [town_colors[town] for town in indexes]

chart = t.plot(y=0, kind='bar', color=colors_in_order, figsize=(16.5, 8.5), xlabel="towns", ylabel="gold", legend=False,
       title=title, ylim=(9_000, 17_000))
fig = chart.get_figure()
fig.savefig(os.path.join(chart_data_path, title + '.png'))

plt.show()