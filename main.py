import pandas as pd
import matplotlib.pyplot as plt
import os


#paths to dictioneries
here = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(here, 'data')
units_data_path = os.path.join(data_path, 'units')
towns_data_path = os.path.join(units_data_path, 'towns')


town_colors = {
    'castle': 'crimson',
    'rampart': 'royalblue',
    'tower': 'tan',
    'inferno': 'limegreen',
    'necropolis': 'orange',
    'dungeon': 'purple',
    'stronghold': 'turquoise',
    'fortress': 'hotpink',
    'conflux': 'yellow',
    'cove': 'slategray'}


town_noup_gold_cost = {
    'castle': 21680,
    'rampart': 19220,
    'tower': 20380,
    'inferno': 20500,
    'necropolis': 20780,
    'dungeon': 21130,
    'stronghold': 17420,
    'fortress': 20350,
    'conflux': 24350,
    'cove': 21315}

town_up_gold_cost = {
    'castle': 29580,
    'rampart': 24920,
    'tower': 31120,
    'inferno': 28090,
    'necropolis': 26920,
    'dungeon': 27205,
    'stronghold': 24530,
    'fortress': 26660,
    'conflux': 31100,
    'cove': 30075
}

#units as dataframes
towns_noup = {}
towns_up = {}

for filename in os.listdir(towns_data_path):
    split = filename.split('_')
    if 'no' in split[1]:
        towns_noup.update({split[0]: pd.read_csv(os.path.join(towns_data_path, filename))})
    else:
        towns_up.update({split[0]: pd.read_csv(os.path.join(towns_data_path, filename))})

neutral_units = pd.read_csv(os.path.join(units_data_path, 'neutral.txt'))

def check(town):
    for i in range(len(town)):
        current = town.iloc[i]

        if current['ammo']>0:
            print(f'{current["name"]} shoot')

        if current['lux_cost']>0:
            print(f'{current["name"]} cost lux')

        if current['max_growth'] > current['growth']*2:
            print(f'{current["name"]} have horde building')
        if "enemy retaliation" in current['special']:
            print(f'{current["name"]} block retaliation')


