from main import units, town_colors, legend_elements, chart_data_path
from common import average_damage
import pandas as pd
import matplotlib.pyplot as plt
import os

chart_name = "sorted by damage"
set_gold = 5000
chart_path = os.path.join(chart_data_path, f"{chart_name}.png")
states = ['upgraded', 'neutral']
def set_avarage_damage(row):
    if "twice" in row["special"]:
        return average_damage.av_dmg(row["damage_min"], row["damage_max"], row["attack"]) * 2 * (set_gold/row["gold_cost"])
    else:
        return average_damage.av_dmg(row["damage_min"], row["damage_max"], row["attack"]) * (set_gold/row["gold_cost"])

units = units.query(f'state == "{states[0]}" or state == "{states[1]}"')
units = units.assign(average_damage=units.apply(set_avarage_damage, axis=1))
units = units.sort_values(by="average_damage", ascending=False)


def plot_with_colors(data, y, colors, x=0):
    if x == 0:
        for i in range(len(data)):
            plt.barh(y=data.iloc[i]["name"], width=data.iloc[i][y], color=colors[data.iloc[i]["fraction"]])
        else:
            plt.legend(handles=legend_elements)
            plt.xlabel('Average damage per 5000 gold vs 0 defense target')
            plt.yticks(fontsize=8)
            plt.legend(handles=legend_elements)
            fig = plt.gcf()
            fig.set_size_inches(18, 10)
            plt.savefig(fname=chart_path, dpi=350, format="png")
            plt.show()


plot_with_colors(units, "average_damage", town_colors)






