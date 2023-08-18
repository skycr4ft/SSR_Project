import random
from Skill import Skill
import Config


class Character:
    def __init__(self, name, attack, defense, max_hp, curr_hp, crit, crit_resistance, crit_damage,
                 crit_reduction, effect_hit, effect_resistance, skills, rage_increase):

        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_hp = max_hp
        self.curr_hp = curr_hp
        self.crit = crit
        self.crit_resistance = crit_resistance
        self.crit_damage = crit_damage
        self.crit_reduction = crit_reduction
        self.effect_hit = effect_hit
        self.effect_resistance = effect_resistance
        self.rage_increase = rage_increase

        self.skills = skills  # Convert dict to Skill objects
        self.def_coef = Config.def_coef
        self.squad = None

    def is_alive(self):
        return self.curr_hp > 0

    def calculate_crit_rate(self, crit_coef):
        return (self.crit - self.crit_resistance) / crit_coef

    def take_action(self, is_rage_skill_phase):
        if is_rage_skill_phase:
            # Use rage skill
            return next((skill for skill in self.skills if skill.definition == 'active'), None)
        else:
            # Use normal skill
            return next((skill for skill in self.skills if skill.definition == 'normal'), None)

    def set_def_coef(self, def_coef):
        # 攻击方的防御系数
        self.def_coef = def_coef

    # def select_targets(self, squads, skill):
    #     if skill.target_type == 'enemy':
    #         target_squads = [squad for squad in squads if squad != self.squad]
    #     elif skill.target_type == 'ally':
    #         target_squads = [self.squad]
    #     elif skill.target_type == 'self':
    #         target_squads = [self.squad]
    #
    #     if skill.target_area == 'single':
    #         target_list = []
    #         for squad in target_squads:
    #             target_list.extend(squad.members)
    #         if skill.target_type == 'enemy':
    #             # Select a target from the enemy squad based on the target_select attribute of the skill
    #             if skill.target_select == 'weakest':
    #                 target = min(target_list, key=lambda character: character.hp)
    #             elif skill.target_select == 'strongest':
    #                 target = max(target_list, key=lambda character: character.hp)
    #             else:  # random selection
    #                 target = random.choice(target_list)
    #         elif skill.target_type == 'ally':
    #             # Select a target from the ally squad, excluding the attacker
    #             target_list.remove(self)
    #             target = random.choice(target_list)
    #         elif skill.target_type == 'self':
    #             target = self
    #         return [target]
    #     elif skill.target_area == 'multiple':
    #         target_squads = random.sample(target_squads, min(skill.max_targets, len(target_squads)))
    #         target_list = []
    #         for squad in target_squads:
    #             for target in squad.members:
    #                 if target.is_alive():  # only attack alive characters
    #                     target_list.append(target)
    #         return target_list

    # def attack(self, squads, skill):
    #     total_damage = 0
    #     targets = self.select_targets(squads, skill)
    #     for target in targets:
    #         damage = self.calculate_damage(target, skill_coef=skill.damage_coefficient,
    #                                        skill_base_damage=skill.base_damage)
    #         target.take_damage(damage)
    #         total_damage += damage

    def cast_skill(self, squads, skill):
        total_damage = 0
        target_list = []
        for effect in skill.effects:
            is_cast, damage, targets = effect.run(self, squads)
            total_damage += damage
            target_list.extend(targets)
        return total_damage, target_list

    def calc_attributes(self):
        return 0

    def calc_damage(self, defender, effect_coef, effect_base_damage):
        crit_rate = self.calculate_crit_rate(1.0)
        damage = effect_coef * self.attack * (1 - defender.defense / (defender.defense + self.def_coef)) \
                 + effect_base_damage
        if crit_rate > random.random():  # Check if the attack is a critical hit
            print('Critical!')
            damage *= (1.0 + self.crit_damage)
        return damage

    def take_damage(self, damage):
        self.curr_hp -= damage
        if self.curr_hp <= 0:
            print(f'{self.squad.name}-{self.name} died!')

    def calc_heal(self, effect_coef, effect_base_damage):
        return effect_coef * self.attack + effect_base_damage

    def take_heal(self, heal):
        self.curr_hp = min(self.curr_hp + heal, self.max_hp)
