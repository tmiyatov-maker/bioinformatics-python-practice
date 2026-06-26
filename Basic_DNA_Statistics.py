"""
Practice Problem: Basic DNA Statistics

Description:
Calculates length, GC content, purine count, pyrimidine count,
and purine percentage for a DNA sequence.

Concepts:
- Counts
- Percentages
- Basic biological categories
"""

dna = "ATCGATCG"

length = len(dna)
gc_content = (dna.count("G") + dna.count("C")) / length * 100
purines = dna.count("A") + dna.count("G")
pyrimidines = dna.count("C") + dna.count("T")
purine_percentage = purines / length * 100

print("Length:", length)
print("GC content:", round(gc_content, 2), "%")
print("Purines:", purines)
print("Pyrimidines:", pyrimidines)
print("Purine percentage:", round(purine_percentage, 2), "%")
