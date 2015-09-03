import pygame

class sucelje(object):
    """Definiranje korisniskog su?elja"""
    def __init__(self, visina, sirina, POV, ikonaHover, ikonaLvl1, ikonaLvl2, ikonaLvl3, ikonaGlavni, ikonaPredjen, upgradeHover, startHover):
        self.visina = visina
        self.sirina = sirina
        self.brojRedova = 0
        self.brojStupaca = 0
        self.mapa = None
        self.POVRSINA = POV
        self.font = pygame.font.SysFont("monospace", 15)
        self.fontDMG = pygame.font.SysFont("tahoma", 10)
        self.pare = 0
        self.toranj1Rect = None
        self.toranj1_uRect = None
        self.toranj2Rect = None
        self.toranj2_uRect = None
        self.toranj3Rect = None
        self.toranj3_uRect = None
        self.snajperRect = None
        self.snajper_uRect = None
        self.mitraljezRect = None
        self.mitraljez_uRect = None
        self.startRect = None
        self.ikonaStart_H = startHover
        self.upgradeHover = upgradeHover
        self.menuHover = ikonaHover
        self.menuLvl1 = ikonaLvl1
        self.Lvl1Rect = self.menuLvl1.get_rect()
        self.menuLvl2 = ikonaLvl2
        self.Lvl2Rect = self.menuLvl2.get_rect()
        self.menuLvl3 = ikonaLvl3
        self.Lvl3Rect = self.menuLvl3.get_rect()
        self.ikonaGlavni = ikonaGlavni
        self.ikonaGlavniRect = self.ikonaGlavni.get_rect()
        self.ikonaPredjen = ikonaPredjen
        self.ikonaPredjenRect = self.ikonaPredjen.get_rect()
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
        elif x is not None and y is not None \
            and self.toranj1Rect is not None \
            and self.toranj2Rect is not None \
            and self.toranj3Rect is not None \
            and self.toranj1_uRect is not None \
            and self.toranj2_uRect is not None \
            and self.toranj3_uRect is not None \
            and self.snajperRect is not None \
            and self.snajper_uRect is not None \
            and self.mitraljezRect is not None \
            and self.mitraljez_uRect is not None \
            and self.startRect is not None:
           if self.toranj1_uRect.collidepoint(x, y):
               self.POVRSINA.blit (self.upgradeHover, self.toranj1_uRect)
           elif self.toranj2_uRect.collidepoint(x, y):
               self.POVRSINA.blit(self.upgradeHover, self.toranj2_uRect)
           elif self.toranj3_uRect.collidepoint(x, y):
               self.POVRSINA.blit(self.upgradeHover, self.toranj3_uRect)
           elif self.snajper_uRect.collidepoint(x, y):
               self.POVRSINA.blit(self.upgradeHover, self.snajper_uRect)
           elif self.mitraljez_uRect.collidepoint(x, y):
               self.POVRSINA.blit(self.upgradeHover, self.mitraljez_uRect)
           if self.toranj1Rect.collidepoint(x, y):
                self.POVRSINA.blit(hover, self.toranj1Rect)
           elif self.toranj2Rect.collidepoint(x, y):
                self.POVRSINA.blit(hover, self.toranj2Rect)
           elif self.toranj3Rect.collidepoint(x, y):
               self.POVRSINA.blit(hover, self.toranj3Rect)
           elif self.snajperRect.collidepoint(x, y):
               self.POVRSINA.blit(hover, self.snajperRect)
           elif self.mitraljezRect.collidepoint(x, y):
               self.POVRSINA.blit(hover, self.mitraljezRect)
           elif self.startRect.collidepoint(x, y):
               self.POVRSINA.blit(self.ikonaStart_H, self.startRect)
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
        if self.snajperRect.collidepoint(x, y):
            self.POVRSINA.blit(odabrano, self.snajperRect)
            return 'Toranj4'
        if self.mitraljezRect.collidepoint(x, y):
            self.POVRSINA.blit(odabrano, self.mitraljezRect)
            return 'Toranj5'
    def odabraniUpgrade(self, x, y):
        if self.toranj1_uRect.collidepoint(x, y):
            self.POVRSINA.blit(self.upgradeHover, self.toranj1_uRect)
            return 'Upgrade1'
        if self.toranj2_uRect.collidepoint(x, y):
            self.POVRSINA.blit(self.upgradeHover, self.toranj2_uRect)
            return 'Upgrade2'
        if self.toranj3_uRect.collidepoint(x, y):
            self.POVRSINA.blit(self.upgradeHover, self.toranj3_uRect)
            return 'Upgrade3'
        if self.snajper_uRect.collidepoint(x, y):
            self.POVRSINA.blit(self.upgradeHover, self.snajper_uRect)
            return 'Upgrade4'
        if self.mitraljez_uRect.collidepoint(x, y):
            self.POVRSINA.blit(self.upgradeHover, self.mitraljez_uRect)
            return 'Upgrade5'
    def pozadina(self, odabrano, slika):
        if odabrano == 'Toranj1':
            toranjRect = self.toranj1Rect
        if odabrano == 'Toranj2':
            toranjRect = self.toranj2Rect
        if odabrano == 'Toranj3':
            toranjRect = self.toranj3Rect
        if odabrano == 'Toranj4':
            toranjRect = self.snajperRect
        if odabrano == 'Toranj5':
            toranjRect = self.mitraljezRect 
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
        elif self.Lvl2Rect.collidepoint(x, y):
            return 'Lvl2'
        elif self.Lvl3Rect.collidepoint(x, y):
            return 'Lvl3'
        else:
            return None
    def menu(self, slikaObrub, slikaToranj1, slikaToranj2, slikaToranj3, slikaSnajper, slikaMitraljez, \
        toranj1_u, toranj2_u, toranj3_u, toranj4_u, toranj5_u, \
        dmg1, dmg2, dmg3, dmg4, dmg5, \
        domet1, domet2, domet3, domet4, domet5, \
        cijena1, cijena2, cijena3, cijena4, cijena5, \
        cijenau1, cijenau2, cijenau3, cijenau4, cijenau5, start):
        #obrub
        slikaRect = slikaObrub.get_rect()
        slikaRect.x = 640
        slikaRect.y = 0
        self.POVRSINA.blit(slikaObrub, slikaRect)
        #toranj1
        self.toranj1_uRect = toranj1_u.get_rect()
        self.toranj1_uRect.x = 640 + 30 + 108 + 10
        self.toranj1_uRect.y = 50
        lblCijenaU = self.fontDMG.render(str(cijenau1), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (640 + 30 + 108 + 10 + 10, 50 + 31))
        self.POVRSINA.blit(toranj1_u, self.toranj1_uRect)
        self.toranj1Rect = slikaToranj1.get_rect()
        self.toranj1Rect.x = 640 + 30
        self.toranj1Rect.y = 50
        self.POVRSINA.blit(slikaToranj1, self.toranj1Rect)
        lblDMG = self.fontDMG.render(str(dmg1), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (640 + 30 + 96, 50 + 23))
        lblDomet = self.fontDMG.render(str(domet1), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (640 + 30 + 90, 50 + 11))
        lblCijena = self.fontDMG.render(str(cijena1), 1, (0, 158, 220))
        self.POVRSINA.blit(lblCijena, (640 + 30 + 36, 50 + 13))
        #toranj2
        self.toranj2_uRect = toranj2_u.get_rect()
        self.toranj2_uRect.x = 640 + 30 + 108 + 10
        self.toranj2_uRect.y = 98
        lblCijenaU = self.fontDMG.render(str(cijenau2), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (640 + 30 + 108 + 10 + 10, 98 + 31))
        self.POVRSINA.blit(toranj2_u, self.toranj2_uRect)
        self.toranj2Rect = slikaToranj2.get_rect()
        self.toranj2Rect.x = 640 + 30
        self.toranj2Rect.y = 50 + 48
        self.POVRSINA.blit(slikaToranj2, self.toranj2Rect)
        lblDMG = self.fontDMG.render(str(dmg2), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (640 + 30 + 96, 98 + 23))
        lblDomet = self.fontDMG.render(str(domet2), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (640 + 30 + 90, 98 + 11))
        lblCijena = self.fontDMG.render(str(cijena2), 1, (0, 158, 220))
        self.POVRSINA.blit(lblCijena, (640 + 30 + 36, 98 + 13))
        #toranj3
        self.toranj3_uRect = toranj3_u.get_rect()
        self.toranj3_uRect.x = 640 + 30 + 108 + 10
        self.toranj3_uRect.y = 146
        lblCijenaU = self.fontDMG.render(str(cijenau3), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (640 + 30 + 108 + 10 + 10, 146 + 31))
        self.POVRSINA.blit(toranj3_u, self.toranj3_uRect)
        self.toranj3Rect = slikaToranj3.get_rect()
        self.toranj3Rect.x = 640 + 30
        self.toranj3Rect.y = 50 + 48 + 48
        self.POVRSINA.blit(slikaToranj3, self.toranj3Rect)
        lblDMG = self.fontDMG.render(str(dmg3), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (640 + 30 + 96, 146 + 23))
        lblDomet = self.fontDMG.render(str(domet3), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (640 + 30 + 90, 146 + 11))
        lblCijena = self.fontDMG.render(str(cijena3), 1, (0, 158, 220))
        self.POVRSINA.blit(lblCijena, (640 + 30 + 36, 146 + 13))
        #snajper
        self.snajper_uRect = toranj4_u.get_rect()
        self.snajper_uRect.x = 640 + 30 + 108 + 10
        self.snajper_uRect.y = 194
        lblCijenaU = self.fontDMG.render(str(cijenau4), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (640 + 30 + 108 + 10 + 10, 194 + 31))
        self.POVRSINA.blit(toranj4_u, self.snajper_uRect)
        self.snajperRect = slikaSnajper.get_rect()
        self.snajperRect.x = 640 + 30
        self.snajperRect.y = 50 + 48 + 48 + 48
        self.POVRSINA.blit(slikaSnajper, self.snajperRect)
        lblDMG = self.fontDMG.render(str(dmg4), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (640 + 30 + 96, 194 + 23))
        lblDomet = self.fontDMG.render(str(domet4), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (640 + 30 + 90, 194 + 11))
        lblCijena = self.fontDMG.render(str(cijena4), 1, (0, 158, 220))
        self.POVRSINA.blit(lblCijena, (640 + 30 + 36, 194 + 13))
        #mitraljez
        self.mitraljez_uRect = toranj5_u.get_rect()
        self.mitraljez_uRect.x = 640 + 30 + 108 + 10
        self.mitraljez_uRect.y = 242
        lblCijenaU = self.fontDMG.render(str(cijenau5), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (640 + 30 + 108 + 10 + 10, 242 + 31))
        self.POVRSINA.blit(toranj5_u, self.mitraljez_uRect)
        self.mitraljezRect = slikaMitraljez.get_rect()
        self.mitraljezRect.x = 640 + 30
        self.mitraljezRect.y = 50 + 48 + 48 + 48 + 48 
        self.POVRSINA.blit(slikaMitraljez, self.mitraljezRect)
        lblDMG = self.fontDMG.render(str(dmg5), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (640 + 30 + 96, 242 + 23))
        lblDomet = self.fontDMG.render(str(domet5), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (640 + 30 + 90, 242 + 11))
        lblCijena = self.fontDMG.render(str(cijena5), 1, (0, 158, 220))
        self.POVRSINA.blit(lblCijena, (640 + 30 + 36, 242 + 13))
        #start ikona
        self.startRect = start.get_rect()
        self.startRect.x = 640 + 10
        self.startRect.y = 480 - 38 - 10
        self.POVRSINA.blit(start, self.startRect)
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
    def CrtajPobjedu(self):
        self.ikonaPredjenRect.x = 100
        self.ikonaPredjenRect.y = 50
        self.POVRSINA.blit(self.ikonaPredjen, self.ikonaPredjenRect)
        self.ikonaGlavniRect.x = 100
        self.ikonaGlavniRect.y = 50 + 120 + 50
        self.POVRSINA.blit(self.ikonaGlavni, self.ikonaGlavniRect)
    def kliknutoPobjeda(self, x, y):
        if self.ikonaGlavniRect.collidepoint(x, y):
            return 1
    def kliknutoStart(self, x, y):
        if self.startRect.collidepoint(x, y):
            return 1
    def hoverPobjeda(self, x, y):
        if self.ikonaGlavniRect.collidepoint(x, y):
            self.POVRSINA.blit(self.menuHover, self.ikonaGlavniRect)
    def CrtajIzgubljeno(self, ikona):
        ikonaRect = ikona.get_rect()
        ikonaRect.x = 100
        ikonaRect.y = 50
        self.POVRSINA.blit(ikona, ikonaRect)
        self.ikonaGlavniRect.x = 100
        self.ikonaGlavniRect.y = 50 + 120 + 50
        self.POVRSINA.blit(self.ikonaGlavni, self.ikonaGlavniRect)