

class Attr:
    # Atk=攻击力， Def=防御力， HP=生命值， Crit=暴击， CritRst=暴击抵抗， Crit_Dmg=暴击伤害, Crit_Dmg_Rst=暴击减伤, Effc_Hit=效果命中, Effc_Rst=
    def __init__(self, Atk, Def, HP, Crit, Crit_Rst, Crit_Dmg, Crit_Dmg_Rst, Effc_Hit, Effc_Rst):
        self.Atk, self.Def, self.HP, self.Crit, self.Crit_Rst, self.Crit_Dmg, self.Crit_Dmg_Rst, self.Effc_Hit, self.Effc_Rst = \
            Atk, Def, HP, Crit, Crit_Rst, Crit_Dmg, Crit_Dmg_Rst, Effc_Hit, Effc_Rst
