from main import units, town_colors, legend_elements, chart_data_path
from common import average_damage
import pandas as pd
import matplotlib.pyplot as plt
import os

chart_name = "base"
set_damage = 500
chart_path = os.path.join(chart_data_path, f"{chart_name}.png")
states = ['upgraded', 'neutral']


def set_average_damage(row):
    if "twice" in row["special"]:
        return average_damage.av_dmg(row["damage_min"], row["damage_max"], row["attack"]) * 2
    else:
        return average_damage.av_dmg(row["damage_min"], row["damage_max"], row["attack"])

units = units.query(f'state == "{states[0]}" or state == "{states[1]}"')
units = units.assign(avg_dmg=units.apply(set_average_damage, axis=1))
units["growths"] = set_damage / units.avg_dmg / units.max_growth
units["gold_req"] = units.growths * units.gold_cost /1000
print(units.head())
#units = units.sort_values(by="average_damage", ascending=False)

units = units[["name", "fraction", "growths", "gold_req"]]
w = 0.3
units.sort_values('growths', ascending=True).plot(x=0, kind="barh", stacked=True, figsize=(18, 10), width=0.8,
                                                  fontsize=6,
                                                  ylabel="growths and gold in thousands",
                                                  xticks=range(0,115,5),
                                                  title=f"weeks of maximum growths and gold needed to reach {set_damage}")
plt.show()
'''
for (gold, name), group in units.groupby(["gold_req", "fraction"]):
    plt.barh(y=group["name"], width=group["growths"], color=town_colors[name])
    plt.barh(y=group["name"], width=group["gold_req"]+group["growths"], color="yellow")
else:
    plt.legend(handles=legend_elements)
    plt.xlabel('Average damage per 5000 gold vs 0 defense target')
    plt.yticks(fontsize=8)
    plt.legend(handles=legend_elements)
    plt.xscale("log")
    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.show()
'''