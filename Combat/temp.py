from Character import Character
from Skill import Skill
from Squad import Squad
from Battle import Battle
import Consts
from ExcelConfig.HeroStats import Hero_Skills, Heroes_qlt, Hero_level
import matplotlib
from ExcelConfig.HeroStats import Numerical, calc_hero_power, get_hero_progression
from ExcelConfig.MonsterStats import Mon_Numerical
import csv
from tqdm import tqdm
from ExcelConfig.HeroStats import get_se_hero_progression


# 计算宠物属性占比
# if __name__ == '__main__':
#     self = Numerical()
#
#     cfgs = get_hero_progression('E:\新建文件夹\战斗\SSR战斗养成数值_7day.xlsx')
#
#     cfg = cfgs[9]
#
#     for a in cfg:
#         hero = a['hero']
#         quality = a['quality']
#         level = a['level']
#         star = a['star']
#         item_qlt = a['item_qlt']
#         item_tier = a['item_tier']
#         item_num = a['item_num']
#         item_boost = a['item_boost']
#         pet_qlt = a['pet_qlt']
#         pet_lvl = a['pet_lvl']
#         pet_star = a['pet_star']
#
#         atk = self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
#               (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
#               item_num * self.item_attr_prop['atk_prop'] / self.attr_weight['atk'] + \
#               self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['atk'] + \
#               self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         pet_atk = self.pet_level_attr[pet_qlt]['slg_atk'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         _def = self.hero_offset[hero]['def'] * self.hero_level_attr[quality]['def'][level - 1] * \
#                (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
#                item_num * self.item_attr_prop['def_prop'] / self.attr_weight['def'] + \
#                self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['def'] + \
#                self.pet_level_attr[pet_qlt]['slg_def'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         pet_def = self.pet_level_attr[pet_qlt]['slg_def'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         hp = self.hero_offset[hero]['hp'] * self.hero_level_attr[quality]['hp'][level - 1] * \
#              (1 + self.hero_star[quality]['base_attr'][star]) + self.item_qlt_power[item_qlt][item_tier] * \
#              item_num * self.item_attr_prop['hp_prop'] / self.attr_weight['hp'] + \
#              self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['hp'] + \
#              self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         pet_hp = self.pet_level_attr[pet_qlt]['slg_hp'][pet_lvl - 1] * (1 + self.pet_rank_attr[max(pet_star - 1, 0)])
#
#         hero_atk = self.hero_offset[hero]['atk'] * self.hero_level_attr[quality]['atk'][level - 1] * \
#         (1 + self.hero_star[quality]['base_attr'][star])
#
#         item_atk = self.item_qlt_power[item_qlt][item_tier] * \
#             item_num * self.item_attr_prop['atk_prop'] / self.attr_weight['atk'] + \
#             self.item_boost_attr[item_boost - 1] * item_num / 3 / self.attr_weight['atk']
#
#
#         print(pet_atk / atk, pet_def / _def, pet_hp / hp)
#
#         print(hero_atk, item_atk, pet_atk, atk)


# if __name__ == '__main__':
#     hero_builder = Numerical()
#
#     cfgs = get_hero_progression('E:\新建文件夹\战斗\SSR战斗养成数值.xlsx')
#
#     cfg = cfgs[7]
#
#     for hero in cfg:
#         char = Character(**hero_builder.pack(hero), skills=Hero_Skills[hero['hero']])
#         print("名称： ", char.name, '血量： ', char.max_hp, '攻击： ', char.attack, '防御： ', char.defense, '暴击： ', char.crit, '暴击抵抗： ', char.crit_res, '暴击伤害： ', char.crit_damage, '暴击减免： ', char.crit_reduction, '效果命中： ', char.eff_hit, '效果抵抗： ', char.eff_res, '怒气增益： ', char.rage_increase)


if __name__ == '__main__':
    res = get_se_hero_progression('E:\新建文件夹\战斗\SSR数值规划3.xlsx')
    for a in res:
        print(a)

