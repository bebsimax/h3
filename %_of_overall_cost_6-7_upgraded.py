from main import towns_up, town_colors, town_up_gold_cost
from operator import itemgetter
import matplotlib.pyplot as plt

to_plot=[]
for town_name, town in towns_up.items():
    cost = 0
    for tier in range(5,7):
        cost += town.iloc[tier]['gold_cost'] * town.iloc[tier]['max_growth']
    else:
        town_overall_cost = town_up_gold_cost[town_name]
        town_color = town_colors[town_name]
        to_plot.append([town_name, cost/town_overall_cost*100, town_color])
else:
    for name, value, color in sorted(to_plot, key=itemgetter(1), reverse=True):
        plt.bar(name, value, color=color)

plt.title("gold cost of units tier 6-7 / gold cost of all units")
plt.ylabel("%")
plt.show()

