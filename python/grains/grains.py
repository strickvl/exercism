def square(number):
    if number < 1:
        raise ValueError("number must be one or greater")
    elif number > 64:
        raise ValueError("number can't be greater than 64")

    grains_val = 1
    for _ in range(1, number):
        grains_val = grains_val * 2
    return grains_val

def total():
    return (square(64) * 2) - 1
