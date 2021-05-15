from main import units, town_colors
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt



set_gold = 5000
states = ['upgraded', 'neutral']
def set_avarage_damage(row):
    if row["gold_cost"] == 0:
        return 0
    if "twice" in row["special"]:
        return ((row["damage_min"] * 0.05 * row["attack"]) + (row["damage_max"] * 0.05 * row["attack"])) /row["gold_cost"] * set_gold
    else:
        return ((row["damage_min"] * 0.05 * row["attack"]) + (row["damage_max"] * 0.05 * row["attack"])) /2 /row["gold_cost"] * set_gold
units = units.query(f'state == "{states[0]}" or state == "{states[1]}"')
units = units.assign(avarage_damage=units.apply(set_avarage_damage, axis=1))
units = units.sort_values(by="avarage_damage", ascending=False)
units.plot(x=0, y=16, kind='barh', figsize=(16.5, 8.5), ylabel=f"damage per {set_gold} gold", xlabel="unit", legend=False,
       title=f'upgraded and neutral units damage per {set_gold} gold')
plt.show()