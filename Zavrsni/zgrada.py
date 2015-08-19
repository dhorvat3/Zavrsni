import pygame

class zgrada(object):
    """Klasa glavne zgrade"""
    def __init__(self, POV, ikona, MAXhp, pozicija, visina, sirina, grid):
        self.POV = POV
        self.pozicija = pozicija
        self.ikona = ikona
        self.ikonaRect = self.ikona.get_rect()
        self.visina = visina
        self.sirina = sirina
        self.brojRedova = len(grid)
        self.brojStupaca = len(grid[0])
        self.ikonaRect.x = self.visina/self.brojRedova*(self.pozicija[1]) + 5
        self.ikonaRect.y = self.sirina/self.brojStupaca*(self.pozicija[0]) + 5
        self.POV.blit(self.ikona, self.ikonaRect.topleft)
        self.maxHP = MAXhp
        self.trenutniHP = MAXhp
    def crtaj(self):
        self.POV.blit(self.ikona, self.ikonaRect.topleft)
    def damage (self, neprijatelji):
        listaNeprijatelja = neprijatelji
        index = self.ikonaRect.collidelist(listaNeprijatelja)
        if index > -1:
            self.trenutniHP = self.trenutniHP - 1
            return index
        else:
            return -1
    def vratiHP(self):
        return self.trenutniHP, self.maxHP