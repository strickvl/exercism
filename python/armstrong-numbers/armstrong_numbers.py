def is_armstrong_number(number):
    string_num = str(number)
    total = sum(int(char) ** len(string_num) for char in string_num)
    return total == number
