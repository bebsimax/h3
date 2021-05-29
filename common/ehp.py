
def e_hp(row, attack=0):
    hp = row["health"]
    ADD = attack - row["defense"]
    if ADD >= 0:
        ehp = hp - (hp * 0.05 * ADD)
    else:
        ehp = hp + (hp * 0.025 * -ADD)
    return ehp