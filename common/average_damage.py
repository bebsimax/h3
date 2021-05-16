def av_dmg(damage_min, damage_max, attack, defense=0):
    ADD = attack - defense
    if ADD >= 0:
        d_min = damage_min * (1 + 0.05*ADD)
        d_max = damage_max * (1 + 0.05*ADD)
    else:
        d_min = damage_min * (1 - 0.025*ADD)
        d_max = damage_max * (1 - 0.025*ADD)
    return (d_min+d_max)/2