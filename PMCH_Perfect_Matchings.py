"""
Rosalind Problem: PMCH - Perfect Matchings and RNA Secondary Structures

Description:
Calculates the number of perfect base-pair matchings in an RNA string.

Concepts:
- Factorials
- Combinatorics
- RNA base pairing
"""

from math import factorial

rna = "AGCUAGUCAU"

answer = factorial(rna.count("A")) * factorial(rna.count("C"))

print(answer)
