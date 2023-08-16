import Consts
from Hero import Hero
import xlwings as xw

if __name__ == '__main__':
    Hero_A = Hero(Name='A', Quality='Blue', Atk=15, Def=15, HP=375)
    Hero_B = Hero(Name='B', Quality='Blue', Atk=15, Def=15, HP=375)
    dmg, dmg_rst_rate, C = dmg(Hero_A, Hero_B)
    print("Combat turns: ", Hero_B.Attr.HP / dmg)
    print("Dmg_Rst_Rate: ", dmg_rst_rate)
    print("Def_factor: ", C)
