from Combat.Skill import Skill

### 标准普攻
# version: 1
Uni_attack = Skill(name='普通攻击', definition='normal', type='instant',
                   effects_param=[{'effect_type': 'atk_dmg', 'dmg_coef': 1.0, 'target_area': 'single'}])

### 技能数值配置
Gem_skills = [Skill(name='杰玛技能', definition='active', type='instant',
                    effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 1.2, 'max_targets': 3,
                                    'target_area': 'single'}]),
              Uni_attack]

# version: 1
Nitro_skills = [Skill(name='奈乔技能', definition='active', type='instant',
                      effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 2.4, 'target_area': 'single'},
                                     {'effect_type': 'skill_dmg', 'dmg_coef': 2.4, 'cast_prob_lower_bound': 0.5,
                                      'cast_prob_upper_bound': 0.5, 'target_area': 'single'}]),
                Uni_attack]

# version: 1
Don_skills = [Skill(name='东技能', definition='active', type='instant',
                    effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 1.2, 'max_targets': 1,
                                    'target_area': 'single'},
                                   {'effect_type': 'buff', 'buffs': {'skill_dmg_rcv_inc': -0.12}, 'max_targets': 2,
                                    'cast_prob_lower_bound': 0.3, 'cast_prob_upper_bound': 0.6, 'duration': 3,
                                    'target_area': 'single', 'target_type': 'ally'}]),
              Uni_attack]

# version: 1
Massager_skills = [Skill(name='按摩师技能', definition='active', type='instant',
                         effects_param=[
                             {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 1, 'target_area': 'single'},
                             {'effect_type': 'buff', 'buffs': {'defense_multi': 3.3}, 'max_targets': 1,
                              'target_type': 'self', 'duration': 3}, ]),
                   Uni_attack]

# version: 1
GoldenNose_skills = [Skill(name='金鼻子技能', definition='active', type='instant',
                           effects_param=[
                               {'effect_type': 'skill_dmg', 'dmg_coef': 3.0, 'max_targets': 1, 'target_area': 'single'},
                               {'effect_type': 'buff', 'buffs': {'rage_increase_add': 5}, 'max_targets': 2,
                                'target_type': 'ally', 'duration': 3}, ]),
                     Uni_attack]

# version: 1
Susie_skills = [Skill(name='苏茜技能', definition='active', type='instant',
                      effects_param=[
                          {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'single'},
                          {'effect_type': 'buff', 'buffs': {'atk_dmg_deal_inc': -0.6}, 'max_targets': 2,
                           'target_type': 'enemy', 'duration': 5}, ]),
                Uni_attack]

# # version: 1
# FemaleDoctor_skill = Skill(name='女医生技能', definition='active', type='instant',
#                            effects_param=[
#                                {'effect_type': 'heal', 'heal_coef': 2.4, 'max_targets': 2, 'target_area': 'single',
#                                 'target_type': 'ally'}, ])
#
# # version: 1
# Artist_skill = Skill(name='艺术家技能', definition='active', type='instant',
#                      effects_param=[
#                          {'effect_type': 'skill_dmg', 'dmg_coef': 2.0, 'max_targets': 2, 'target_area': 'single'},
#                          {'effect_type': 'buff', 'buffs': {'continuous_atk': 1}, 'max_targets': 1,
#                           'target_type': 'self', 'duration': 3}, ])
#
# # version: 1
# Judge_skill = Skill(name='审判长技能', definition='active', type='instant',
#                     effects_param=[
#                         {'effect_type': 'skill_dmg', 'dmg_coef': 2.0, 'max_targets': 3, 'target_area': 'single'}])
#
# # version: 1
# Jaden_skill = Skill(name='杰登技能', definition='active', type='instant',
#                     effects_param=[
#                         {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'multiple'}])
#
# # version: 1
# Singer_skill = Skill(name='歌手技能', definition='active', type='instant',
#                      effects_param=[
#                          {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
#                          {'effect_type': 'buff', 'buffs': {'dmg_rcv_inc': 0.22}, 'max_targets': 3,
#                           'target_type': 'enemy', 'duration': 3}, ])
#
# # version: 1
# Gilbert_skill = Skill(name='吉尔伯特技能', definition='active', type='instant',
#                       effects_param=[
#                           {'effect_type': 'skill_dmg', 'dmg_coef': 1.5, 'max_targets': 3, 'target_area': 'single'},
#                           {'effect_type': 'buff', 'buffs': {'chase_atk': 1}, 'max_targets': 1,
#                            'target_type': 'self', 'duration': 3}, ])
#
# # version: 1
# Egirl_skill = Skill(name='E-girl技能', definition='active', type='instant',
#                     effects_param=[
#                         {'effect_type': 'skill_dmg', 'dmg_coef': 4.0, 'max_targets': 1, 'target_area': 'single',
#                          'target_select': 'weakest'},
#                         {'effect_type': 'buff', 'buffs': {'atk_multi': 0.25}, 'max_targets': 1,
#                          'target_type': 'self'}, ])
#
# # version: 1
# Watt_skill = Skill(name='华特技能', definition='active', type='instant',
#                    effects_param=[
#                        {'effect_type': 'skill_dmg', 'dmg_coef': 2.0, 'max_targets': 2, 'target_area': 'single'},
#                        {'effect_type': 'buff', 'buffs': {'reverse_atk': 1}, 'max_targets': 1,
#                         'target_type': 'self', 'duration': 3}, ])
#
# # version: 1
# Strongman_skill = Skill(name='硬汉技能', definition='active', type='instant',
#                         effects_param=[
#                             {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
#                             {'effect_type': 'buff', 'buffs': {'teammate_guard': 1}, 'max_targets': 2,
#                              'target_type': 'ally'}, ])
#
# # version: 1
# Nancy_skill = Skill(name='南希技能', definition='active', type='instant',
#                     effects_param=[
#                         {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
#                         {'effect_type': 'buffs', 'buffs': {'atk_dmg_deal_inc': 0.34}, 'max_targets': 3, 'duration': 3,
#                          'target_type': 'enemy'}, ])
