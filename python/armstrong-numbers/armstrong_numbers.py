def is_armstrong_number(number):
    string_num = str(number)
    total = 0
    for char in string_num:
        total += int(char) ** len(string_num)
    return total == number
