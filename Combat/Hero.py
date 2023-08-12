from Attr import Attr


class Hero:

    def __init__(self, Name, Quality, Atk, Def, HP, Crit=0, Crit_Rst=0, Crit_Dmg=1, Crit_Dmg_Rst=0,
                 Effc_Hit=0, Effc_Rst=0, lvl=1):
        ##
        self.Attr = Attr(Atk=Atk, Def=Def, HP=HP, Crit=Crit, Crit_Rst=Crit_Rst, Crit_Dmg=Crit_Dmg,
                         Crit_Dmg_Rst=Crit_Dmg_Rst, Effc_Hit=Effc_Hit, Effc_Rst=Effc_Rst)
        self.Name, self.Quality, self.lvl = Name, Quality, lvl


        