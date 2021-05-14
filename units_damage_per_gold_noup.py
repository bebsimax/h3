from main import towns_noup, town_colors, legend_elements
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt
list_of_damage_per_gold=[]

for key, value in towns_noup.items():
    for i in range(len(value)):
        unit_name = value.iloc[i]['name']
        unit_min_damage = value.iloc[i]['damage_min']
        unit_max_damage = value.iloc[i]['damage_max']
        unit_attack = value.iloc[i]['attack']
        unit_cost = value.iloc[i]['gold_cost']
        min_damage_per_gold = unit_min_damage*0.05*unit_attack/unit_cost*5000
        max_damage_per_gold = unit_max_damage*0.05*unit_attack/unit_cost*5000
        average_damage_per_gold = (min_damage_per_gold+max_damage_per_gold)/2
        list_of_damage_per_gold.append([unit_name, round(average_damage_per_gold,4), key])
else:
    list_of_damage_per_gold = sorted(list_of_damage_per_gold, key=itemgetter(1), reverse=True)


for unit_name, value, town_name in list_of_damage_per_gold:
    plt.barh(unit_name, value, color=town_colors[town_name], align='edge', height=0.6)
else:
    plt.xlabel('Avarage damage per 5000 gold')
    plt.yticks(fontsize=8)
    plt.legend(handles=legend_elements)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.show()