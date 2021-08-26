import re

def is_isogram(string: str) -> bool:
    chars = re.sub(r'[^a-zA-Z]', '', string).lower()
    char_counts = {}
    for char in chars:
        if char in char_counts:
            return False
        else:
            char_counts[char] = True

    return True
