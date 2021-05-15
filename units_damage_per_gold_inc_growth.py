'''
from main import towns_noup, towns_up, town_colors
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
        unit_growth = value.iloc[i]['growth']
        min_damage_per_gold = unit_min_damage*0.05*unit_attack*unit_growth/unit_cost
        max_damage_per_gold = unit_max_damage*0.05*unit_attack*unit_growth/unit_cost
        if "twice" in value.iloc[i]['special']:
            average_damage_per_gold = (min_damage_per_gold + max_damage_per_gold)
        else:
            average_damage_per_gold = (min_damage_per_gold+max_damage_per_gold)/2
        list_of_damage_per_gold.append([unit_name, round(average_damage_per_gold,4), key])
else:
    list_of_damage_per_gold = sorted(list_of_damage_per_gold, key=itemgetter(1), reverse=True)


for unit_name, value, town_name in list_of_damage_per_gold:
    plt.barh(unit_name, value, color=town_colors[town_name])
else:
    plt.xlabel('Avarage damage per gold for basic growth')
    plt.show()
'''