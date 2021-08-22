CODON_TO_PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

STOP_CODONS = ["UAA", "UAG", "UGA"]

def proteins(strand):
    startidx = 0
    result = []
    while startidx < len(strand):
        codon = strand[startidx:startidx + 3]
        if codon in STOP_CODONS:
            return result
        else:
            result.append(CODON_TO_PROTEIN[codon])
        startidx += 3
    return result
