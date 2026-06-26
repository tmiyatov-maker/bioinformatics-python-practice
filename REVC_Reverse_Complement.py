"""
Rosalind Problem: REVC - Reverse Complement

Description:
Generates the reverse complement of a DNA sequence.

Concepts:
- Dictionaries
- reversed()
- join()
- DNA base pairing
"""

dna = "AAAACCCGGT"

complement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

reverse_complement = "".join(complement[base] for base in reversed(dna))

print(reverse_complement)
