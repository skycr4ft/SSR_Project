import random


class Battle:
    def __init__(self, squad1, squad2):
        self.squads = [squad1, squad2]
        self.turn = 0
        self.log = []

    def fight(self):
        random.seed(1)
        while self.squads[0].is_alive() and self.squads[1].is_alive():
            self.next_turn()

    def next_turn(self):
        self.turn += 1
        print(f'【回合{self.turn}】')
        # Get the squads for this turn
        squad1 = self.squads[0]
        squad2 = self.squads[1]

        # 更新所有角色的状态
        squad1.update()
        squad2.update()

        # Get the characters for this turn
        # character1 = squad1.get_next_alive_character()
        # character2 = squad2.get_next_alive_character()

        # Get the characters for this turn
        character1 = squad1.get_next_character()
        character2 = squad2.get_next_character()

        if character1 is None:
            print(f'Squad {squad1.name} - idle')
        else:
            print(f'Squad {squad1.name} - {character1.name}')
        if character2 is None:
            print(f'Squad {squad2.name} - idle')
        else:
            print(f'Squad {squad2.name} - {character2.name}')

        # Determine if the squads are in the rage skill phase
        is_rage_skill_phase1 = squad1.rage_skill_phase > 0
        is_rage_skill_phase2 = squad2.rage_skill_phase > 0

        # Get the skills for this turn
        skill1 = character1.take_action(is_rage_skill_phase1) if character1 is not None else None
        skill2 = character2.take_action(is_rage_skill_phase2) if character2 is not None else None

        # select_targets
        is_cast_list1, target_list1 = character1.select_targets(self.squads, skill1) if character1 is not None \
            else ([], [])
        is_cast_list2, target_list2 = character2.select_targets(self.squads, skill2) if character2 is not None \
            else ([], [])

        # cast skill
        character1.cast_skill(target_list1, skill1) if character1 is not None else (0, [])
        character2.cast_skill(target_list2, skill2) if character2 is not None else (0, [])

        # 记录每回合的攻击方、受击方、技能和造成伤害的日志
        # if is_cast:
        #     self.log.append((self.turn, squads.name, self.name,
        #                      [target.name for target in target_list1], skill.name, damage))
        # else:
        #     self.log.append((self.turn, squad1.name, character1.name,
        #                      [target.name for target in target_list1], skill1.name, damage))
        # for effect in skill1.effects:
        #     is_cast, damage = effect.run(character1, target_squads1)
        #     # 记录每回合的攻击方、受击方、技能和造成伤害的日志
        #     if is_cast:
        #         self.log.append((self.turn, squad1.name, character1.name,
        #                          [target.name for target in target_list1], skill1.name, damage))
        #     else:
        #         self.log.append((self.turn, squad1.name, character1.name,
        #                          [target.name for target in target_list1], skill1.name, damage))

        # Move to the next character in each squad
        # 决定下一回合的出手角色
        squad1.current_character_index = (squad1.current_character_index + 1) % len(squad1.characters)
        squad2.current_character_index = (squad2.current_character_index + 1) % len(squad2.characters)

        # Handle the rage skill phase and increase rage
        self.handle_rage(character1, squad1, is_rage_skill_phase1)
        self.handle_rage(character2, squad2, is_rage_skill_phase2)


    # 技能释放
    def attack(self, character, targets, skill):
        total_damage = 0
        for target in targets:
            damage = character.calc_dmg(target, skill_coef=skill.damage_coefficient,
                                        skill_base_damage=skill.base_damage)
            target.take_dmg(damage)
            total_damage += damage

        return total_damage

    ## 判断战斗是否结束
    def is_over(self):
        return not self.squads[0].is_alive() or not self.squads[1].is_alive()

    # 打印战斗日志
    def print_log(self):
        for turn, squad1, attacker, targets, skill, damage in self.log:
            print(
                f"【回合{turn}】部队{squad1} - {attacker} 对敌方{targets} 使用了 {skill}，总共造成了 {damage} 点伤害。")

    def get_total_damage_by_squad(self):
        squad_damage = {}
        for _, squad_name, _, _, _, damage in self.log:
            if squad_name not in squad_damage:
                squad_damage[squad_name] = damage
            else:
                squad_damage[squad_name] += damage
        return squad_damage

    def get_total_damage_by_character(self):
        character_damage = {}
        for _, squad_name, attacker_name, _, _, damage in self.log:
            character_name = squad_name + '-' + attacker_name
            if character_name not in character_damage:
                character_damage[character_name] = damage
            else:
                character_damage[character_name] += damage
        return character_damage

    def handle_rage(self, character, squad, is_rage_skill_phase):
        if is_rage_skill_phase:
            squad.rage_skill_phase -= 1
            if squad.rage_skill_phase == 0:
                squad.end_rage_skill_phase()
        else:
            squad.increase_rage(character.rage_increase if character is not None else 0)
            if squad.rage >= 100:
                squad.start_rage_skill_phase()

    # def get_next_alive_character(self, squad):
    #     # Find the next alive character in the squad
    #     for i in range(len(squad.characters)):
    #         character = squad.characters[(self.turn + i) % len(squad.characters)]
    #         if character.is_alive():
    #             return character
    #     return None
