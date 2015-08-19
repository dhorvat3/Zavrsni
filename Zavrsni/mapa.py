import pygame

class Mapa(object):
    """Klasa objekta mapa"""
    def __init__(self, polje, visina, sirina):
        '''Stvaranje objekta mape, uzma polje po kojem generira mapu s obzirom na rezoluciju ekrana'''
        self.grid = polje
        self.brojRedova = len(self.grid)
        self.brojStupaca = len(self.grid[0])
        print(self.brojRedova, self.brojStupaca)
        self.ekranVisina = visina
        self.ekranSirina = sirina
    def crtajMrezu (self, POV):
        '''Crta mapu'''
        dimX = int(self.ekranVisina/self.brojRedova)
        dimY = int(self.ekranSirina/self.brojStupaca)
        for i in range(self.brojRedova):
            for j in range(self.brojStupaca):
                if self.grid[i][j] == 'S' or self.grid[i][j] == 'D' or self.grid[i][j] == 'L' or self.grid[i][j] == 'T':
                    pygame.draw.rect(POV, (255, 15, 0), (dimX * j, dimY * i, dimX, dimY), 1)