import random
from Skill import Skill
import Consts
from Effect import EffectTracker


class Character:
    def __init__(self, name, level, atk_base, def_base, max_hp_base, crit_base,
                 crit_res_base,
                 eff_hit_base, eff_res_base, skills,
                 rage_increase_base=18, crit_damage_base=0.5, crit_reduction_base=0):

        self.name = name
        self.level = level

        # 读取属性基础值
        self.attack_base = atk_base
        self.defense_base = def_base
        self.max_hp_base = max_hp_base
        self.curr_hp_base = max_hp_base
        self.crit_base = crit_base
        self.crit_res_base = crit_res_base
        self.crit_damage_base = crit_damage_base
        self.crit_reduction_base = crit_reduction_base
        self.eff_hit_base = eff_hit_base
        self.eff_res_base = eff_res_base
        self.rage_increase_base = rage_increase_base

        self.skills = skills  # Convert list to Skill objects
        self.def_coef = Consts.def_coef[level - 1]
        self.squad = None
        self.base_attrs = ['attack', 'defense', 'max_hp', 'crit', 'crit_res', 'crit_damage',
                           'crit_reduction', 'eff_hit', 'eff_res', 'rage_increase']
        # 配置进阶属性
        self.promoted_attrs = ['atk_dmg_rcv_inc', 'skill_dmg_rcv_inc', 'atk_dmg_deal_inc', 'skill_dmg_deal_inc',
                               'dmg_rcv_inc', 'dmg_deal_inc', 'heal_rcv_inc', 'heal_deal_inc']

        self.effect_tracker = EffectTracker()

        # 初始化属性值
        self.attack = self.attack_base
        self.defense = self.defense_base
        self.max_hp = self.max_hp_base
        self.curr_hp = self.curr_hp_base
        self.crit = self.crit_base
        self.crit_res = self.crit_res_base
        self.crit_damage = self.crit_damage_base
        self.crit_reduction = self.crit_reduction_base
        self.eff_hit = self.eff_hit_base
        self.eff_res = self.eff_res_base
        self.rage_increase = self.rage_increase_base

        # 初始化进阶属性
        self.atk_dmg_rcv_inc = 0.0
        self.skill_dmg_rcv_inc = 0.0
        self.atk_dmg_deal_inc = 0.0
        self.skill_dmg_deal_inc = 0.0
        self.dmg_rcv_inc = 0.0
        self.dmg_deal_inc = 0.0
        self.heal_rcv_inc = 0.0
        self.heal_deal_inc = 0.0

        # 记录造成的伤害
        self.skill_dmg_dealt = 0.0
        self.atk_dmg_dealt = 0.0

    def is_alive(self):
        return self.curr_hp > 0

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

    # 选择技能效果的目标
    def select_targets(self, squads, skill):
        is_cast_list = []
        target_list = []
        for effect in skill.effects:
            is_cast, targets = effect.run(self, squads)
            target_list.append(targets)
            is_cast_list.append(is_cast)
        return is_cast_list, target_list

    # 结算技能效果
    def cast_skill(self, target_list, skill):
        total_damage = 0
        for (effect, targets) in zip(skill.effects, target_list):
            effect.apply(self, targets)
        # return total_damage

    def take_dmg(self, damage):
        self.curr_hp -= damage
        # if self.curr_hp <= 0:
        #     print(f'{self.squad.name}-{self.name} died!')

    def calc_heal(self, effect_coef, effect_base_dmg):
        return effect_coef * self.attack + effect_base_dmg

    def take_heal(self, heal):
        self.curr_hp = min(self.curr_hp + heal, self.max_hp)

    def update(self):
        # 更新效果的状态
        self.effect_tracker.tick(self)

        # 计算角色的属性
        bonus = self.gather_bonus()
        self.calc_attributes(bonus)

    def gather_bonus(self):
        bonus = {}
        for buff_effect in self.effect_tracker.buff_effects:
            for buff in buff_effect.buffs:
                bonus[buff] = buff_effect.buffs[buff] if buff not in bonus else bonus[buff] + buff_effect.buffs[buff]
        return bonus

    def calc_attributes(self, bonus):
        # 计算所有属性
        for attr in self.base_attrs:
            setattr(self, attr, getattr(self, attr + '_base') *
                    (1.0 + bonus[attr + '_multi'] if attr + '_multi' in bonus else 1.0) +
                    (bonus[attr + '_add'] if attr + '_add' in bonus else 0))

        for attr in self.promoted_attrs:
            setattr(self, attr, getattr(self, attr) + bonus[attr] if attr in bonus else getattr(self, attr))
