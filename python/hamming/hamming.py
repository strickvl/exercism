def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("the two strings must be of equal length")

    inconsistent_elements = [1 for val in range(len(strand_a)) if strand_a[val] != strand_b[val]]

    return sum(inconsistent_elements)
