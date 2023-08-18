

class Skill:
    # def __init__(self, name, definition, type, damage_coefficient, target_area, effects, base_damage=0.0, target_select='random',
    #              area_shape=None, area_length=0.0, area_width=0.0, area_angle=0.0, distance_limit=0.0, max_targets=1,
    #              target_type='enemy', first_allowed_turn=0, cooldown_turns=0, cooldown_group=None, cooldown_time=None,
    #              cooldown_coefficient=None):
    #
    #     self.name = name
    #     # 技能定义，取值范围为{普通攻击或主动技能}
    #     self.definition = definition
    #     # 技能类型，取值范围为{瞬发或吟唱}
    #     self.type = type
    #     # 技能伤害系数
    #     self.damage_coefficient = damage_coefficient
    #     # 技能基础伤害值
    #     self.base_damage = base_damage
    #     # 技能目标，取值范围为{单体，群体} {'single', 'multiple'}
    #     self.target_area = target_area
    #     # 选择目标的方法 {Random, Weakest}
    #     self.target_select = target_select
    #     # 范围技能形状，取值范围为{扇形，矩形，圆形}
    #     self.area_shape = area_shape
    #     # 范围长或半径
    #     self.area_length = area_length
    #     # 范围宽
    #     self.area_width = area_width
    #     # 范围角度
    #     self.area_angle = area_angle
    #     # 释放距离限制
    #     self.distance_limit = distance_limit
    #     # 最大目标数
    #     self.max_targets = max_targets
    #     # 目标类型,取值范围为{敌人，友方，自身}
    #     self.target_type = target_type
    #     # 技能首次允许释放回合，默认值为0
    #     self.first_allowed_turn = first_allowed_turn
    #     # 技能冷却回合，默认值为0
    #     self.cooldown_turns = cooldown_turns
    #     # 公共冷却组，默认值为空
    #     self.cooldown_group = cooldown_group
    #     # 公共冷却时间，默认值为空
    #     self.cooldown_time = cooldown_time
    #     # 公共冷却系数，默认值为空
    #     self.cooldown_coefficient = cooldown_coefficient
    #
    #     self.effects = effects

    def __init__(self, name, definition, type, effects_param, first_allowed_turn=0, cooldown_turns=0,
                 cooldown_group=None, cooldown_time=None, cooldown_coefficient=None):
        self.name = name
        # 技能定义，取值范围为{普通攻击或主动技能}
        self.definition = definition
        # 技能类型，取值范围为{瞬发或吟唱}
        self.type = type
        # 技能首次允许释放回合，默认值为0
        self.first_allowed_turn = first_allowed_turn
        # 技能冷却回合，默认值为0
        self.cooldown_turns = cooldown_turns
        # 公共冷却组，默认值为空
        self.cooldown_group = cooldown_group
        # 公共冷却时间，默认值为空
        self.cooldown_time = cooldown_time
        # 公共冷却系数，默认值为空
        self.cooldown_coefficient = cooldown_coefficient

        # 初始化效果
        self.effects = self.create_effect(effects_param)

    # 创建效果
    def create_effect(self, effects_param):
        effects = []
        for effect_param in effects_param:
            if effect_param['effect_type'] == 'damage':
                from Effect import DamageEffect
                effect = DamageEffect(**effect_param)
                effects.append(effect)
            elif effect_param['effect_type'] == 'heal':
                from Effect import HealEffect
                effect = HealEffect(**effect_param)
                effects.append(effect)
            elif effect_param['effect_type'] == 'buff':
                from Effect import BuffEffect
                effect = BuffEffect(**effect_param)
                effects.append(effect)
            elif effect_param['effect_type'] == 'debuff':
                from Effect import DebuffEffect
                effect = DebuffEffect(**effect_param)
                effects.append(effect)
        return effects

