class Grille:
    def __init__(self, cases):
        self.cases = cases  # liste de listes de caractères

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, "r") as f:
            lignes = [list(line.strip()) for line in f if line.strip()]
        return cls(lignes)

    def get(self, x, y):
        return self.cases[y][x]

    def est_mur(self, x, y):
        return self.get(x, y) == "#"

    def est_sortie(self, x, y):
        return self.get(x, y) == "S"

    def trouver_joueur(self):
        for y, ligne in enumerate(self.cases):
            for x, case in enumerate(ligne):
                if case == "P":
                    return x, y
        raise ValueError("Position de départ (P) non trouvée dans la grille.")