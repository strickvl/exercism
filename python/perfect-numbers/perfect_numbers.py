def classify(number):
    if number < 1:
        raise ValueError("number is too low")
    total = sum(val for val in range(1, number) if number % val == 0)
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    elif total < number:
        return "deficient"
