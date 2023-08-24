from Skill import Skill
from ExcelConfig import Hero

Uni_attack = Skill(name='Attack', definition='normal', type='instant',
                   effects_param=[{'effect_type': 'atk_dmg', 'dmg_coef': 1.0, 'target_area': 'single'}])

Gem_skill = Skill(name='Gem_skill', definition='active', type='instant',
                  effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 2.0, 'max_targets': 3,
                                  'target_area': 'single'}])

Nitro_skill = Skill(name='Nitro_skill', definition='active', type='instant',
                    effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 5, 'target_area': 'single'},
                                   {'effect_type': 'skill_dmg', 'dmg_coef': 5, 'cast_prob_lower_bound': 0.2,
                                    'cast_prob_upper_bound': 0.2, 'target_area': 'single'}])

Don_skill = Skill(name='Don_skill', definition='active', type='instant',
                  effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 3.0, 'max_targets': 1,
                                  'target_area': 'single'},
                                 {'effect_type': 'buff', 'buffs': {'skill_dmg_rcv_inc': -0.5}, 'max_targets': 2,
                                  'cast_prob_lower_bound': 0.3, 'cast_prob_upper_bound': 0.6, 'duration': 3,
                                  'target_area': 'single', 'target_type': 'ally'}])

# Massager = Skill(name='Massager_skill', definition='active', type='instant')

def_coef = [60, 68, 76, 84, 92, 100, 108, 116, 124, 132, 140, 148, 156, 164, 172, 180, 188, 196, 204, 212, 224, 236,
            248, 260, 272, 284, 296, 308, 320, 332, 344, 356, 368, 380, 392, 404, 416, 428, 440, 452]

# blue_hero_standard_atk = [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 56, 59, 62,
#                           65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113]
# purple_hero_standard_atk = [24, 26, 28, 30, 33, 35, 37, 40, 42, 44, 47, 49, 52, 54, 57, 60, 62, 65, 67, 70, 74, 78, 82,
#                             86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134, 138, 142, 146, 150]
# orange_hero_standard_atk = [33, 35, 38, 41, 45, 48, 51, 55, 58, 61, 65, 68, 71, 75, 78, 81, 85, 89, 92, 95, 101, 106,
#                             111, 117, 122, 127, 133, 138, 144, 149, 154, 160, 165, 171, 176, 181, 187, 192, 198, 203]

blue_hero_standard_atk, purple_hero_standard_atk, orange_hero_standard_atk, \
    blue_hero_standard_def, purple_hero_standard_def, orange_hero_standard_def, \
    blue_hero_standard_hp, purple_hero_standard_hp, orange_hero_standard_hp = Hero.fetch_hero_attr()

attr_offset = {'atk': 1, 'def': 1, 'hp': 25.0 / 3}

hero_attr_offset = Hero.fetch_hero_offset()
