
Project description

ProKit (Protein Analysis Library)
ProKit is a Python library to fetch and analyze protein sequences from UniProt.
It calculates molecular weight, hydrophobic ratio, and displays results in a neat, organized table.

Installation
Install from PyPI:

pip install prokit from prokit import Protein

Create a Protein object by specifying the protein name
p = Protein.from_name("Hemoglobin subunit beta")

Show summary table:
p.show_summary() # Displays Name, Organism, Length, Molecular Weight, Hydrophobic Ratio

Available Properties and Methods:
Property / Method	Description
p.sequence	Full protein sequence as a string
p.name	Protein name
p.molecular_weight()	Calculates and returns the molecular weight
p.hydrophobic_ratio()	Calculates and returns the fraction of hydrophobic residues.

License:
MIT License – Free to use, modify, and distribute with attribution to the original author.

Author
Sarah Ali – alsayedsarah01@gmail.com
