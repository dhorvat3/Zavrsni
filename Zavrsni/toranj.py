import pygame
from metak import metak
from math import atan2, pi

class toranj(object):
    """klasa za tornjeve
        ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage, cooldown"""
    def __init__(self, tip, ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage, vrijeme, ikona, pucanj):
        self.Aspeed = ASpeed
        self.poljex = poljex
        self.poljey = poljey
        self.grid = grid
        self.POV = POV;
        self.ikona = ikona
        self.visina = Visina
        self.sirina = Sirina
        self.brojRedova = len(self.grid)
        self.brojStupaca = len(self.grid[0])
        self.tip = tip
        #self.ikona = pygame.Surface((self.visina/self.brojRedova - 20, self.sirina/self.brojStupaca - 20)).convert()
        #self.ikona.fill((20, 150, 30))
        self.ikonaRect = self.ikona.get_rect()
        self.domet = domet
        self.damage = damage
        #self.projektil = None
        self.projektil = []
        self.DometTornja = None
        self.index = -1
        self.pocetno = pygame.time.get_ticks()
        self.cooldown = vrijeme
        self.kut = 0
        self.pucanj = pucanj
    def vratiTip (self):
        return self.tip
    def upgradeDMG(self, iznos):
        self.damage = self.damage + iznos
    def lijevoGore(self, boxx, boxy):
        trecinax = int(self.visina/self.brojRedova)
        trecinay = int(self.sirina/self.brojStupaca)
        lijevo = boxx * trecinax
        gore = boxy * trecinay
        return(lijevo, gore)
    def rot_center(self):
        """rotate an image while keeping its center and size"""
        orig_rect = self.ikona.get_rect()
        rot_image = pygame.transform.rotate(self.ikona, -self.kut)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    def Crtaj (self):
        lijevo, gore = self.lijevoGore(self.poljex, self.poljey)
        self.ikonaRect.x = self.visina/self.brojRedova*(self.poljey)# + 10
        self.ikonaRect.y = self.sirina/self.brojStupaca*(self.poljex)# + 10
        #self.POV.blit(self.ikona, self.ikonaRect)
        self.POV.blit(self.rot_center(), self.ikonaRect)
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
            self.pucanj.play(0)
            neprijatelj = listaNeprijatelja[self.index]
            self.projektil.append(metak(self.Aspeed, "A", self.ikonaRect, self.DometTornja, self.POV, metakIkona, neprijatelj))
        elif self.index > -1:
            neprijatelj = listaNeprijatelja[self.index]
        else:
            neprijatelj = None
        if self.index > -1 and neprijatelj is not None:
            self.kut = atan2(neprijatelj.centery - self.ikonaRect.centery, neprijatelj.centerx - self.ikonaRect.centerx) / pi * 180
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