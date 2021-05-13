from main import towns_noup, towns_up, town_colors
from operator import itemgetter
import matplotlib.pyplot as plt


def max_gold_cost(town):
    return town.gold_cost.dot(town.max_growth)

towns_noup_gold = []
towns_up_gold = []

plt.subplot(211)
plt.title("Cost of weekly growth of unupgraded units")
plt.ylabel('Gold')
plt.ylim(15000,25000)
for key, value in towns_noup.items():
    temp_list = [key, max_gold_cost(value)]
    towns_noup_gold.append(temp_list)
else:
    sorted_noup_towns = sorted(towns_noup_gold, key=itemgetter(1), reverse=True)

for key, value in towns_up.items():
    temp_list = [key, max_gold_cost(value)]
    towns_up_gold.append(temp_list)
else:
    sorted_up_towns = sorted(towns_up_gold, key=itemgetter(1), reverse=True)
print(towns_noup_gold)
print(towns_up_gold)

for zipped_town_gold in sorted_noup_towns:
    town_name = zipped_town_gold[0]
    town_name = town_name.split('_')
    town_name = town_name[0]
    town_color = town_colors[town_name]
    town_units_cost = zipped_town_gold[1]
    plt.bar(town_name, town_units_cost, color=town_color)

plt.subplot(212)
plt.title("Cost of weekly growth of upgraded units")
plt.ylabel('Gold')
plt.ylim(20000, 34000)
for zipped_town_gold in sorted_up_towns:
    town_name = zipped_town_gold[0]
    town_name = town_name.split('_')
    town_name = town_name[0]
    town_color = town_colors[town_name]
    town_units_cost = zipped_town_gold[1]
    plt.bar(town_name, town_units_cost, color=town_color)

plt.show()