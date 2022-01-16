import re

def e_hp(row, attack=20):
    hp = row["health"]
    special = row["special"]

    if "Ignores 30% of enemy's attack skill" in special:
        damage_min = 1.2 * damage_min

    ADD = attack - row["defense"]
     # For each extra point of Defense skill over attackers's Attack skill, the received damage gets reduced by 2.5 % (up to 70 %, which is 28 points in difference).
    if ADD >= 0:
        ADD = min(ADD, 60)
        ehp = hp - (hp * 0.05 * ADD)
    else:
        ADD = ADD * -1
        ADD = min(ADD, 28)
        ehp = hp + (hp * 0.025 * ADD)
    return ehp