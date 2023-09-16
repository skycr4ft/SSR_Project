from Character import Character
from Skill import Skill
from Squad import Squad
from Battle import Battle
import Consts
from ExcelConfig.HeroStats import Hero_Skills, Heroes_qlt, Hero_level
import matplotlib
from ExcelConfig.HeroStats import Numerical, calc_hero_power, active_hero_progress, super_hero_progress
from ExcelConfig.MonsterStats import Mon_Numerical
import csv


# def main():
#     # Define the characters and their skills
#     super_r_orange_hero_info = {'hero': '', 'level': 40, 'star': 5, 'quality': 'orange', 'item_qlt': 'orange',
#                                 'item_tier': 't2_power', 'item_num': 5,
#                                 'item_boost': 10, 'pet_qlt': 'orange', 'pet_lvl': 40, 'pet_star': 11}
#     super_r_purple_hero_info = {'hero': '', 'level': 40, 'star': 5, 'quality': 'purple', 'item_qlt': 'orange',
#                                 'item_tier': 't2_power', 'item_num': 5,
#                                 'item_boost': 10, 'pet_qlt': 'orange', 'pet_lvl': 40, 'pet_star': 11}
#     active_orange_hero_info = {'hero': '', 'level': 35, 'star': 1, 'quality': 'orange', 'item_qlt': 'blue',
#                                'item_tier': 't2_power', 'item_num': 5,
#                                'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
#     # active_purple_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'purple', 'item_qlt': 'blue',
#     #                            'item_tier': 't2_power', 'item_num': 5,
#     #                            'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
#     # active_blue_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'blue', 'item_qlt': 'blue',
#     #                          'item_tier': 't2_power', 'item_num': 5,
#     #                          'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 4}
#     active_purple_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'purple', 'item_qlt': 'blue',
#                                'item_tier': 't2_power', 'item_num': 5,
#                                'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 8}
#     active_blue_hero_info = {'hero': '', 'level': 35, 'star': 3, 'quality': 'blue', 'item_qlt': 'blue',
#                              'item_tier': 't2_power', 'item_num': 5,
#                              'item_boost': 1, 'pet_qlt': 'orange', 'pet_lvl': 35, 'pet_star': 4}
#     hero_builder = Numerical()
#     monster_builder = Mon_Numerical()
#
#     heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']
#
#     ## PVP
#     N = 1000
#     turn = 0
#     victory_num = 0
#     for i in range(N):
#         squad1 = ['东', '奈乔', '杰玛']
#         squad2 = ['']
#         squad1_list, squad2_list = [], []
#         for member in squad1:
#             if Heros[member] == 'blue':
#                 active_blue_hero_info['hero'] = member
#                 hero_info = active_blue_hero_info
#             elif Heros[member] == 'purple':
#                 active_purple_hero_info['hero'] = member
#                 hero_info = active_purple_hero_info
#             else:
#                 active_orange_hero_info['hero'] = member
#                 hero_info = active_orange_hero_info
#             squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))
#         for member in squad2:
#             if Heros[member] == 'purple':
#                 active_purple_hero_info['hero'] = member
#                 hero_info = active_purple_hero_info
#             else:
#                 active_orange_hero_info['hero'] = member
#                 hero_info = active_orange_hero_info
#             squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))
#
#         # Create the squads
#         squad2 = Squad('A', characters=squad1_list, alliance='超R')
#         squad1 = Squad('B', characters=squad2_list, alliance='活跃')
#
#         # Create the battle
#         battle = Battle(squad1=squad1, squad2=squad2)
#
#         battle.fight()
#
#         if squad1
#
#         # Print the battle log
#         # battle.print_log()
#
#         # Print total damage by character
#         character_damage = battle.get_total_damage_by_character()
#         # for squad in battle.squads:
#         #     for character in squad.characters:
#         #         total_dmg = character.skill_dmg_dealt + character.atk_dmg_dealt
#         #         print(f"部队{squad.name}-{character.name} 造成的总伤害是 {total_dmg}。")
#         #         print(
#         #             f'部队{squad.name}-{character.name} 造成的技能伤害是 {character.skill_dmg_dealt}，占比为 {character.skill_dmg_dealt / total_dmg}。')
#         #         print(
#         #             f'部队{squad.name}-{character.name} 造成的普攻伤害是 {character.atk_dmg_dealt}，占比为 {character.atk_dmg_dealt / total_dmg}。')
#         #         character.skill_dmg_dealt = 0
#         #         character.atk_dmg_dealt = 0
#         #
#         # print(f'部队{squad1.name} 释放 {squad1.skill_cast_time} 次技能')
#         # print(f'部队{squad2.name} 释放 {squad2.skill_cast_time} 次技能')
#         turn += battle.turn
#
#     print('平均回合数', turn / N)
#     print('平均战胜队伍数', victory_num / N)

def main():
    PVP_1vN()

def PVP_1v1():
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
    monster_builder = Mon_Numerical()

    heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']

    ## PVP
    N = 1000
    turn = 0
    for i in range(N):
        squad1 = ['东', '奈乔', '杰玛']
        squad2 = ['']
        squad1_list, squad2_list = [], []
        for member in squad1:
            if Heroes_qlt[member] == 'blue':
                active_blue_hero_info['hero'] = member
                hero_info = active_blue_hero_info
            elif Heroes_qlt[member] == 'purple':
                active_purple_hero_info['hero'] = member
                hero_info = active_purple_hero_info
            else:
                active_orange_hero_info['hero'] = member
                hero_info = active_orange_hero_info
            squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))
        for member in squad2:
            if Heroes_qlt[member] == 'purple':
                active_purple_hero_info['hero'] = member
                hero_info = active_purple_hero_info
            else:
                active_orange_hero_info['hero'] = member
                hero_info = active_orange_hero_info
            squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))

        # Create the squads
        squad2 = Squad('A', characters=squad1_list, alliance='超R')
        squad1 = Squad('B', characters=squad2_list, alliance='活跃')

        # Create the battle
        battle = Battle(squad1=squad1, squad2=squad2)

        battle.fight()

        # Print the battle log
        # battle.print_log()

        # Print total damage by character
        character_damage = battle.get_total_damage_by_character()
        # for squad in battle.squads:
        #     for character in squad.characters:
        #         total_dmg = character.skill_dmg_dealt + character.atk_dmg_dealt
        #         print(f"部队{squad.name}-{character.name} 造成的总伤害是 {total_dmg}。")
        #         print(
        #             f'部队{squad.name}-{character.name} 造成的技能伤害是 {character.skill_dmg_dealt}，占比为 {character.skill_dmg_dealt / total_dmg}。')
        #         print(
        #             f'部队{squad.name}-{character.name} 造成的普攻伤害是 {character.atk_dmg_dealt}，占比为 {character.atk_dmg_dealt / total_dmg}。')
        #         character.skill_dmg_dealt = 0
        #         character.atk_dmg_dealt = 0
        #
        # print(f'部队{squad1.name} 释放 {squad1.skill_cast_time} 次技能')
        # print(f'部队{squad2.name} 释放 {squad2.skill_cast_time} 次技能')
        turn += battle.turn

    print('平均回合数', turn / N)


def PVP_1vN():
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
    monster_builder = Mon_Numerical()

    heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']

    ## PVP
    cfgs = []
    for i in range(len(active_hero_progress)):
        cfgs.append([active_hero_progress[i], super_hero_progress[i]])

    for cfg in cfgs:
        N = 1000
        turn = 0
        victory_num = 0
        for i in range(N):
            _squad1 = ['东', '奈乔', '杰玛']
            _squad2 = ['杰登', '吉尔伯特', '大鹅']
            squad2_list = []
            for i in range(len(_squad2)):
                cfg[1][i]['hero'] = _squad2[i]
                cfg[1][i]['quality'] = Heroes_qlt[_squad2[i]]
                squad2_list.append(Character(**hero_builder.pack(cfg[1][i]), skills=Hero_Skills[_squad2[i]]))

            squad2 = Squad('A', characters=squad2_list, alliance='超R')

            while True:
                squad1_list = []
                for i in range(len(_squad1)):
                    cfg[0][i]['hero'] = _squad1[i]
                    cfg[0][i]['quality'] = Heroes_qlt[_squad1[i]]
                    squad1_list.append(Character(**hero_builder.pack(cfg[0][i]), skills=Hero_Skills[_squad1[i]]))
                squad1 = Squad('B', characters=squad1_list, alliance='活跃')

                battle = Battle(squad1=squad1, squad2=squad2)
                battle.fight()
                turn += battle.turn

                # 如果超R队伍胜利，则战胜队伍数+1，否则跳出循环
                if squad2.is_alive():
                    victory_num += 1
                else:
                    break



        print('平均回合数', turn / N)
        print('平均战胜队伍数', victory_num / N)


def PVP_NvM():
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
    monster_builder = Mon_Numerical()

    heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']

    ## PVP
    cfgs = [[], []]

    for cfg in cfgs:
        N = 1000
        turn = 0
        victory_num = 0
        for i in range(N):
            squad1 = ['东', '奈乔', '杰玛']
            squad2 = ['']
            squad1_list, squad2_list = [], []
            for member in squad2:
                if Heroes_qlt[member] == 'purple':
                    active_purple_hero_info['hero'] = member
                    hero_info = active_purple_hero_info
                else:
                    active_orange_hero_info['hero'] = member
                    hero_info = active_orange_hero_info
                squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))

            squad2 = Squad('A', characters=squad1_list, alliance='超R')

            while True:
                for member in squad1:
                    if Heroes_qlt[member] == 'blue':
                        active_blue_hero_info['hero'] = member
                        hero_info = active_blue_hero_info
                    elif Heroes_qlt[member] == 'purple':
                        active_purple_hero_info['hero'] = member
                        hero_info = active_purple_hero_info
                    else:
                        active_orange_hero_info['hero'] = member
                        hero_info = active_orange_hero_info
                    squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))
                squad1 = Squad('B', characters=squad2_list, alliance='活跃')

                battle = Battle(squad1=squad1, squad2=squad2)
                battle.fight()

                # 如果超R队伍胜利，则战胜队伍数+1，否则跳出循环
                if squad2.is_alive():
                    victory_num += 1
                else:
                    break

            turn += battle.turn

        print('平均回合数', turn / N)
        print('平均战胜队伍数', victory_num / N)


def PVE_1v1():
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
    monster_builder = Mon_Numerical()

    heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']

    N = 1000
    turn = 0
    a, b = 0, 0
    battle_loss = 0
    rows = ['SLG怪物等级', '剩余血量']
    for k in range(20):
        level = int((k + 1) * (k + 1) * 0.05 + 0.2 * (k + 1) + 5)
        print('level:', k + 1)
        for i in range(N):
            active_blue_hero_info1 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_blue_hero_info2 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_blue_hero_info3 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_purple_hero_info = {'hero': '', 'level': level, 'star': 1, 'quality': 'purple', 'item_qlt': 'blue',
                                       'item_tier': 't1_power', 'item_num': 0,
                                       'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            squad = ['奈乔', '东', '杰玛']
            squad1_list, squad2_list = [], []
            # for member in squad:
            #     if Heros[member] == 'blue':
            #         active_blue_hero_info['hero'] = member
            #         hero_info = active_blue_hero_info
            #     elif Heros[member] == 'purple':
            #         active_purple_hero_info['hero'] = member
            #         hero_info = active_purple_hero_info
            #     else:
            #         active_orange_hero_info['hero'] = member
            #         hero_info = active_orange_hero_info
            #     squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))

            hero_info1, hero_info2, hero_info3 = active_blue_hero_info1, active_blue_hero_info2, active_purple_hero_info
            hero_info1['hero'], hero_info2['hero'], hero_info3['hero'] = '杰玛', '东', '奈乔'
            hero_info1['level'], hero_info2['level'], hero_info3['level'] = Hero_level[k][0], Hero_level[k][1], \
                Hero_level[k][2]
            squad1_list = [Character(**hero_builder.pack(hero_info1), skills=Hero_Skills['杰玛']),
                           Character(**hero_builder.pack(hero_info2), skills=Hero_Skills['东']),
                           Character(**hero_builder.pack(hero_info3), skills=Hero_Skills['奈乔'])]
            # for member in squad1_list:
            #     print(member.name, member.level, member.max_hp, member.attack, member.defense)

            hero_info = active_blue_hero_info3
            hero_info['hero'] = '白板'
            hero_info['level'] = level
            for i in range(3):
                squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills['白板']))

            # for member in squad2_list:
            #     print(member.name, member.level, member.max_hp, member.attack, member.defense)

            # Create the squads
            squad1 = Squad('A', characters=squad1_list, alliance='Justice')
            squad2 = Squad('B', characters=squad2_list, alliance='Evil')

            # Create the battle
            battle = Battle(squad1=squad1, squad2=squad2)

            battle.fight()
            for squad in battle.squads:
                for character in squad.characters:
                    if character is not None:
                        total_dmg = character.skill_dmg_dealt + character.atk_dmg_dealt
                        # print(f"部队{squad.name}-{character.name} 造成的总伤害是 {total_dmg}。")
                        # print(
                        #     f'部队{squad.name}-{character.name} 造成的技能伤害是 {character.skill_dmg_dealt}，占比为 {character.skill_dmg_dealt / total_dmg}。')
                        # print(
                        #     f'部队{squad.name}-{character.name} 造成的普攻伤害是 {character.atk_dmg_dealt}，占比为 {character.atk_dmg_dealt / total_dmg}。')

                        character.skill_dmg_dealt = 0
                        character.atk_dmg_dealt = 0

            hp_remain = 0
            hp_max = 0
            for hero in squad1.characters:
                hp_remain += hero.curr_hp
                hp_max += hero.max_hp

            if battle.squads[0].is_alive():
                a += 1
                # print('Justice win!')
            else:
                b += 1
                # print('Evil win!')

            turn += battle.turn
            battle_loss += hp_remain / hp_max

        power = 0
        for character in squad1.characters:
            power += calc_hero_power(character)
        print("队伍战力：", power)
        print('平均回合数：', turn / N)
        print('平均剩余血量：', battle_loss / N)
        print('Justice win rate:', a / N)
        print('Evil win rate:', b / N)

        rows.append([k + 1, battle_loss / N])

        turn = 0
        battle_loss = 0
        a = 0
        b = 0
    with open('C:\\Users\Administrator\Desktop\BattleLoss.csv', 'w', newline='',
              encoding='utf-8') as loss:
        writer = csv.writer(loss)
        writer.writerows(rows)


def PVE_Nv1():
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
    monster_builder = Mon_Numerical()

    heros = ['奈乔', '东', '杰玛', '按摩师', '金鼻子', '苏茜', '女医生']

    N = 1000
    turn = 0
    a, b = 0, 0
    battle_loss = 0
    rows = ['SLG怪物等级', '剩余血量']
    for k in range(20):
        level = int((k + 1) * (k + 1) * 0.05 + 0.2 * (k + 1) + 5)
        print('level:', k + 1)
        for i in range(N):
            active_blue_hero_info1 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_blue_hero_info2 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_blue_hero_info3 = {'hero': '', 'level': level, 'star': 1, 'quality': 'blue', 'item_qlt': 'blue',
                                      'item_tier': 't1_power', 'item_num': 0,
                                      'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            active_purple_hero_info = {'hero': '', 'level': level, 'star': 1, 'quality': 'purple', 'item_qlt': 'blue',
                                       'item_tier': 't1_power', 'item_num': 0,
                                       'item_boost': 1, 'pet_qlt': 'blue', 'pet_lvl': 1, 'pet_star': 1}
            squad = ['奈乔', '东', '杰玛']
            squad1_list, squad2_list = [], []
            # for member in squad:
            #     if Heros[member] == 'blue':
            #         active_blue_hero_info['hero'] = member
            #         hero_info = active_blue_hero_info
            #     elif Heros[member] == 'purple':
            #         active_purple_hero_info['hero'] = member
            #         hero_info = active_purple_hero_info
            #     else:
            #         active_orange_hero_info['hero'] = member
            #         hero_info = active_orange_hero_info
            #     squad1_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills[member]))

            hero_info1, hero_info2, hero_info3 = active_blue_hero_info1, active_blue_hero_info2, active_purple_hero_info
            hero_info1['hero'], hero_info2['hero'], hero_info3['hero'] = '杰玛', '东', '奈乔'
            hero_info1['level'], hero_info2['level'], hero_info3['level'] = Hero_level[k][0], Hero_level[k][1], \
                Hero_level[k][2]
            squad1_list = [Character(**hero_builder.pack(hero_info1), skills=Hero_Skills['杰玛']),
                           Character(**hero_builder.pack(hero_info2), skills=Hero_Skills['东']),
                           Character(**hero_builder.pack(hero_info3), skills=Hero_Skills['奈乔'])]
            # for member in squad1_list:
            #     print(member.name, member.level, member.max_hp, member.attack, member.defense)

            hero_info = active_blue_hero_info3
            hero_info['hero'] = '白板'
            hero_info['level'] = level
            for i in range(3):
                squad2_list.append(Character(**hero_builder.pack(hero_info), skills=Hero_Skills['白板']))

            # for member in squad2_list:
            #     print(member.name, member.level, member.max_hp, member.attack, member.defense)

            # Create the squads
            squad1 = Squad('A', characters=squad1_list, alliance='Justice')
            squad2 = Squad('B', characters=squad2_list, alliance='Evil')

            # Create the battle
            battle = Battle(squad1=squad1, squad2=squad2)

            battle.fight()
            for squad in battle.squads:
                for character in squad.characters:
                    if character is not None:
                        total_dmg = character.skill_dmg_dealt + character.atk_dmg_dealt
                        # print(f"部队{squad.name}-{character.name} 造成的总伤害是 {total_dmg}。")
                        # print(
                        #     f'部队{squad.name}-{character.name} 造成的技能伤害是 {character.skill_dmg_dealt}，占比为 {character.skill_dmg_dealt / total_dmg}。')
                        # print(
                        #     f'部队{squad.name}-{character.name} 造成的普攻伤害是 {character.atk_dmg_dealt}，占比为 {character.atk_dmg_dealt / total_dmg}。')

                        character.skill_dmg_dealt = 0
                        character.atk_dmg_dealt = 0

            hp_remain = 0
            hp_max = 0
            for hero in squad1.characters:
                hp_remain += hero.curr_hp
                hp_max += hero.max_hp

            if battle.squads[0].is_alive():
                a += 1
                # print('Justice win!')
            else:
                b += 1
                # print('Evil win!')

            turn += battle.turn
            battle_loss += hp_remain / hp_max

        power = 0
        for character in squad1.characters:
            power += calc_hero_power(character)
        print("队伍战力：", power)
        print('平均回合数：', turn / N)
        print('平均剩余血量：', battle_loss / N)
        print('Justice win rate:', a / N)
        print('Evil win rate:', b / N)

        rows.append([k + 1, battle_loss / N])

        turn = 0
        battle_loss = 0
        a = 0
        b = 0
    with open('C:\\Users\Administrator\Desktop\BattleLoss.csv', 'w', newline='',
              encoding='utf-8') as loss:
        writer = csv.writer(loss)
        writer.writerows(rows)


if __name__ == '__main__':
    PVP_1vN()
