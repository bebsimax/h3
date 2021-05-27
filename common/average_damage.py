def av_dmg(damage_min, damage_max, attack, special, defense=0):
    ADD = attack - defense
    if "Death blow" in special:
        damage_min = 1.2 * damage_min
    if ADD >= 0:
        d_min = damage_min * (1 + 0.05*ADD)
        d_max = damage_max * (1 + 0.05*ADD)
    else:
        d_min = damage_min * (1 - 0.025*ADD)
        d_max = damage_max * (1 - 0.025*ADD)
    avg = (d_min+d_max)/2
    if "twice" in special or "Ferocity" in special:
        return avg*2
    else:
        return avg