from Skill import Skill

### 普攻
Uni_attack = Skill(name='普通攻击', definition='normal', type='instant',
                   effects_param=[{'effect_type': 'atk_dmg', 'dmg_coef': 1.0, 'target_area': 'single'}])

### 技能
Gem_skill = Skill(name='杰玛技能', definition='active', type='instant',
                  effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 2.0, 'max_targets': 3,
                                  'target_area': 'single'}])

Nitro_skill = Skill(name='奈乔技能', definition='active', type='instant',
                    effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 5, 'target_area': 'single'},
                                   {'effect_type': 'skill_dmg', 'dmg_coef': 5, 'cast_prob_lower_bound': 0.2,
                                    'cast_prob_upper_bound': 0.2, 'target_area': 'single'}])

Don_skill = Skill(name='东技能', definition='active', type='instant',
                  effects_param=[{'effect_type': 'skill_dmg', 'dmg_coef': 3.0, 'max_targets': 1,
                                  'target_area': 'single'},
                                 {'effect_type': 'buff', 'buffs': {'skill_dmg_rcv_inc': -0.2}, 'max_targets': 2,
                                  'cast_prob_lower_bound': 0.3, 'cast_prob_upper_bound': 0.6, 'duration': 3,
                                  'target_area': 'single', 'target_type': 'ally'}])

Massager_skill = Skill(name='按摩师技能', definition='active', type='instant',
                       effects_param=[
                           {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 1, 'target_area': 'single'},
                           {'effect_type': 'buff', 'buffs': {'defense_multi': 0.2}, 'max_targets': 1,
                            'target_type': 'self'}, ])

GoldenNose_skill = Skill(name='金鼻子技能', definition='active', type='instant',
                         effects_param=[
                             {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 1, 'target_area': 'single'},
                             {'effect_type': 'buff', 'buffs': {'rage_increase_add': 5}, 'max_targets': 2,
                              'target_type': 'ally'}, ])

Susie_skill = Skill(name='苏茜技能', definition='active', type='instant',
                    effects_param=[
                        {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'single'},
                        {'effect_type': 'buff', 'buffs': {'atk_dmg_deal_inc': -0.2}, 'max_targets': 2,
                         'target_type': 'enemy'}, ])

FemaleDoctor_skill = Skill(name='女医生技能', definition='active', type='instant',
                           effects_param=[
                               {'effect_type': 'heal', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'single',
                                'target_type': 'ally'}, ])

Artist_skill = Skill(name='艺术家技能', definition='active', type='instant',
                     effects_param=[
                         {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'single'},
                         {'effect_type': 'buff', 'buffs': {'continuous_atk': 1}, 'max_targets': 1,
                          'target_type': 'self'}, ])

Judge_skill = Skill(name='审判长技能', definition='active', type='instant',
                    effects_param=[
                        {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'}])

Jaden_skill = Skill(name='杰登技能', definition='active', type='instant',
                    effects_param=[
                        {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'multiple'}])

Singer_skill = Skill(name='歌手技能', definition='active', type='instant',
                     effects_param=[
                         {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
                         {'effect_type': 'buff', 'buffs': {'dmg_rcv_inc': 0.2}, 'max_targets': 3,
                          'target_type': 'ally'}, ])

Gilbert_skill = Skill(name='吉尔伯特技能', definition='active', type='instant',
                      effects_param=[
                          {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
                          {'effect_type': 'buff', 'buffs': {'chase_atk': 1}, 'max_targets': 1,
                           'target_type': 'self'}, ])

Egirl_skill = Skill(name='E-girl技能', definition='active', type='instant',
                    effects_param=[
                        {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 1, 'target_area': 'single'},
                        {'effect_type': 'buff', 'buffs': {'atk_multi': 0.2}, 'max_targets': 1,
                         'target_type': 'self'}, ])

Watt_skill = Skill(name='华特技能', definition='active', type='instant',
                   effects_param=[
                       {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 2, 'target_area': 'single'},
                       {'effect_type': 'buff', 'buffs': {'reverse_atk': 1}, 'max_targets': 1,
                        'target_type': 'self'}, ])

Strongman_skill = Skill(name='硬汉技能', definition='active', type='instant',
                        effects_param=[
                            {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
                            {'effect_type': 'buff', 'buffs': {'teammate_guard': 0.2}, 'max_targets': 2,
                             'target_type': 'ally'}, ])

Nancy_skill = Skill(name='南希技能', definition='active', type='instant',
                    effects_param=[
                        {'effect_type': 'skill_dmg', 'dmg_coef': 1.0, 'max_targets': 3, 'target_area': 'single'},
                        {'effect_type': 'buff', 'buffs': {'atk_dmg_deal_inc': 0.2}, 'max_targets': 3, 'duration': 3,
                         'target_type': 'enemy'}, ])
