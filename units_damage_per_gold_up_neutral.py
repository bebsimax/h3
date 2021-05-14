from main import units, town_colors, legend_elements
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt


units_up_and_neutral = [units[0], units[2]]
set_gold = 5000
list_of_damage_per_gold=[]
for faction in units_up_and_neutral:
    for key, value in faction.items():
        for i in range(len(value)):
            unit_name = value.iloc[i]['name']
            unit_min_damage = value.iloc[i]['damage_min']
            unit_max_damage = value.iloc[i]['damage_max']
            unit_attack = value.iloc[i]['attack']
            unit_cost = value.iloc[i]['gold_cost']
            if unit_cost == 0:
                continue
            min_damage_per_gold = unit_min_damage*0.05*unit_attack/unit_cost
            max_damage_per_gold = unit_max_damage*0.05*unit_attack/unit_cost
            average_damage_per_gold = (min_damage_per_gold+max_damage_per_gold)/2
            average_damage_per_set_gold = average_damage_per_gold * set_gold
            list_of_damage_per_gold.append([unit_name, round(average_damage_per_set_gold, 4), key])
else:
    list_of_damage_per_gold = sorted(list_of_damage_per_gold, key=itemgetter(1), reverse=True)


for unit_name, value, town_name in list_of_damage_per_gold:
    plt.barh(unit_name, value, color=town_colors[town_name], align='edge', height=0.6)
else:
    plt.xlabel('Avarage damage per 5000 gold')
    plt.yticks(fontsize=8)
    plt.legend(handles = legend_elements)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    plt.show()