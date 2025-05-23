class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, dx, dy, grille):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= ny < len(grille.cases) and 0 <= nx < len(grille.cases[0]):
            if not grille.est_mur(nx, ny):
                self.x, self.y = nx, ny
                return True
        return False