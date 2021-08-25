import re

class PhoneNumber:
    def __init__(self, number: str):
        self.number = re.sub(r'[^0-9]', "", number)
        if len(self.number) == 1 and self.number[0] == "1":
            self.number = self.number[1:]
        if len(self.number) != 10:
            raise ValueError("this is an invalid number")

        self.area_code = self.number[0:3]
        if self.area_code[0] == "0" or self.area_code[0] == "1":
            raise ValueError("area code can't start with a value less than 2")
