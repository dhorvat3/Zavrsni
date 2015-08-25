import pygame
from metak import metak

class toranj(object):
    """klasa za tornjeve
        ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage, cooldown"""
    def __init__(self, ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage, vrijeme):
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
        #self.projektil = None
        self.projektil = []
        self.DometTornja = None
        self.index = -1
        self.pocetno = pygame.time.get_ticks()
        self.cooldown = vrijeme
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
    def vrijeme(self):
        trenutno = pygame.time.get_ticks()
        if trenutno - self.pocetno >= self.cooldown:
            self.pocetno = trenutno
            return 1
    def Ciljanje (self, neprijatelji, metakIkona):
        listaNeprijatelja = neprijatelji
        dmgLista = []
        status = -3
        tmpIndex = self.DometTornja.collidelist(listaNeprijatelja)
        if not self.index == tmpIndex:
            self.index = tmpIndex
        if self.index > -1 and self.vrijeme(): #and self.projektil is None:
            neprijatelj = listaNeprijatelja[self.index]
            self.projektil.append(metak(self.Aspeed, "A", self.ikonaRect, self.DometTornja, self.POV, metakIkona, neprijatelj))
        if not self.projektil == []:
            for i in self.projektil[:]:
                status = i.Pomak(listaNeprijatelja)
                if status > -1:
                    print ("Status: ", status)
                    self.projektil.remove(i)
                    dmgLista.append([status, self.damage])
                elif status == -2:
                    self.index = -1
                    self.projektil.remove(i)
                    dmgLista.append([-1, 0])
                else:
                    dmgLista.append([-1, 0])
        else:
            dmgLista.append([-1, 0])
        return dmgLista