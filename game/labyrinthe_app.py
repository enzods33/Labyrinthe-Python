import tkinter as tk
from game.grille import Grille
from game.joueur import Joueur

CELL_SIZE = 40

class LabyrintheApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Labyrinthe - Tkinter")

        # Grille et joueur
        self.grille = Grille.from_file("labyrinthe.txt")  # ou .from_lignes([...])
        self.joueur = Joueur(*self.grille.trouver_joueur())

        # Canvas
        largeur = len(self.grille.cases[0]) * CELL_SIZE
        hauteur = len(self.grille.cases) * CELL_SIZE
        self.canvas = tk.Canvas(root, width=largeur, height=hauteur)
        self.canvas.pack()

        self.dessiner_labyrinthe()

        # Contrôles clavier
        self.root.bind("<Up>",    lambda e: self.deplacer(0, -1))
        self.root.bind("<Down>",  lambda e: self.deplacer(0, 1))
        self.root.bind("<Left>",  lambda e: self.deplacer(-1, 0))
        self.root.bind("<Right>", lambda e: self.deplacer(1, 0))

    def deplacer(self, dx, dy):
        if self.joueur.deplacer(dx, dy, self.grille):
            self.dessiner_labyrinthe()
            if self.grille.est_sortie(self.joueur.x, self.joueur.y):
                print("🎉 Bravo, tu as gagné !")
                self.afficher_victoire()

    def dessiner_labyrinthe(self):
        self.canvas.delete("all")
        for y, ligne in enumerate(self.grille.cases):
            for x, char in enumerate(ligne):
                x1, y1 = x * CELL_SIZE, y * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                couleur = {
                    "#": "black",
                    "S": "green",
                }.get(char, "white")
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur)

        # Dessin du joueur
        x, y = self.joueur.x, self.joueur.y
        x1, y1 = x * CELL_SIZE + 5, y * CELL_SIZE + 5
        x2, y2 = x1 + CELL_SIZE - 10, y1 + CELL_SIZE - 10
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue")