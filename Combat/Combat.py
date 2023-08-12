import Consts
from Hero import Hero
import xlwings as xw


def dmg(hero_atk, hero_def) -> (float, float):
    for i in range(1, 100):
        dmg_base = float(hero_atk.Attr.Atk * (1 - float(hero_def.Attr.Def) / (hero_def.Attr.Def + i)))

        dmg_final = dmg_base
        turn = hero_def.Attr.HP / dmg_final
        if abs(turn - 60) < 2:
            dmg_rst_rate = hero_def.Attr.Def / (hero_def.Attr.Def + i)
            C = i
            break
    return dmg_final, dmg_rst_rate, C


if __name__ == '__main__':
    Hero_A = Hero(Name='A', Quality='Blue', Atk=15, Def=15, HP=375)
    Hero_B = Hero(Name='B', Quality='Blue', Atk=15, Def=15, HP=375)
    dmg, dmg_rst_rate, C = dmg(Hero_A, Hero_B)
    print("Combat turns: ", Hero_B.Attr.HP / dmg)
    print("Dmg_Rst_Rate: ", dmg_rst_rate)
    print("Def_factor: ", C)
