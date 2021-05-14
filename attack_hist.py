import matplotlib.pyplot as plt
from main import units

attack_of_all_units = []
attribute = 'attack'
for category_of_units in units:
    for town in category_of_units.values():
        for i in range(len(town)):
            attack_of_all_units.append(town.iloc[i][attribute])
plt.hist(attack_of_all_units, bins=100)
plt.show()