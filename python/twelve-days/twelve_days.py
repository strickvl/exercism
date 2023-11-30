LIST = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree.",
]

num_to_ordinal = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

def recite(start_verse, end_verse):
    start = f"On the {num_to_ordinal[end_verse - 1]} day of Christmas my true love gave to me: "

    return (
        [start] + ["a Partridge in a Pear Tree."]
        if start_verse == 1
        else [start] + LIST[-start_verse:]
    )
