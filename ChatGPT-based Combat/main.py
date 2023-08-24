from Character import Character
from Skill import Skill
from Squad import Squad
from Battle import Battle
import Config
import matplotlib


def main():
    # Define the characters and their skills

    skills1 = [
        Config.Gem_skill,
        Config.Uni_attack
    ]
    skills2 = [
        Config.Nitro_skill,
        Config.Uni_attack
    ]
    skills3 = [
        Config.Don_skill,
        Config.Uni_attack
    ]

    # Create the characters
    character1 = Character(name='奈乔', level=30, attack_base=68.828, defense_base=68.828,
                           max_hp_base=1802.6/3,
                           crit_base=18.75, crit_resistance_base=18.75, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.11, effect_resistance_base=0.08, skills=skills3, rage_increase_base=15)
    character2 = Character(name='东', level=30, attack_base=51.45, defense_base=51.45,
                           max_hp_base=1349.3/3,
                           crit_base=15, crit_resistance_base=15, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.09, effect_resistance_base=0.07, skills=skills2, rage_increase_base=15)
    character3 = Character(name='杰玛', level=30, attack_base=51.45, defense_base=51.45, max_hp_base=1349.3/3,
                           crit_base=15, crit_resistance_base=15, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.09, effect_resistance_base=0.07, skills=skills1, rage_increase_base=15)

    character4 = Character(name='奈乔', level=30, attack_base=68.828, defense_base=68.828,
                           max_hp_base=1802.6/3,
                           crit_base=18.75, crit_resistance_base=18.75, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.11, effect_resistance_base=0.08, skills=skills3, rage_increase_base=15)
    character5 = Character(name='东', level=30, attack_base=51.45, defense_base=51.45,
                           max_hp_base=1349.3/3,
                           crit_base=15, crit_resistance_base=15, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.09, effect_resistance_base=0.07, skills=skills2, rage_increase_base=15)
    character6 = Character(name='杰玛', level=30, attack_base=51.45, defense_base=51.45, max_hp_base=1349.3/3,
                           crit_base=15, crit_resistance_base=15, crit_damage_base=0, crit_reduction_base=0,
                           effect_hit_base=0.09, effect_resistance_base=0.07, skills=skills1, rage_increase_base=15)

    # Create the squads
    # squad1 = Squad('A', characters=[character1, character2, character3], alliance='Justice')
    # squad2 = Squad('B', characters=[character4, character5, character6], alliance='Evil')

    squad1 = Squad('A', characters=[character2], alliance='Justice')
    squad2 = Squad('B', characters=[character1], alliance='Evil')

    # Create the battle
    battle = Battle(squad1=squad1, squad2=squad2)

    battle.fight()

    # Print the battle log
    # battle.print_log()

    # Print total damage by squad
    squad_damage = battle.get_total_damage_by_squad()
    for squad, damage in squad_damage.items():
        print(f"{squad} 造成的总伤害是 {damage}。")

    # Print total damage by character
    character_damage = battle.get_total_damage_by_character()
    for character, damage in character_damage.items():
        print(f"{character} 造成的总伤害是 {damage}。")

    print(f'部队{squad1.name} 释放 {squad1.skill_cast_time} 次技能')
    print(f'部队{squad2.name} 释放 {squad2.skill_cast_time} 次技能')


if __name__ == '__main__':
    main()
