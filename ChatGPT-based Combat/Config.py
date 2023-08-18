from Skill import Skill
from Effect import DamageEffect

Uni_attack = Skill(name='Attack', definition='normal', type='instant',
                   effects_param=[{'effect_type': 'damage', 'damage_coef': 1.0, 'target_area': 'single'}])

Gem_skill = Skill(name='Gem_skill', definition='active', type='instant',
                  effects_param=[{'effect_type': 'damage', 'damage_coef': 2.6, 'max_targets': 2,
                                  'target_area': 'single'}])

Nitro_skill = Skill(name='Nitro_skill', definition='active', type='instant',
                    effects_param=[{'effect_type': 'damage', 'damage_coef': 3.5, 'target_area': 'single'},
                                   {'effect_type': 'damage', 'damage_coef': 3.5, 'cast_prob_lower_bound': 0.2,
                                    'cast_prob_upper_bound': 0.2, 'target_area': 'single'}])

Don_skill = Skill(name='Don_skill', definition='active', type='instant',
                  effects_param=[{'effect_type': 'damage', 'damage_coef': 3.0, 'max_targets': 1,
                                  'target_area': 'single'}])

def_coef = 222.0
