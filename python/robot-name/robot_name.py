import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

class Robot:
    assigned_names = []

    def __init__(self):
        self.name = self.generate_new_name()
        Robot.assigned_names.append(self.name)

    def generate_new_name(self):
        letters = "".join(random.choices(LETTERS, k=2))
        numbers = "".join(random.choices(NUMBERS, k=3))
        new_name = letters + numbers
        while new_name in Robot.assigned_names:
            new_name = self.generate_new_name()

        return new_name

    def reset(self):
        self.name = self.generate_new_name()
        Robot.assigned_names.append(self.name)
