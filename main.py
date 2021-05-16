import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches
pd.options.mode.chained_assignment = None

#paths to dictioneries
here = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(here, 'data')
units_data_path = os.path.join(data_path, 'units')
towns_data_path = os.path.join(units_data_path, 'towns')
chart_data_path = os.path.join(here, 'charts')


town_colors = {
    'castle': 'crimson',
    'conflux': 'gold',
    'cove': 'slategray',
    'dungeon': 'purple',
    'fortress': 'hotpink',
    'inferno': 'limegreen',
    'necropolis': 'orange',
    'rampart': 'royalblue',
    'stronghold': 'turquoise',
    'tower': 'tan',
    'neutral': 'darkgoldenrod'}

fraction_name_list = list(town_colors.keys())

legend_elements = []

for name, color in town_colors.items():
    legend_elements.append(mpatches.Patch(color=color, label=name))


units = pd.read_csv(os.path.join(units_data_path, 'all_units.txt'))


