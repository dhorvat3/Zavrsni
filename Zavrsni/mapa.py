import pygame

class Mapa(object):
    """Klasa objekta mapa"""
    def __init__(self, polje, visina, sirina, okolis, put_ravno, put_dole, put_kutLD, put_kut_DD):
        '''Stvaranje objekta mape, uzma polje po kojem generira mapu s obzirom na rezoluciju ekrana'''
        self.grid = polje
        self.brojRedova = len(self.grid)
        self.brojStupaca = len(self.grid[0])
        print(self.brojRedova, self.brojStupaca)
        self.ekranVisina = visina
        self.ekranSirina = sirina
        self.okolis = okolis
        self.okolisRect = self.okolis.get_rect()
        self.put_ravno = put_ravno
        self.put_dole = put_dole
        self.put_kutLD = put_kutLD
        self.put_kutDD = put_kut_DD
        self.put_kutDG = pygame.transform.rotate(self.put_kutDD, 180)
        self.put_kutGD = pygame.transform.rotate(self.put_kutLD, 180)
        self.putRect = self.put_ravno.get_rect()
    def crtajMrezu (self, POV):
        '''Crta mapu'''
        dimX = int(self.ekranVisina/self.brojRedova)
        dimY = int(self.ekranSirina/self.brojStupaca)
        for i in range(self.brojRedova):
            for j in range(self.brojStupaca):
                if self.grid[i][j] == 'S' or self.grid[i][j] == 'D' or self.grid[i][j] == 'L' or self.grid[i][j] == 'T':
                    self.okolisRect.x = dimX * j
                    self.okolisRect.y = dimY * i
                    POV.blit(self.okolis, self.okolisRect)
                    #pygame.draw.rect(POV, (255, 15, 0), (dimX * j, dimY * i, dimX, dimY), 1)
                else:
                    self.putRect.x = dimX * j
                    self.putRect.y = dimY * i
                    if i > 0 and i < 9:
                        if self.grid[i + 1][j] == 'Z' or self.grid[i - 1][j] == 'Z':
                            POV.blit(self.put_dole, self.putRect)
                    if j > 0 and j < 9:
                        if self.grid[i][j + 1] == 'Z' or self.grid[i][j - 1] == 'Z':
                            POV.blit(self.put_ravno, self.putRect)
                    if i < 9 and j > 0:
                        if self.grid[i + 1][j] == 'Z' and self.grid[i][j - 1] == 'Z':
                            POV.blit(self.put_kutLD, self.putRect)
                    if i > 0 and j < 9:
                        if self.grid[i - 1][j] == 'Z' and self.grid[i][j + 1] == 'Z':
                            POV.blit(self.put_kutGD, self.putRect)
                    if i > 0 and j > 0:
                        if self.grid[i - 1][j] == 'Z' and self.grid[i][j - 1] == 'Z':
                            POV.blit(self.put_kutDG, self.putRect)
                    if i < 9 and j < 9:
                        if self.grid[i + 1][j] == 'Z' and self.grid[i][j + 1] == 'Z':
                            POV.blit(self.put_kutDD, self.putRect)
