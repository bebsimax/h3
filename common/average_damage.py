def avg_dmg(row, defense=0):
    damage_min = row["damage_min"]
    damage_max = row["damage_max"]
    attack = row["attack"]
    special = row["special"]

    ADD = attack - defense

    if "Death blow" in special:
        damage_min = 1.2 * damage_min

    if ADD >= 0:
        d_min = damage_min * (1 + 0.05 * ADD)
        d_max = damage_max * (1 + 0.05 * ADD)
    else:
        d_min = damage_min * (1 - 0.025 * ADD)
        d_max = damage_max * (1 - 0.025 * ADD)

    avg = (d_min + d_max) / 2

    if "twice" in special or "Ferocity" in special:
        return avg * 2
    else:
        return avg