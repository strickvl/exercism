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
    result = []
    for startidx in range(0, len(strand), 3):
        codon = strand[startidx:startidx + 3]
        if codon in STOP_CODONS:
            return result
        else:
            result.append(CODON_TO_PROTEIN[codon])
    return result
