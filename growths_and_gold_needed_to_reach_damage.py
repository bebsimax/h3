from main import units, town_colors, legend_elements, chart_data_path
from common import average_damage
import pandas as pd
import matplotlib.pyplot as plt
import os

set_damage = 500
title = f'number of maximum growths and gold needed to reach {set_damage} damage'
chart_name = title
states = ['upgraded', 'neutral']


units_up_and_neu = units.query(f'state == "{states[0]}" or state == "{states[1]}"')

units_up_and_neu = units_up_and_neu.assign(avg_dmg=units_up_and_neu.apply(average_damage.avg_dmg_series, axis=1))
units_up_and_neu["growths"] = (set_damage / units_up_and_neu.avg_dmg / units_up_and_neu.max_growth).round(0)
units_up_and_neu["gold_req"] = units_up_and_neu.growths * units_up_and_neu.gold_cost / 1000


units_to_chart = units_up_and_neu[["name", "fraction", "growths", "gold_req"]]
w = 0.6
chart = units_to_chart.sort_values('growths', ascending=True).plot(x=0, kind="barh",
                                                  stacked=True,
                                                  figsize=(18, 10),
                                                  width=w,
                                                  fontsize=6,
                                                  ylabel="growths, gold in thousands",
                                                  xticks=range(0, int(max(units_up_and_neu["gold_req"])+max(units_up_and_neu["growths"])), 2),
                                                  title=title)
fig = chart.get_figure()
fig.savefig(os.path.join(chart_data_path, chart_name + '.png'))


plt.show()
