from main import units, town_colors, chart_data_path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


tiers = (1, 7)
state = "upgraded"
title_1 = '% of tier 4-5 units cost in overall towns cost'
title_2 = 'gold cost of maximum growth for each town, units tiers 4-5'
chart_name = title_1 + ' + ' + title_2

fig, axes = plt.subplots(nrows=2, ncols=1)

units_all_tiers = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}"')
units_all_tiers["max_gold_cost"] = units.max_growth * units.gold_cost
t = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t["overall_gold_cost"] = units_all_tiers.groupby(["fraction"])['max_gold_cost'].sum()

tiers = (4, 5)
units_tier_45 = units_all_tiers.query(f'tier >= {tiers[0]} & tier <= {tiers[1]}')
t["gold_cost13"] = units_tier_45.groupby(["fraction"])['max_gold_cost'].sum()
t["%"] = t.gold_cost13 / t.overall_gold_cost * 100
t = t.sort_values(by="%", ascending=False)

indexes = t.index.values
colors_in_order = [town_colors[town] for town in indexes]

chart = t.plot(ax=axes[0], y=2, kind='bar', color=colors_in_order, figsize=(18, 10), xlabel="towns", ylabel="%", legend=False,
       title=title_1, rot=0, ylim=(15,33))


tiers = (4, 5)
state = "upgraded"

units_tier_45_2 = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}"')
units_tier_45_2["max_gold_cost"] = units_tier_45_2.max_growth * units_tier_45_2.gold_cost

t_2 = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t_2["max_gold_cost"] = units_tier_45_2.groupby(["fraction"])['max_gold_cost'].sum()


t_2 = t_2.sort_values(by="max_gold_cost", ascending=False)

indexes = t_2.index.values
colors_in_order = [town_colors[town] for town in indexes]

chart_2 = t_2.plot(ax=axes[1], y=0, kind='bar', color=colors_in_order, figsize=(18, 10), xlabel="towns", ylabel="gold",
                   legend=False, title=title_2, rot=0, ylim=(5_000, 8_400))


fig = chart.get_figure()
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))

plt.show()

