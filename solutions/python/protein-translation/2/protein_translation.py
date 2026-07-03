codon_to_protein = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}

def proteins(strand):
    rna_segment = [ strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []
    for segment in rna_segment:
        if codon_to_protein[segment] == 'STOP':
            return result
        result.append(codon_to_protein[segment])
    return result
        
