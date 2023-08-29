from Character import Character
from Skill import Skill
from Squad import Squad
from Battle import Battle
import Consts
from ExcelConfig.Hero import Skills, Heros
import matplotlib
from ExcelConfig.Hero import Numerical


def main():
    # Define the characters and their skills
    super_r_orange_hero_info = {'hero': '', 'level': 40, 'star': 5, 'quality': 'orange', 'item_qlt': 'orange',
                                'item_tier': 't2_power', 'item_num': 5,
                                'item_boost': 10, 'pet_qlt': 'orange', 'pet_lvl': 40, 'pet_star': 11}
    super_r_purple_hero_info = {'hero': '', 'level': 40, 'star': 5, 'quality': 'purple', 'item_qlt': 'orange',
                                'item_tier': 't2_power', 'item_num': 5,
                                'item_boost': 10, 'pet_qlt': 'orange', 'pet_lvl': 40, 'pet_star': 11}
    active_orange_hero_info = {'hero': '', 'level': 35, 'star': 1, 'quality': 'orange', 'item_qlt': 'blue',
                               'item_tier': 't2_power', 'item_num': 5,
                               'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
    # active_purple_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'purple', 'item_qlt': 'blue',
    #                            'item_tier': 't2_power', 'item_num': 5,
    #                            'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
    # active_blue_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'blue', 'item_qlt': 'blue',
    #                          'item_tier': 't2_power', 'item_num': 5,
    #                          'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 4}
    active_purple_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'purple', 'item_qlt': 'blue',
                               'item_tier': 't2_power', 'item_num': 5,
                               'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
    active_blue_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'blue', 'item_qlt': 'blue',
                             'item_tier': 't2_power', 'item_num': 5,
                             'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 4}
    hero_builder = Numerical()

    squad = ['奈乔', '东', '杰玛']
    squad1_list, squad2_list = [], []

    for member in squad:
        if Heros[member] == 'blue':
            active_blue_hero_info['hero'] = member
            hero_info = active_blue_hero_info
        elif Heros[member] == 'purple':
            active_purple_hero_info['hero'] = member
            hero_info = active_purple_hero_info
        else:
            active_orange_hero_info['hero'] = member
            hero_info = active_orange_hero_info
        squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Skills[member]))
        squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Skills[member]))

    # Create the squads
    squad1 = Squad('A', characters=squad1_list, alliance='Justice')
    squad2 = Squad('B', characters=squad2_list, alliance='Evil')

    # Create the battle
    battle = Battle(squad1=squad1, squad2=squad2)

    battle.fight()

    # Print the battle log
    # battle.print_log()

    # Print total damage by character
    character_damage = battle.get_total_damage_by_character()
    for squad in battle.squads:
        for character in squad.characters:
            total_dmg = character.skill_dmg_dealt + character.atk_dmg_dealt
            print(f"部队{squad.name}-{character.name} 造成的总伤害是 {total_dmg}。")
            print(
                f'部队{squad.name}-{character.name} 造成的技能伤害是 {character.skill_dmg_dealt}，占比为 {character.skill_dmg_dealt / total_dmg}。')
            print(
                f'部队{squad.name}-{character.name} 造成的普攻伤害是 {character.atk_dmg_dealt}，占比为 {character.atk_dmg_dealt / total_dmg}。')
            character.skill_dmg_dealt = 0
            character.atk_dmg_dealt = 0

    print(f'部队{squad1.name} 释放 {squad1.skill_cast_time} 次技能')
    print(f'部队{squad2.name} 释放 {squad2.skill_cast_time} 次技能')


if __name__ == '__main__':
    main()
