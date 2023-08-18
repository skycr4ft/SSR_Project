class Attribute:
    def __init__(self, base_value):
        self.base_value = base_value
        self.fixed_bonus = 0
        self.percentage_bonus = 0

    @property
    def final_value(self):
        return self.base_value + self.fixed_bonus + self.base_value * self.percentage_bonus