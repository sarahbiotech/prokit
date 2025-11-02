import requests
import pandas as pd
from IPython.display import display

class Protein:
    base_url = "https://rest.uniprot.org/uniprotkb/search?query="

    def __init__(self, name, sequence, organism=None):
        self.name = name
        self.sequence = sequence
        self.organism = organism

    @classmethod
    def from_name(cls, name):
        query = name.replace(" ", "+")
        url = f"https://rest.uniprot.org/uniprotkb/search?query={query}&format=json&fields=organism_name,sequence,protein_name"
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Protein '{name}' not found in UniProt.")

        data = response.json()
        if not data.get("results"):
            raise ValueError(f"Protein '{name}' not found in UniProt.")

        entry = data["results"][0]

        # استخراج اسم البروتين
        try:
            protein_name = entry["proteinDescription"]["recommendedName"]["fullName"]["value"]
        except KeyError:
            protein_name = name

        # استخراج التسلسل
        sequence = entry["sequence"]["value"]

        # استخراج اسم الكائن
        organism = entry["organism"]["scientificName"]

        return cls(protein_name, sequence, organism)

    def molecular_weight(self):
        weights = {
            'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
            'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.18,
            'L': 131.18, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
            'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
        }
        return sum(weights.get(aa, 0) for aa in self.sequence)

    def hydrophobic_ratio(self):
        hydrophobic = {'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'}
        return round(sum(1 for aa in self.sequence if aa in hydrophobic) / len(self.sequence), 3)

    def show_summary(self):
        data = {
            "Property": ["Protein Name", "Organism", "Length", "Molecular Weight (Da)", "Hydrophobic Ratio"],
            "Value": [
                self.name,
                self.organism,
                len(self.sequence),
                round(self.molecular_weight(), 2),
                self.hydrophobic_ratio()
            ]
        }
        df = pd.DataFrame(data)
        display(df)

