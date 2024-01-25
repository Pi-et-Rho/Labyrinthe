import pygame
import csv

class Labyrinthe:
    def __init__(self, sizeX: int, sizeY: int, filename: str, color: pygame.Color):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.filename = filename
        self.color = color
        self.matrice = []

    def readFile(self):
        with open(self.filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                row_list = [int(cell) for cell in row]
                self.matrice.append(row_list)

    def drawMap(self, screen, tilesize):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 1:
                    pygame.draw.rect(screen, self.color, pygame.Rect(j * tilesize, i * tilesize, tilesize, tilesize))

    def affiche(self):
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                print(self.matrice[j][i], end="")
            print()

    def afficherMap(self):
        for row in self.matrice:
            print(row)

    def get_matrice(self):
        return self.matrice

    def getXY(self, i, j):
        return self.matrice[j][i]

    def setXY(self, i, j, v):
        self.matrice[j][i] = v

    def getSize(self):
        return self.sizeX, self.sizeY

    def détruire_mur(self, i, j):
        self.matrice[j][i] = 0

# Usage example:
# laby = Labyrinthe(12, 5, 'Map1.csv', pygame.Color('black'))
# laby.readFile()
# laby.afficherMap()
# laby.drawMap(screen, tilesize)  # Call this within your main loop to draw the labyrinth on the screen