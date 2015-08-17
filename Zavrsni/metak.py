import pygame
from math import hypot

class metak(object):
    """pf pf"""
    def __init__(self, brzina, tip, toranj, domet, POV, ikona):
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

    def Pomak(self, meta):
        TockaBx = meta.centerx
        TockaBy = meta.centery

        if TockaBx < self.TockaAx:
            self.TockaAx -= self.brzina
        elif TockaBx > self.TockaAx:
            self.TockaAx += self.brzina

        if TockaBy < self.TockaAy:
            self.TockaAy -= self.brzina
        elif TockaBy > self.TockaAy:
            self.TockaAy += self.brzina

        self.POV.blit(self.ikona, (self.TockaAx, self.TockaAy))
        self.ikonaRect.centerx = self.TockaAx
        self.ikonaRect.centery = self.TockaAy
        if not self.ikonaRect.colliderect(self.domet):
            return -1
        if self.ikonaRect.colliderect(meta):
            return 1