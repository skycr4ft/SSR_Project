import random


class Effect:
    def __init__(self, effect_type, target_area='single', duration=0, cast_prob_lower_bound=100,
                 cast_prob_upper_bound=100,
                 target_select='random', area_shape=None, area_length=0.0, area_width=0.0, area_angle=0.0,
                 distance_limit=0.0, max_targets=1, target_type='enemy'):
        # 效果释放概率下限
        self.cast_prob_lower_bound = cast_prob_lower_bound
        # 效果释放概率上限
        self.cast_prob_upper_bound = cast_prob_upper_bound

        # 效果类型，取值范围为{伤害，治疗，增益，减益} {'damage', 'heal', 'buff', 'debuff'}
        self.effect_type = effect_type
        # 效果目标，取值范围为{单体，群体} {'single', 'multiple'}
        self.target_area = target_area
        # 选择目标的方法 {random, weakest, strongest, self, ally_except_self,}
        self.target_select = target_select
        # 效果目标类型,取值范围为{敌人，友方，自身}
        self.target_type = target_type
        # 效果最大目标数
        self.max_targets = max_targets

        # 效果持续回合数
        self.duration = duration
        # 效果伤害系数
        # self.damage_coef= damage_coef
        # 效果基础伤害值
        # self.base_damage = base_damage

        # 效果范围形状，取值范围为{扇形，矩形，圆形}
        self.area_shape = area_shape
        self.area_length = area_length
        self.area_width = area_width
        self.area_angle = area_angle
        self.distance_limit = distance_limit

    def is_applicable(self, character):
        # Define the condition for the effect to be applicable
        return True

    def tick(self, character):
        # Define what happens when the effect "ticks" (i.e., advances one time step)
        pass

    # 执行效果逻辑
    def run(self, caster, squads):
        raise NotImplementedError

    # 记录日志
    # def log(self, caster, targets, damage):
    #     raise NotImplementedError

    # 计算效果的释放概率
    def calc_cast_prob(self, caster, target) -> float:
        delta = self.cast_prob_upper_bound - self.cast_prob_lower_bound
        cast_prob = self.cast_prob_lower_bound + delta * (caster.eff_hit - target.eff_res)
        cast_prob = min(max(cast_prob, self.cast_prob_lower_bound), self.cast_prob_upper_bound)
        return cast_prob

    def select_targets(self, caster, squads):
        if self.target_type == 'enemy':
            target_squads = [squad for squad in squads if squad.alliance != caster.squad.alliance]
        # elif self.target_type == 'ally':
        #     target_squads = [caster.squad]
        # elif self.target_type == 'self':
        #     target_squads = [caster.squad]
        else:
            target_squads = [caster.squad]

        if self.target_area == 'single':
            target_list = []
            squad = random.choice(target_squads)
            target_list.extend([character for character in squad.characters if character is not None
                                and character.is_alive()])

            if self.target_select == 'self':
                target = [caster]
            elif self.target_select == 'ally_except_self':
                target_list.remove(caster)
                target = random.sample(target_list, min(self.max_targets, len(target_list)))
            elif self.target_select == 'weakest':
                target = [min(target_list, key=lambda caster: caster.curr_hp)]
            elif self.target_select == 'strongest':
                target = [max(target_list, key=lambda caster: caster.curr_hp)]
            else:  # random selection
                target = random.sample(target_list, min(self.max_targets, len(target_list)))
            return target
        elif self.target_area == 'multiple':
            target_squads = random.sample(target_squads, min(self.max_targets, len(target_squads)))
            target_list = []
            for squad in target_squads:
                for target in squad.characters:
                    if target.is_alive():  # only attack alive characters
                        target_list.append(target)
            return target_list


class DamageEffect(Effect):
    def __init__(self, dmg_coef, dmg_base=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dmg_coef = dmg_coef
        self.dmg_base = dmg_base

    def run(self, caster, squads):
        # 选择目标
        targets = self.select_targets(caster, squads)
        return True, targets

    def apply(self, caster, targets):
        # 计算总伤害
        total_damage = 0

        for target in targets:
            # 计算效果释放概率
            cast_prob = self.calc_cast_prob(caster, target)
            # 生成随机数
            rand = random.random()
            if cast_prob < rand:
                return False, total_damage

            total_damage += self.apply_one(caster, target)

            # 判断攻击者是否带有连击效果，并且是否在本次攻击中未触发
            if caster.effect_tracker.is_exist('chain'):
                chain = caster.effect_tracker.get_effect('chain')
                if chain.used:
                    chain.used = False
                    return
                else:
                    chain.used = True
                    total_damage += self.apply_one(caster, target)

            # 打印日志
            # self.log(caster, target, total_damage)

        return True, total_damage

    def apply_one(self, caster, target):
        total_damage = 0
        # 计算伤害
        damage = self.calc_dmg(caster, target, effect_coef=self.dmg_coef, effect_base_dmg=self.dmg_base)
        total_damage += damage
        # 计算反击伤害
        counter_damage = 0.2 * self.calc_dmg(target, caster, effect_coef=1, effect_base_dmg=0)
        # 打印日志
        # self.log(caster, target, damage, self.effect_type)
        # self.log(target, caster, counter_damage, '反击')
        # 造成伤害
        target.take_dmg(damage)
        caster.take_dmg(counter_damage)

        # 判断受击者是否带有反击效果
        if target.effect_tracker.is_exist('counter'):
            counter = target.effect_tracker.get_effect('counter')
            # 计算反击伤害
            counter_damage = self.calc_dmg(target, caster, effect_coef=counter.dmg_coef,
                                           effect_base_dmg=counter.base_dmg)
            # self.log(target, caster, counter_damage, '反击')
            caster.take_dmg(counter_damage)

        # 判断攻击者是否带有追击效果
        if caster.effect_tracker.is_exist('chase'):
            chase = caster.effect_tracker.get_effect('chase')
            # 计算追击伤害
            chase_damage = self.calc_dmg(caster, target, effect_coef=chase.dmg_coef, effect_base_dmg=chase.base_dmg)
            # self.log(caster, target, chase_damage, '追击')
            target.take_dmg(chase_damage)

        return total_damage

    def calc_dmg(self, caster, defender, effect_coef, effect_base_dmg):
        crit_rate = self.calc_crit_rate(caster.crit, defender.crit_res)
        crit_dmg_bonus = 1
        if crit_rate > random.random():  # Check if the attack is a critical hit
            # print('暴击!')
            crit_dmg_bonus += caster.crit_damage
        if self.effect_type == 'skill_dmg':
            damage = (effect_coef * caster.attack * (1 - defender.defense / (defender.defense + caster.def_coef))
                      + effect_base_dmg) * (1 + defender.skill_dmg_rcv_inc) * (1 + caster.skill_dmg_deal_inc) * \
                     (1 + caster.dmg_deal_inc) * (1 + defender.dmg_rcv_inc) * crit_dmg_bonus
            caster.skill_dmg_dealt += damage
        else:
            damage = (effect_coef * caster.attack * (1 - defender.defense / (defender.defense + caster.def_coef))
                      + effect_base_dmg) * (1 + defender.atk_dmg_rcv_inc) * (1 + caster.atk_dmg_deal_inc) * \
                     (1 + caster.dmg_deal_inc) * (1 + defender.dmg_rcv_inc) * crit_dmg_bonus
            caster.atk_dmg_dealt += damage

        return damage

    def calc_crit_rate(self, caster_crit, defender_crit_res):
        from Combat.Consts import CRIT_COEF
        return (caster_crit - defender_crit_res) / CRIT_COEF

    def log(self, caster, target, damage):
        print(
            f'{caster.squad.name}-{caster.name} to {target.squad.name}-{target.name} {damage} {self.effect_type}.')


class HealEffect(Effect):
    def __init__(self, heal_coef, heal_base=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heal_coef = heal_coef
        self.heal_base = heal_base

    def run(self, caster, squads):
        # 选择目标
        targets = self.select_targets(caster, squads)
        return True, targets

    def apply(self, character, targets):
        total_heal = 0

        for target in targets:
            # 计算效果释放概率
            # cast_prob = self.calc_cast_prob(caster, target)
            # # 生成随机数
            # rand = random.random()
            # if cast_prob < rand:
            #     # print(f'{caster.squad.name}-{caster.name} failed to cast {self.effect_type}.')
            #     return False, total_heal

            # 计算治疗
            heal = self.calc_heal(character, target, effect_coef=self.heal_coef, effect_base_heal=self.heal_base)
            total_heal += heal

            # 造成治疗
            target.take_heal(heal)

            # 打印日志
            # self.log(character, target, heal)

        return total_heal

    def calc_heal(self, caster, target, effect_coef, effect_base_heal):
        heal = (effect_coef * caster.max_hp + effect_base_heal) * (1 + target.heal_rcv_inc) * (1 + caster.heal_deal_inc)
        return heal

    def log(self, caster, target, heal):
        print(
            f'{caster.squad.name}-{caster.name} to {target.squad.name}-{target.name} {heal} {self.effect_type}.')


class BuffEffect(Effect):
    def __init__(self, buffs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 示例：buffs = {'atk_multi': 0.1}
        self.buffs = buffs

    def clone(self):
        return BuffEffect(buffs=self.buffs, effect_type=self.effect_type, target_area=self.target_area,
                          duration=self.duration, cast_prob_lower_bound=self.cast_prob_lower_bound,
                          cast_prob_upper_bound=self.cast_prob_upper_bound, target_select=self.target_select,
                          area_shape=self.area_shape, area_length=self.area_length, area_width=self.area_width,
                          area_angle=self.area_angle, distance_limit=self.distance_limit, max_targets=self.max_targets,
                          target_type=self.target_type)

    def run(self, caster, squads):
        # 选择目标
        targets = self.select_targets(caster, squads)
        return True, targets

    def apply(self, caster, targets):
        for target in targets:
            # 计算效果释放概率
            cast_prob = self.calc_cast_prob(caster, target)
            # 生成随机数
            rand = random.random()
            if cast_prob < rand:
                # print(f'{caster.squad.name}-{caster.name} failed to cast {self.effect_type}.')
                return
            # 造成增益
            target.effect_tracker.add_buff_effect(self.clone())

            # 打印日志
            # self.log(caster, target)

    def tick(self, character):
        self.duration -= 1
        # if self.duration < 0:
        #     print(f'{character.squad.name}-{character.name} {self.buffs} {self.effect_type} expired.')

    def log(self, caster, target):
        print(
            f'{caster.squad.name}-{caster.name} to {target.squad.name}-{target.name} {self.buffs} {self.effect_type}.')


class DOTEffect(Effect):
    def __init__(self, dmg_coef, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 示例：buffs = {'atk_multi': 0.1}
        self.dmg_coef = dmg_coef

    def clone(self):
        return DOTEffect(dmg_coef=self.dmg_coef, effect_type=self.effect_type, target_area=self.target_area,
                         duration=self.duration, cast_prob_lower_bound=self.cast_prob_lower_bound,
                         cast_prob_upper_bound=self.cast_prob_upper_bound, target_select=self.target_select,
                         area_shape=self.area_shape, area_length=self.area_length, area_width=self.area_width,
                         area_angle=self.area_angle, distance_limit=self.distance_limit, max_targets=self.max_targets,
                         target_type=self.target_type)

    def run(self, caster, squads):
        # 选择目标
        targets = self.select_targets(caster, squads)
        return True, targets

    def apply(self, caster, targets):
        for target in targets:
            # 计算效果释放概率
            cast_prob = self.calc_cast_prob(caster, target)
            # 生成随机数
            rand = random.random()
            if cast_prob < rand:
                # print(f'{caster.squad.name}-{caster.name} failed to cast {self.effect_type}.')
                return False, []

            # 造成增益
            target.effect_tracker.add_dot(self.clone())

            # 打印日志
            # self.log(caster, target)

    def tick(self, character):
        self.duration -= 1
        # if self.duration < 0:
        #     print(f'{character.squad.name}-{character.name} {self.effect_type} expired.')

    def log(self, caster, target):
        print(
            f'{caster.squad.name}-{caster.name} to {target.squad.name}-{target.name} {self.effect_type}.')


class SpecialEffect(Effect):
    def __init__(self, dmg_coef=1.0, base_dmg=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dmg_coef = dmg_coef
        self.base_dmg = base_dmg
        self.used = False

    def clone(self):
        return SpecialEffect(base_dmg=self.base_dmg, dmg_coef=self.dmg_coef, effect_type=self.effect_type,
                             target_area=self.target_area,
                             duration=self.duration, cast_prob_lower_bound=self.cast_prob_lower_bound,
                             cast_prob_upper_bound=self.cast_prob_upper_bound, target_select=self.target_select,
                             area_shape=self.area_shape, area_length=self.area_length, area_width=self.area_width,
                             area_angle=self.area_angle, distance_limit=self.distance_limit,
                             max_targets=self.max_targets,
                             target_type=self.target_type)

    def run(self, caster, squads):
        # 选择目标
        targets = self.select_targets(caster, squads)
        return True, targets

    def apply(self, caster, targets):
        for target in targets:
            # 计算效果释放概率
            cast_prob = self.calc_cast_prob(caster, target)
            # 生成随机数
            rand = random.random()
            if cast_prob < rand:
                return

            # 施加特殊效果
            target.effect_tracker.add_spcl_eff(self.clone())
            # 打印日志
            # self.log(caster, target)

    def tick(self, character):
        self.duration -= 1
        # if self.duration < 0:
        #     print(f'{character.squad.name}-{character.name} {self.effect_type} expired.')

    def log(self, caster, target):
        print(
            f'{caster.squad.name}-{caster.name} to {target.squad.name}-{target.name} {self.effect_type}.')


class EffectTracker:
    def __init__(self):
        self.buff_effects = []
        self.spcl_effs = []
        self.dots = []

    def add_buff_effect(self, effect):
        self.buff_effects.append(effect)

    def add_spcl_eff(self, effect):
        self.spcl_effs.append(effect)

    def add_dot(self, effect):
        self.dots.append(effect)

    def tick(self, character):
        for effect in self.buff_effects:
            effect.tick(character)
            # if effect.duration < 0:
            #     self.effects.remove(effect)
        self.buff_effects = [effect for effect in self.buff_effects if effect.duration >= 0]

        for effect in self.spcl_effs:
            effect.tick(character)
            # if effect.duration < 0:
            #     self.effects.remove(effect)
        self.spcl_effs = [effect for effect in self.spcl_effs if effect.duration >= 0]

        for effect in self.dots:
            effect.tick(character)
            # if effect.duration < 0:
            #     self.effects.remove(effect)
        self.dots = [effect for effect in self.dots if effect.duration >= 0]

    def is_exist(self, effect_type):
        for effect in self.spcl_effs:
            if effect.effect_type == effect_type:
                return True
        return False

    def get_effect(self, effect_type):
        for effect in self.spcl_effs:
            if effect.effect_type == effect_type:
                return effect
        return None
