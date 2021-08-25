def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("the two strings must be of equal length")

    hamming_val = 0
    for idx in range(len(strand_a)):
        if (strand_a[idx] != strand_b[idx]):
            hamming_val += 1

    return hamming_val
