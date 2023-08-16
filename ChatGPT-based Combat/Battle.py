import random

class Battle:
    def __init__(self, squad1, squad2):
        self.squads = [squad1, squad2]
        self.turn = 0
        self.log = []
        random.seed(1)

    def fight(self):
        while self.squads[0].is_alive() and self.squads[1].is_alive():
            self.next_turn()

    def next_turn(self):
        self.turn += 1
        # Get the squads for this turn
        squad1 = self.squads[0]
        squad2 = self.squads[1]

        # Get the characters for this turn
        character1 = squad1.get_next_alive_character()
        character2 = squad2.get_next_alive_character()

        # Determine if the squads are in the rage skill phase
        is_rage_skill_phase1 = squad1.rage_skill_phase > 0
        is_rage_skill_phase2 = squad2.rage_skill_phase > 0

        # Get the skills for this turn
        skill1 = character1.take_action(is_rage_skill_phase1)
        skill2 = character2.take_action(is_rage_skill_phase2)

        # Get the targets for this turn
        # target_list1 = squad2.get_target(skill1.target_select)
        # target_list2 = squad1.get_target(skill2.target_select)
        target_list1 = self.select_targets(character1, self.squads, skill1)
        target_list2 = self.select_targets(character2, self.squads, skill2)

        # Make them attack each other
        damage1 = self.attack(character1, target_list1, skill1)
        damage2 = self.attack(character2, target_list2, skill2)

        # Handle the rage skill phase and increase rage
        if is_rage_skill_phase1:
            squad1.rage_skill_phase -= 1
            if squad1.rage_skill_phase == 0:
                squad1.end_rage_skill_phase()
        else:
            squad1.increase_rage(character1)
            if squad1.rage >= 100:
                squad1.start_rage_skill_phase()

        if is_rage_skill_phase2:
            squad2.rage_skill_phase -= 1
            if squad2.rage_skill_phase == 0:
                squad2.end_rage_skill_phase()
        else:
            squad2.increase_rage(character2)
            if squad2.rage >= 100:
                squad2.start_rage_skill_phase()

        # Move to the next character in each squad
        squad1.current_character_index = (squad1.current_character_index + 1) % len(squad1.characters)
        squad2.current_character_index = (squad2.current_character_index + 1) % len(squad2.characters)

        # 记录每回合的攻击方、受击方、技能和造成伤害的日志
        self.log.append((self.turn, squad1.name, character1.name, squad2.name,
                         [target.name for target in target_list1], skill1.name, damage1))
        self.log.append((self.turn, squad2.name, character2.name, squad1.name,
                         [target.name for target in target_list2], skill2.name, damage2))

    ## 选择技能释放目标
    # def select_targets(self, character, squads, skill):
    #     if skill.target_type == 'enemy':
    #         target_squads = [squad for squad in squads if squad != character.squad]
    #     elif skill.target_type == 'ally':
    #         target_squads = [character.squad]
    #     # elif skill.target_type == 'self':
    #     else:
    #         target_squads = [character.squad]
    #
    #     if skill.target_area == 'single':
    #         target_list = []
    #         for squad in target_squads:
    #             target_list.extend(squad.characters)
    #         if skill.target_type == 'enemy':
    #             # Select a target from the enemy squad based on the target_select attribute of the skill
    #             if skill.target_select == 'weakest':
    #                 target = [min(target_list, key=lambda character: character.current_health)]
    #             elif skill.target_select == 'strongest':
    #                 target = [max(target_list, key=lambda character: character.current_health)]
    #             else:  # random selection
    #                 target = random.sample(target_list, min(skill.max_targets, len(target_list)))
    #         elif skill.target_type == 'ally':
    #             # Select a target from the ally squad, excluding the attacker
    #             target_list.remove(character)
    #             target = random.sample(target_list, min(skill.max_targets, len(target_list)))
    #         # elif skill.target_type == 'self':
    #         else:
    #             target = [character]
    #         return target
    #     elif skill.target_area == 'multiple':
    #         target_squads = random.sample(target_squads, min(skill.max_targets, len(target_squads)))
    #         target_list = []
    #         for squad in target_squads:
    #             for target in squad.members:
    #                 if target.is_alive():  # only attack alive characters
    #                     target_list.append(target)
    #         return target_list

    # def attack(self, attacker, defender, skill):
    #     if not attacker.is_alive():
    #         return
    #
    #     damage = attacker.calculate_damage(defender, skill.damage_coefficient, skill.base_damage)
    #     # print(f'{attacker.name} attacks {defender.name} for {damage} damage.')
    #     defender.current_health -= damage
    #
    #     if not defender.is_alive():
    #         print(f'{defender.name} is defeated.')
    #
    #     return damage

    # 技能释放
    def attack(self, character, targets, skill):
        total_damage = 0
        for target in targets:
            damage = character.calculate_damage(target, skill_coef=skill.damage_coefficient, skill_base_damage=skill.base_damage)
            target.take_damage(damage)
            total_damage += damage

        return total_damage

    ## 判断战斗是否结束
    def is_over(self):
        return not self.squads[0].is_alive() or not self.squads[1].is_alive()

    # 打印战斗日志
    def print_log(self):
        for turn, squad1, attacker, squad2, defender, skill, damage in self.log:
            print(f"【回合{turn}】部队{squad1} - {attacker} 对部队{squad2} - {defender} 使用了 {skill}，总共造成了 {damage} 点伤害。")

    def get_total_damage_by_squad(self):
        squad_damage = {}
        for _, squad_name, _, _, _, _, damage in self.log:
            if squad_name not in squad_damage:
                squad_damage[squad_name] = damage
            else:
                squad_damage[squad_name] += damage
        return squad_damage

    def get_total_damage_by_character(self):
        character_damage = {}
        for _, squad_name, attacker_name, _, _, _, damage in self.log:
            character_name = squad_name + '-' + attacker_name
            if character_name not in character_damage:
                character_damage[character_name] = damage
            else:
                character_damage[character_name] += damage
        return character_damage

    # def get_next_alive_character(self, squad):
    #     # Find the next alive character in the squad
    #     for i in range(len(squad.characters)):
    #         character = squad.characters[(self.turn + i) % len(squad.characters)]
    #         if character.is_alive():
    #             return character
    #     return None
