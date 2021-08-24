def classify(number):
    if number < 1:
        raise ValueError("number is too low")
    total = 0
    for val in range(1, number):
        if number % val == 0:
            total += val
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    elif total < number:
        return "deficient"
