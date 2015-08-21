import pygame
from metak import metak

class toranj(object):
    """klasa za tornjeve
        ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage"""
    def __init__(self, ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage):
        self.Aspeed = ASpeed
        self.poljex = poljex
        self.poljey = poljey
        self.grid = grid
        self.POV = POV;
        self.visina = Visina
        self.sirina = Sirina
        self.brojRedova = len(self.grid)
        self.brojStupaca = len(self.grid[0])
        self.ikona = pygame.Surface((self.visina/self.brojRedova - 20, self.sirina/self.brojStupaca - 20)).convert()
        self.ikona.fill((20, 150, 30))
        self.ikonaRect = self.ikona.get_rect()
        self.domet = domet
        self.damage = damage
        self.projektil = None
        self.DometTornja = None
        self.index = -1
    def lijevoGore(self, boxx, boxy):
        trecinax = int(self.visina/self.brojRedova)
        trecinay = int(self.sirina/self.brojStupaca)
        lijevo = boxx * trecinax
        gore = boxy * trecinay
        return(lijevo, gore)
    def Crtaj (self):
        lijevo, gore = self.lijevoGore(self.poljex, self.poljey)
        self.ikonaRect.x = self.visina/self.brojRedova*(self.poljey) + 10
        self.ikonaRect.y = self.sirina/self.brojStupaca*(self.poljex) + 10
        self.POV.blit(self.ikona, self.ikonaRect)
        self.DometTornja = self.ikonaRect.copy()
        self.DometTornja = self.DometTornja.inflate(self.domet, self.domet);
        #Crtanje kvadrata s alpha vrijednostima
        s = pygame.Surface((self.DometTornja.right - self.DometTornja.left, self.DometTornja.bottom - self.DometTornja.top))  # the size of your rect
        s.set_alpha(70)                # alpha level
        s.fill((84,48,15))           # this fills the entire surface
        self.POV.blit(s, (self.DometTornja.left,self.DometTornja.top))    # (0,0) are the top-left coordinates
    def Ciljanje (self, neprijatelji, metakIkona):
        listaNeprijatelja = neprijatelji
        status = 0
        tmpIndex = self.DometTornja.collidelist(listaNeprijatelja)
        if not self.index == tmpIndex:
            self.projektil = None
            self.index = tmpIndex
        if self.index > -1 and self.projektil is None:
            neprijatelj = listaNeprijatelja[self.index]
            self.projektil = metak(3, "A", self.ikonaRect, self.DometTornja, self.POV, metakIkona, neprijatelj)
        if self.projektil is not None:
            status = self.projektil.Pomak()
        if status == 1:
            print ("Status: ", status)
            self.projektil = None
            ind = self.index
            self.index = -1
            return ind, self.damage
        elif status == -1:
            self.index = -1
            self.projektil = None
            return -1, 0
        else:
            return -1, 0