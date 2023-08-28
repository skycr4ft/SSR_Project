import Consts
from Hero import Hero


def calc_dmg(skill_atk, hero_atk, hero_def) -> (float, float):
    for i in range(1, 100):
        dmg_base = float(hero_atk.Attr.Atk * (1 - float(hero_def.Attr.Def) / (hero_def.Attr.Def + i)))

        dmg_final = dmg_base
        turn = hero_def.Attr.HP / dmg_final
        if abs(turn - 30) < 2:
            dmg_rst_rate = hero_def.Attr.Def / (hero_def.Attr.Def + i)
            C = i
            break
    return dmg_final, dmg_rst_rate, C





