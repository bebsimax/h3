import re
global ATTACK
ATTACK = 0

def e_hp(row):
    special = row["special"]
    hp = row["health"]
    attack = ATTACK

    if "enemy's attack skill" in special:
        numbers = re.findall(r'\d+', special)
        attack = attack - int(numbers[0])/100 * attack

    ADD = attack - row["defense"]
     # For each extra point of Defense skill over attackers's Attack skill, the received damage gets reduced by 2.5 % (up to 70 %, which is 28 points in difference).
    if ADD >= 0:
        ADD = min(ADD, 60)
        ehp = 1 - (0.05 * ADD)
    else:
        ADD = ADD * -1
        ADD = min(ADD, 28)
        ehp = 1 + (0.025 * ADD)
    return hp * ehp

def e_hp_coef(row):
    special = row["special"]
    attack = ATTACK

    if "enemy's attack skill" in special:
        numbers = re.findall(r'\d+', special)
        attack = attack - int(numbers[0])/100 * attack

    ADD = attack - row["defense"]
     # For each extra point of Defense skill over attackers's Attack skill, the received damage gets reduced by 2.5 % (up to 70 %, which is 28 points in difference).
    if ADD >= 0:
        ADD = min(ADD, 60)
        ehp = 1 + (0.05 * ADD)
    else:
        ADD = ADD * -1
        ADD = min(ADD, 28)
        ehp = 1 - (0.025 * ADD)
    return ehp