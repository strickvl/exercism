def convert(number):
    FACTORS_TO_SOUNDS = {
        3: "Pling"
        }
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result += str(number)
    return result
