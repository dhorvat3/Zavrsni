import pygame
from math import atan2, sin, cos, pi

class metak(object):
    """pf pf"""
    def __init__(self, brzina, tip, toranj, domet, POV, ikona, meta):
        self.POV = POV
        self.brzina = brzina
        self.tip = tip
        self.ishodiste = toranj
        self.TockaAx = self.ishodiste.centerx
        self.TockaAy = self.ishodiste.centery
        self.ikona = ikona
        self.ikonaRect = self.ikona.get_rect()
        self.POV.blit(ikona, self.ishodiste.center)
        self.domet = domet
        self.pocetniPomak = 2
        self.meta = meta
        TockaBx = meta.centerx
        TockaBy = meta.centery
        x = TockaBx - self.TockaAx
        y = TockaBy - self.TockaAy
        self.kut = atan2(y, x) / pi * 180
    def Pomak(self):
        self.TockaAx += cos(self.kut*pi/180) * self.brzina
        self.TockaAy += sin(self.kut*pi/180) * self.brzina

        self.POV.blit(self.ikona, (self.TockaAx, self.TockaAy))
        self.ikonaRect.centerx = self.TockaAx
        self.ikonaRect.centery = self.TockaAy
        if not self.ikonaRect.colliderect(self.domet):
            return -1
        if self.ikonaRect.colliderect(self.meta):
            return 1