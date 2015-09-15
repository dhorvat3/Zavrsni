import pygame
from metak import metak
from math import atan2, pi

class toranj(object):
    """klasa za tornjeve
        tip, ASpeed, poljex, poljey, grid, POV, Visina, Sirina, domet, damage, cooldown, ikona, pucanj"""
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
        self.ikonaRect = self.ikona.get_rect()
        self.domet = domet
        self.damage = damage
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
        if self.tip == 4:
            self.POV.blit(self.ikona, self.ikonaRect)
        else:
            self.POV.blit(self.rot_center(), self.ikonaRect)
        self.DometTornja = self.ikonaRect.copy()
        self.DometTornja = self.DometTornja.inflate(self.domet, self.domet);
        #Crtanje kvadrata s alpha vrijednostima
        s = pygame.Surface((self.DometTornja.right - self.DometTornja.left, self.DometTornja.bottom - self.DometTornja.top))  # the size of your rect
        s.set_alpha(30)                # alpha level
        if self.tip == 1:
            s.fill((56,195,255))           # this fills the entire surface
        elif self.tip == 2:
            s.fill((143,255,70))
        elif self.tip == 3:
            s.fill((255,85,85))
        elif self.tip == 4:
            s.fill((251,36,173))
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
        if self.index > -1 and self.vrijeme():
            self.pucanj.play(0)
            neprijatelj = listaNeprijatelja[self.index]
            self.projektil.append(metak(self.Aspeed, "A", self.ikonaRect, self.DometTornja, self.POV, metakIkona, neprijatelj))
        elif self.index > -1:
            neprijatelj = listaNeprijatelja[self.index]
        else:
            neprijatelj = None
        if self.index > -1 and neprijatelj is not None:
            if self.tip == 4:
                pygame.draw.line(self.POV, (255, 0, 0), self.ikonaRect.center, neprijatelj.center, 1)
            self.kut = atan2(neprijatelj.centery - self.ikonaRect.centery, neprijatelj.centerx - self.ikonaRect.centerx) / pi * 180
        if not self.projektil == []:
            for i in self.projektil[:]:
                status = i.Pomak(listaNeprijatelja)
                if status > -1:
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