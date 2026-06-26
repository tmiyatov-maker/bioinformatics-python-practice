"""
Rosalind Problem: PROT - Translating RNA into Protein

Description:
Translates an RNA sequence into a protein sequence using a codon table.

Concepts:
- Dictionaries
- Codons
- Loops with step size 3
- Stop codons
"""

rna = "AUGGCCUAA"

codon_table = {
    "AUG": "M",
    "GCC": "A",
    "UAA": "Stop"
}

protein = ""

for i in range(0, len(rna), 3):
    codon = rna[i:i + 3]
    amino_acid = codon_table[codon]

    if amino_acid == "Stop":
        break

    protein += amino_acid

print(protein)
