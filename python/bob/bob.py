import re

def response(hey_bob):
    transformed = re.sub(r'[^a-zA-Z\?]', "", hey_bob)
    if transformed.isspace():
        return "Fine. Be that way!"
    elif hey_bob == hey_bob.upper() and hey_bob.rstrip()[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob.rstrip()[-1] == "?":
        return "Sure."
    elif hey_bob == hey_bob.upper() and :
        return "Whoa, chill out!"
    else:
        return "Whatever."

print(response("1, 2, 3"))
