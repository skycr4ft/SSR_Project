import random


class Squad:

    def __init__(self, name, characters, alliance):
        if not 1 <= len(characters) <= 3:
            raise ValueError('A squad must have 1 to 3 characters')
        self.name = name
        self.characters = characters
        while len(characters) < 3:
            self.characters.append(None)
        self.rage = 0
        self.rage_skill_phase = 0
        self.current_character_index = 0
        self.alliance = alliance
        self.skill_cast_time = 0
        for character in self.characters:
            character.squad = self

    def is_alive(self):
        return any(character.is_alive() for character in self.characters)

    def increase_rage(self, rage_increase):
        self.rage += rage_increase

    def start_rage_skill_phase(self):
        self.rage_skill_phase = 3
        self.current_character_index = 0  # Reset the character index
        self.skill_cast_time += 1

    def end_rage_skill_phase(self):
        self.rage_skill_phase = 0
        self.rage = 0
        self.current_character_index = 0  # Reset the character index

    def get_next_alive_character(self):
        # Find the next alive character in the squad
        for i in range(len(self.characters)):
            character = self.characters[(self.current_character_index + i) % len(self.characters)]
            if character.is_alive():
                self.current_character_index = (self.current_character_index + i + 1) % len(self.characters)
                return character
        return None

    def get_next_character(self):
        # if self.rage_skill_phase > 0:
        #     # If the squad is in the rage skill phase, return the character at the current index
        #     return self.characters[self.current_character_index]
        # else:
        #     # If the squad is not in the rage skill phase, return the next alive character
        #     for i in range(len(self.characters)):
        #         character = self.characters[(self.current_character_index + i) % len(self.characters)]
        #         if character.is_alive():
        #             return character
        if not self.characters[self.current_character_index].is_alive():
            return None
        return self.characters[self.current_character_index]

    # Add more methods as needed for your game mechanics
