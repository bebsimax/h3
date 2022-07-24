from main import units, town_colors, legend_elements, chart_data_path
from common import average_damage
import pandas as pd
import matplotlib.pyplot as plt
import os

set_damage = 500
title = f'number of maximum growths and gold needed to reach {set_damage} damage'
chart_name = title
states = ['upgraded', 'neutral']


u = units.query(f'state == "{states[0]}" or state == "{states[1]}"')

u = u.assign(avg_dmg=u.apply(average_damage.avg_dmg, axis=1))
u["growths"] = (set_damage / u.avg_dmg / u.max_growth).round(0)
u["gold_req"] = u.growths * u.gold_cost / 1000


units_to_chart = u[["name", "fraction", "growths", "gold_req"]]
w = 0.6
chart = units_to_chart.sort_values('growths', ascending=True).plot(x=0, kind="barh",
                                                                   stacked=True,
                                                                   figsize=(18, 10),
                                                                   width=w,
                                                                   fontsize=6,
                                                                   ylabel="growths, gold in thousands",
                                                                   xticks=range(0, int(max(u["gold_req"]) + max(u["growths"])), 2),
                                                                   title=title)
fig = chart.get_figure()
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))


plt.show()
