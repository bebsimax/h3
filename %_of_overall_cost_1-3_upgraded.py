from main import units, town_colors, chart_data_path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


tiers = (1, 7)
state = "upgraded"
title = '% of towns overall cost are units tiers 1-3'



units = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}" & name != "corsairs"')
units["max_gold_cost"] = units.max_growth * units.gold_cost
t = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t["overall_gold_cost"] = units.groupby(["fraction"])['max_gold_cost'].sum()

tiers = (1, 3)
units = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]}')
t["gold_cost13"] = units.groupby(["fraction"])['max_gold_cost'].sum()
t["%"] = t.gold_cost13 / t.overall_gold_cost * 100
t = t.sort_values(by="%", ascending=False)

indexes = t.index.values
colors_in_order = [town_colors[town] for town in indexes]

chart = t.plot(y=2, kind='bar', color=colors_in_order, figsize=(16.5, 8.5), xlabel="towns", ylabel="%", legend=False,
       title=title, ylim=(20, 35))
fig = chart.get_figure()
fig.savefig(os.path.join(chart_data_path, title + '.png'))

plt.show()















