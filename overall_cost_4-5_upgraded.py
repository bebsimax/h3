from main import units, town_colors
import pandas as pd
import matplotlib.pyplot as plt

tiers = (4, 5)
state = "upgraded"
units = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}"')
units["max_gold_cost"] = units.max_growth * units.gold_cost

t = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t["max_gold_cost"] = units.groupby(["fraction"])['max_gold_cost'].sum()


t = t.sort_values(by="max_gold_cost", ascending=False)

indexes = t.index.values
colors_in_order = [town_colors[town] for town in indexes]

t.plot(y=0, kind='bar', color=colors_in_order, figsize=(16.5, 8.5), xlabel="towns", ylabel="gold", legend=False,
       title='cost of units tiers 4-5 for each town max growth', ylim=(4_000, 9_000))


plt.show()