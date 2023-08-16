import random


class Effect:
    def __init__(self, effect_type, target_area, duration=0, cast_prob_lower_bound=100,cast_prob_upper_bound=100,
                 target_select='random', area_shape=None, area_length=0.0, area_width=0.0, area_angle=0.0,
                 distance_limit=0.0, max_targets=1, target_type='enemy', damage_coef=1.0, base_damage=0.0):
        # 效果释放概率下限
        self.cast_prob_lower_bound = cast_prob_lower_bound
        # 效果释放概率上限
        self.cast_prob_upper_bound = cast_prob_upper_bound

        # 效果类型，取值范围为{伤害，治疗，增益，减益} {'damage', 'heal', 'buff', 'debuff'}
        self.effect_type = effect_type
        # 效果目标，取值范围为{单体，群体} {'single', 'multiple'}
        self.target_area = target_area
        # 选择目标的方法 {Random, Weakest}
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

    # def apply(self, character, effect_value):
    #     raise NotImplementedError

    def tick(self, character):
        # Define what happens when the effect "ticks" (i.e., advances one time step)
        pass

    def calc_cast_prob(self, caster, target) -> float:
        cast_prob = self.cast_prob_lower_bound + (self.cast_prob_upper_bound - self.cast_prob_lower_bound) * \
            (caster.effect_hit - target.effect_resistance)
        cast_prob = min(self.cast_prob_upper_bound, max(self.cast_prob_lower_bound, cast_prob))
        return cast_prob

    def run(self, caster, target):
        raise NotImplementedError

    def select_targets(self, character, squads, skill):
        if skill.target_type == 'enemy':
            target_squads = [squad for squad in squads if squad != character.squad]
        elif skill.target_type == 'ally':
            target_squads = [character.squad]
        # elif skill.target_type == 'self':
        else:
            target_squads = [character.squad]

        if skill.target_area == 'single':
            target_list = []
            for squad in target_squads:
                target_list.extend(squad.characters)
            if skill.target_type == 'enemy':
                # Select a target from the enemy squad based on the target_select attribute of the skill
                if skill.target_select == 'weakest':
                    target = [min(target_list, key=lambda character: character.current_health)]
                elif skill.target_select == 'strongest':
                    target = [max(target_list, key=lambda character: character.current_health)]
                else:  # random selection
                    target = random.sample(target_list, min(skill.max_targets, len(target_list)))
            elif skill.target_type == 'ally':
                # Select a target from the ally squad, excluding the attacker
                target_list.remove(character)
                target = random.sample(target_list, min(skill.max_targets, len(target_list)))
            # elif skill.target_type == 'self':
            else:
                target = [character]
            return target
        elif skill.target_area == 'multiple':
            target_squads = random.sample(target_squads, min(skill.max_targets, len(target_squads)))
            target_list = []
            for squad in target_squads:
                for target in squad.members:
                    if target.is_alive():  # only attack alive characters
                        target_list.append(target)
            return target_list


class DamageEffect(Effect):
    def __init__(self, damage_coef, damaga_base, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage_coef = damage_coef
        self.damaga_base = damaga_base

    def apply_one_target(self, caster, target):
        # 计算效果释放概率
        cast_prob = self.calc_cast_prob(caster, target)
        # 生成随机数
        rand = random.random()
        if cast_prob < rand:
            print(f'{caster.name} failed to cast {self.effect_type}.')
            return 0
        # 计算伤害
        damage = caster.calculate_damage(target, skill_coef=self.damage_coef, skill_base_damage=self.damaga_base)
        # 造成伤害
        target.take_damage(damage)
        return damage

    def run(self, caster, squads) -> float:
        # 选择目标
        targets = self.select_targets(caster, squads, self)
        # 计算总伤害
        total_damage = 0
        for target in targets:
            total_damage += self.apply_one_target(caster, target)
        return total_damage


class HealEffect(Effect):
    def __init__(self, heal_coef, heal_base, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heal_coef = heal_coef
        self.heal_base = heal_base


class BuffEffect(Effect):
    def __init__(self, attribute, increase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attribute = attribute
        self.increase = increase

    def apply(self, character):
        setattr(character, self.attribute, getattr(character, self.attribute) + self.increase)

    def tick(self, character):
        self.duration -= 1
        if self.duration <= 0:
            # Remove the buff when the duration is over
            setattr(character, self.attribute, getattr(character, self.attribute) - self.increase)


class Skill:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def use(self, character, target):
        for effect in self.effects:
            if effect.is_applicable(character):
                effect.apply(target)
                if effect.duration > 0:
                    character.effect_tracker.add_effect(effect)


class Character:
    # ...existing code...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.effect_tracker = EffectTracker()

    def use_skill(self, skill, target):
        skill.use(self, target)

    def tick(self):
        self.effect_tracker.tick(self)


class EffectTracker:
    def __init__(self):
        self.effects = []

    def add_effect(self, effect):
        self.effects.append(effect)

    def tick(self, character):
        for effect in self.effects:
            effect.tick(character)
        self.effects = [effect for effect in self.effects if effect.duration > 0]
