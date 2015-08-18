import pygame

class sucelje(object):
    """Definiranje korisniskog su?elja"""
    def __init__(self, visina, sirina, POV, ikonaHover, ikonaLvl1, ikonaLvl2, ikonaLvl3):
        self.visina = visina
        self.sirina = sirina
        self.brojRedova = 0
        self.brojStupaca = 0
        self.mapa = None
        self.POVRSINA = POV
        self.font = pygame.font.SysFont("monospace", 15)
        self.pare = 0
        self.toranj1Rect = None
        self.toranj2Rect = None
        self.toranj3Rect = None
        self.menuHover = ikonaHover
        self.menuLvl1 = ikonaLvl1
        self.Lvl1Rect = self.menuLvl1.get_rect()
        self.menuLvl2 = ikonaLvl2
        self.Lvl2Rect = self.menuLvl2.get_rect()
        self.menuLvl3 = ikonaLvl3
        self.Lvl3Rect = self.menuLvl3.get_rect()
    def lijevoGore(self, boxx, boxy):
        trecinax = int(self.visina/self.brojRedova)
        trecinay = int(self.sirina/self.brojStupaca)

        lijevo = boxx * trecinax
        gore = boxy * trecinay
        return(lijevo, gore)

    def poljeNaPixelu(self, x, y):
        for boxx in range(self.brojRedova):
            for boxy in range(self.brojStupaca):
                lijevo, gore = self.lijevoGore(boxx, boxy)
                boxRect = pygame.Rect(lijevo, gore, self.visina/self.brojRedova - 2, self.sirina/self.brojStupaca - 2)
                if boxRect.collidepoint(x, y):
                    return(boxx, boxy)
        return(None, None)
    def crtajObrub(self, x, y, hover):
        poljex, poljey = self.poljeNaPixelu(x, y)
        if poljex != None and poljey != None and self.mapa[poljey][poljex] != 'Z':
            lijevo, gore = self.lijevoGore(poljex, poljey)
            pygame.draw.rect(self.POVRSINA, (60,  60, 100), (lijevo, gore, self.visina/self.brojRedova, self.sirina/self.brojStupaca), 3)
        elif x is not None and y is not None and self.toranj1Rect is not None and self.toranj2Rect is not None and self.toranj3Rect is not None:
           if self.toranj1Rect.collidepoint(x, y):
                self.POVRSINA.blit(hover, self.toranj1Rect)
           elif self.toranj2Rect.collidepoint(x, y):
                self.POVRSINA.blit(hover, self.toranj2Rect)
           elif self.toranj3Rect.collidepoint(x, y):
               self.POVRSINA.blit(hover, self.toranj3Rect)
    def odabraniToranj(self, x, y, odabrano):
        if self.toranj1Rect.collidepoint(x, y):
            self.POVRSINA.blit(odabrano, self.toranj1Rect)
            return 'Toranj1'
        if self.toranj2Rect.collidepoint(x, y):
            self.POVRSINA.blit(odabrano, self.toranj2Rect)
            return 'Toranj2'
        if self.toranj3Rect.collidepoint(x, y):
            self.POVRSINA.blit(odabrano, self.toranj3Rect)
            return 'Toranj3'
    def pozadina(self, odabrano, slika):
        if odabrano == 'Toranj1':
            toranjRect = self.toranj1Rect
        if odabrano == 'Toranj2':
            toranjRect = self.toranj2Rect
        if odabrano == 'Toranj3':
            toranjRect = self.toranj3Rect
        self.POVRSINA.blit(slika, toranjRect)
    def crtajGlavniMenu(self):
        self.Lvl1Rect.x = 100
        self.Lvl1Rect.y = 50
        self.Lvl2Rect.x = 100
        self.Lvl2Rect.y = 50 + 70 + 20
        self.Lvl3Rect.x = 100
        self.Lvl3Rect.y = 50 + 70 + 20 + 70 + 20
        self.POVRSINA.blit(self.menuLvl1, self.Lvl1Rect)
        self.POVRSINA.blit(self.menuLvl2, self.Lvl2Rect)
        self.POVRSINA.blit(self.menuLvl3, self.Lvl3Rect)
    def hoverGlavniMenu(self, x, y):
        if self.Lvl1Rect.collidepoint(x, y):
            self.POVRSINA.blit(self.menuHover, self.Lvl1Rect)
        elif self.Lvl2Rect.collidepoint(x, y):
            self.POVRSINA.blit(self.menuHover, self.Lvl2Rect)
        elif self.Lvl3Rect.collidepoint(x, y):
            self.POVRSINA.blit(self.menuHover, self.Lvl3Rect)
    def kliknutoGlavniMenu(self, x, y):
        if self.Lvl1Rect.collidepoint(x, y):
            return 'Lvl1'
        else:
            return None
    def menu(self, slikaObrub, slikaToranj1, slikaToranj2, slikaToranj3):
        #obrub
        slikaRect = slikaObrub.get_rect()
        slikaRect.x = 640
        slikaRect.y = 0
        self.POVRSINA.blit(slikaObrub, slikaRect)
        #toranj1
        self.toranj1Rect = slikaToranj1.get_rect()
        self.toranj1Rect.x = 640 + 30
        self.toranj1Rect.y = 50
        self.POVRSINA.blit(slikaToranj1, self.toranj1Rect)
        #toranj2
        self.toranj2Rect = slikaToranj2.get_rect()
        self.toranj2Rect.x = 640 + 30
        self.toranj2Rect.y = 98
        self.POVRSINA.blit(slikaToranj2, self.toranj2Rect)
        #toranj3
        self.toranj3Rect = slikaToranj3.get_rect()
        self.toranj3Rect.x = 640 + 30
        self.toranj3Rect.y = 146
        self.POVRSINA.blit(slikaToranj3, self.toranj3Rect)
    def azurirajNovce (self, vrijednost):
        self.pare = self.pare + vrijednost
    def vratiNovce (sefl):
        return sefl.pare
    def ispisStanja(self, HP):
        lblHP = self.font.render(("Player HP: " + str(HP[0]) + "/" + str(HP[1])), 1, (254, 158, 154))
        self.POVRSINA.blit(lblHP, (640 + 30, 5))
        lblNovci = self.font.render(("Stanje: " + str(self.pare)), 1, (254, 158, 18))
        self.POVRSINA.blit(lblNovci, (640 + 30, 20))
    def postaviMrezu(self, mreza):
        self.mapa = mreza
        self.brojRedova = len(self.mapa)
        self.brojStupaca = len(self.mapa[0])
    def postaviNovce(self, novci):
        self.pare = novci