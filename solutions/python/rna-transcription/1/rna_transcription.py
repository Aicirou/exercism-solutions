def to_rna(dna_strand):
    rna_strand = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    return ''.join(rna_strand[strnd] for strnd in dna_strand)
