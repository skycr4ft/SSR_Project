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
    character1 = Character(name='Don', attack=68.828, defense=68.828, max_hp=1802.6, curr_hp=1802.6,
                           crit=18.75, crit_resistance=18.75, crit_damage=0, crit_reduction=0, effect_hit=0.11,
                           effect_resistance=0.08, skills=skills3, rage_increase=10)
    character2 = Character(name='Nitro', attack=51.45, defense=51.45, max_hp=1349.3, curr_hp=1349.3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills2, rage_increase=20)
    character3 = Character(name='Gem', attack=51.45, defense=51.45, max_hp=1349.3, curr_hp=1349.3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills1, rage_increase=5)

    character4 = Character(name='Don', attack=68.828, defense=68.828, max_hp=1802.6, curr_hp=1802.6,
                           crit=18.75, crit_resistance=18.75, crit_damage=0, crit_reduction=0, effect_hit=0.11,
                           effect_resistance=0.08, skills=skills3, rage_increase=10)
    character5 = Character(name='Nitro', attack=51.45, defense=51.45, max_hp=1349.3, curr_hp=1349.3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills2, rage_increase=20)
    character6 = Character(name='Gem', attack=51.45, defense=51.45, max_hp=1349.3, curr_hp=1349.3,
                           crit=15, crit_resistance=15, crit_damage=0, crit_reduction=0, effect_hit=0.09,
                           effect_resistance=0.07, skills=skills1, rage_increase=5)

    # Create the squads
    squad1 = Squad('A', characters=[character1, character2, character3], alliance='Justice')
    squad2 = Squad('B', characters=[character4, character5, character6], alliance='Evil')

    # Create the battle
    battle = Battle(squad1=squad1, squad2=squad2)

    # Run the battle for 10 turns
    battle.fight()

    # Print the battle log
    battle.print_log()

    # Print total damage by squad
    squad_damage = battle.get_total_damage_by_squad()
    for squad, damage in squad_damage.items():
        print(f"{squad} 造成的总伤害是 {damage}。")

    # Print total damage by character
    character_damage = battle.get_total_damage_by_character()
    for character, damage in character_damage.items():
        print(f"{character} 造成的总伤害是 {damage}。")


if __name__ == '__main__':
    main()
