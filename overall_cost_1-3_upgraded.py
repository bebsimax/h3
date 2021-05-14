from main import units, town_colors
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt

tiers = (1, 3)
state = "upgraded"
c_unit = units.query(f'tier >= {tiers[0]} & tier <= {tiers[1]} & state == "{state}"')
c_unit['max_gold_cost'] = c_unit.gold_cost * c_unit.max_growth
t = pd.DataFrame(index=[town for town in town_colors.keys() if town != 'neutral'])
t["max_gold_cost"] = c_unit.groupby(["fraction"])['max_gold_cost'].sum()
t = t.reset_index()
t = t.rename(columns={"index": "name"})
t = t.sort_values(by=["max_gold_cost"], ascending=False)
plt.figure(figsize=(18.5, 10.5))
plt.title("cost of upgraded units tiers 1-3")
plt.ylim(6_000, 10_000)
for i in range(len(t)):
    plt.bar(x=t.iloc[i]["name"], height=t.iloc[i]["max_gold_cost"], width=0.4, color=town_colors[t.iloc[i]["name"]])

plt.show()















