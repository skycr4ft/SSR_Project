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
    character1 = Character(name='Don', attack=68.828, defense=68.828, max_hp=1802.6/3, curr_hp=1802.6/3,
                           crit=18.75, crit_resistance=18.75, crit_damage=0, crit_reduction=0, effect_hit=0.11,
                           effect_resistance=0.08, skills=skills3, rage_increase=20)
    character2 = Character(name='Nitro', attack=51.45, defense=51.45, max_hp=1349.3/3, curr_hp=1349.3/3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills2, rage_increase=20)
    character3 = Character(name='Gem', attack=51.45, defense=51.45, max_hp=1349.3/4, curr_hp=1349.3/3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills1, rage_increase=20)

    character4 = Character(name='Don', attack=68.828, defense=68.828, max_hp=1802.6/3, curr_hp=1802.6/3,
                           crit=18.75, crit_resistance=18.75, crit_damage=0, crit_reduction=0, effect_hit=0.11,
                           effect_resistance=0.08, skills=skills3, rage_increase=20)
    character5 = Character(name='Nitro', attack=51.45, defense=51.45, max_hp=1349.3/3, curr_hp=1349.3/3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills2, rage_increase=20)
    character6 = Character(name='Gem', attack=51.45, defense=51.45, max_hp=1349.3/3, curr_hp=1349.3/3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills1, rage_increase=20)

    # Create the squads
    squad1 = Squad('A', characters=[character1, character2, character3], alliance='Justice')
    squad2 = Squad('B', characters=[character4, character5, character6], alliance='Evil')

    # Create the battle
    battle = Battle(squad1=squad1, squad2=squad2)

    # Run the battle for 10 turns
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
