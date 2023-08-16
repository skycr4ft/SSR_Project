import random


class Squad:

    def __init__(self, name, characters, alliance):
        if not 1 <= len(characters) <= 3:
            raise ValueError('A squad must have 1 to 3 characters')
        self.name = name
        self.characters = characters
        self.rage = 0
        self.rage_skill_phase = 0
        self.current_character_index = 0
        self.alliance = alliance
        for character in self.characters:
            character.squad = self

    def is_alive(self):
        return any(character.is_alive() for character in self.characters)

    def increase_rage(self, character):
        self.rage += character.rage_increase

    def start_rage_skill_phase(self):
        self.rage_skill_phase = len(self.characters)
        self.current_character_index = 0  # Reset the character index

    def end_rage_skill_phase(self):
        self.rage_skill_phase = 0
        self.rage = 0
        self.current_character_index = 0  # Reset the character index

    def get_next_alive_character(self):
        # Find the next alive character in the squad
        for i in range(len(self.characters)):
            character = self.characters[(self.current_character_index + i) % len(self.characters)]
            if character.is_alive():
                self.current_character_index = (self.current_character_index + i) % len(self.characters)
                return character
        return None

    # def get_target(self, target_select):
    #     if target_select == 'random':
    #         # Choose a random character as the target
    #         return random.choice([character for character in self.characters if character.is_alive()])
    #     elif target_select == 'weakest':
    #         # Choose the character with the lowest current health as the target
    #         return min((character for character in self.characters if character.is_alive()),
    #                    key=lambda character: character.current_health)
    #     else:
    #         raise ValueError(f'Unknown target selection method: {target_select}')

    # Add more methods as needed for your game mechanics
