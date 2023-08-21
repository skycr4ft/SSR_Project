from Skill import Skill

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
                                 {'effect_type': 'buff', 'buffs': {'skill_dmg_rcv_inc': -0.2}, 'max_targets': 2,
                                  'cast_prob_lower_bound': 0.3, 'cast_prob_upper_bound': 0.6, 'duration': 3,
                                  'target_area': 'single', 'target_type': 'ally'}])

# Massager = Skill(name='Massager_skill', definition='active', type='instant')

def_coef = [60, 68, 76, 84, 92, 100, 108, 116, 124, 132, 140, 148, 156, 164, 172, 180, 188, 196, 204, 212, 224, 236,
            248, 260, 272, 284, 296, 308, 320, 332, 344, 356, 368, 380, 392, 404, 416, 428, 440, 452]

