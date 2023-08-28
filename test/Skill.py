
class Skill:
    def __init__(self, skill_def, skill_type, target_type, target_select, dmg_factor, dmg_base, req):
        # req: requirement，技能释放的条件
        self.req = req
        # skill_def:
        self.skill_def = skill_def
        # skill_type: 0=瞬发，1=吟唱
        self.skill_type = skill_type
        # target_type: 0=友方，1=敌方，2=自身
        self.target_type = target_type
        #
        self.target_select = target_select
        self.dmg_factor = dmg_factor
        self.dmg_base = dmg_base
        self.range = None


    def logical(self):
