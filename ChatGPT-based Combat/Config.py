from Skill import Skill

Uni_attack = Skill(name='Attack', definition='normal', type='instant', damage_coefficient=1.0, target_area='single')

Gem_skill = Skill(name='Gem_skill', definition='active', type='instant', damage_coefficient=2.0, target_area='single',
                  max_targets=2)

Nitro_skill = Skill(name='Nitro_skill', definition='active', type='instant', target_area='single', max_targets=1,
                    target_type='enemy', target_select='random', damage_coefficient=2.0)

Don_skill = Skill(name='Don_skill', definition='active', type='instant', target_area='single', target_select='random',
                  max_targets=1, target_type='enemy', damage_coefficient=1.5)

def_doef = 600.0
