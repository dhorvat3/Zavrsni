import pygame

class sucelje(object):
    """Definiranje korisniskog su?elja"""
    def __init__(self, visina, sirina, POV, ikonaLvl1, ikonaLvl2, ikonaLvl3, ikonaGlavni, ikonaPredjen, upgradeHover, startHover):
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
        self.audioRect = None
        self.ikonaStart_H = startHover
        self.upgradeHover = upgradeHover
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

    def azurirajNovce (self, vrijednost):
        self.pare = self.pare + vrijednost

    def vratiNovce (sefl):
        return sefl.pare

    def ispisStanja(self, HP, trenutno, ukupno):
        boja = (23, 0, 247)
        lblHP = self.font.render(("Player HP: " + str(HP[0]) + "/" + str(HP[1])), 1, boja)
        self.POVRSINA.blit(lblHP, (640 + 10, 10))
        lblNovci = self.font.render(("Stanje: " + str(self.pare)), 1, boja)
        self.POVRSINA.blit(lblNovci, (640 + 10, 25))
        lblNeprijatelji = self.font.render(("Broj: " + str(trenutno) + "/" + str(ukupno)), 1, boja)
        self.POVRSINA.blit(lblNeprijatelji, (640 + 10, 40))

    def postaviMrezu(self, mreza):
        self.mapa = mreza
        self.brojRedova = len(self.mapa)
        self.brojStupaca = len(self.mapa[0])

    def postaviNovce(self, novci):
        self.pare = novci

    def poljeNaPixelu(self, x, y):
        for boxx in range(self.brojRedova):
            for boxy in range(self.brojStupaca):
                lijevo, gore = self.lijevoGore(boxx, boxy)
                boxRect = pygame.Rect(lijevo, gore, self.visina/self.brojRedova - 2, self.sirina/self.brojStupaca - 2)
                if boxRect.collidepoint(x, y):
                    return(boxx, boxy)
        return(None, None)

    def crtajObrub(self, x, y):
        poljex, poljey = self.poljeNaPixelu(x, y)
        if poljex != None and poljey != None and self.mapa[poljey][poljex] != 'Z':
            lijevo, gore = self.lijevoGore(poljex, poljey)
            pygame.draw.rect(self.POVRSINA, (60,  60, 100), (lijevo, gore, self.visina/self.brojRedova, self.sirina/self.brojStupaca), 3)
        elif x is not None and y is not None \
            and self.toranj1_uRect is not None \
            and self.toranj2_uRect is not None \
            and self.toranj3_uRect is not None \
            and self.snajper_uRect is not None \
            and self.mitraljez_uRect is not None:
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

    def odabraniToranj(self, x, y, odabrano):
        if self.toranj1Rect.collidepoint(x, y):
            return 'Toranj1'
        if self.toranj2Rect.collidepoint(x, y):
            return 'Toranj2'
        if self.toranj3Rect.collidepoint(x, y):
            return 'Toranj3'
        if self.snajperRect.collidepoint(x, y):
            return 'Toranj4'
        if self.mitraljezRect.collidepoint(x, y):
            return 'Toranj5'

    def odabraniGumb(self, odabrani, ikona):
        if odabrani == 'Toranj1':
            self.POVRSINA.blit(ikona, self.toranj1Rect)
        elif odabrani == 'Toranj2':
            self.POVRSINA.blit(ikona, self.toranj2Rect)
        elif odabrani == 'Toranj3':
            self.POVRSINA.blit(ikona, self.toranj3Rect)
        elif odabrani == 'Toranj4':
            self.POVRSINA.blit(ikona, self.snajperRect)
        elif odabrani == 'Toranj5':
            self.POVRSINA.blit(ikona, self.mitraljezRect) 

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

    def crtajGlavniMenu(self):
        self.Lvl1Rect.x = 100
        self.Lvl1Rect.y = 200
        self.Lvl2Rect.x = 100
        self.Lvl2Rect.y = 200 + 70 + 20
        self.Lvl3Rect.x = 100
        self.Lvl3Rect.y = 200 + 70 + 20 + 70 + 20
        self.POVRSINA.blit(self.menuLvl1, self.Lvl1Rect)
        self.POVRSINA.blit(self.menuLvl2, self.Lvl2Rect)
        self.POVRSINA.blit(self.menuLvl3, self.Lvl3Rect)

    def gumbGlavniMenu(self, gumb):
        self.POVRSINA.blit(gumb, self.Lvl1Rect)
        self.POVRSINA.blit(gumb, self.Lvl2Rect)
        self.POVRSINA.blit(gumb, self.Lvl3Rect)

    def klikGlavniMenu(self, x, y, gumb):
        if self.Lvl1Rect.collidepoint(x, y):
            self.POVRSINA.blit(gumb, self.Lvl1Rect)
        elif self.Lvl2Rect.collidepoint(x, y):
            self.POVRSINA.blit(gumb, self.Lvl2Rect)
        elif self.Lvl3Rect.collidepoint(x, y):
            self.POVRSINA.blit(gumb, self.Lvl3Rect)

    def kliknutoGlavniMenu(self, x, y):
        if self.Lvl1Rect.collidepoint(x, y):
            return 'Lvl1'
        elif self.Lvl2Rect.collidepoint(x, y):
            return 'Lvl2'
        elif self.Lvl3Rect.collidepoint(x, y):
            return 'Lvl3'
        else:
            return None

    def menuObrub (self, obrub):
        slikaRect = obrub.get_rect()
        slikaRect.x = 640
        slikaRect.y = 0
        self.POVRSINA.blit(obrub, slikaRect)

    def menu(self, slikaToranj1, slikaToranj2, slikaToranj3, slikaSnajper, slikaMitraljez, \
        toranj1_u, toranj2_u, toranj3_u, toranj4_u, toranj5_u, \
        dmg1, dmg2, dmg3, dmg4, dmg5, \
        domet1, domet2, domet3, domet4, domet5, \
        cijena1, cijena2, cijena3, cijena4, cijena5, \
        cijenau1, cijenau2, cijenau3, cijenau4, cijenau5, start):
        pocetak = 80
        bojaCijena = (160, 231, 6)
        #toranj1
        self.toranj1Rect = slikaToranj1.get_rect()
        self.toranj1Rect.x = 640 + 30
        self.toranj1Rect.y = pocetak
        self.POVRSINA.blit(slikaToranj1, self.toranj1Rect)
        lblDMG = self.fontDMG.render(str(dmg1), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (self.toranj1Rect.x + 96, self.toranj1Rect.y + 23))
        lblDomet = self.fontDMG.render(str(domet1), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (self.toranj1Rect.x + 90, self.toranj1Rect.y + 11))
        lblCijena = self.fontDMG.render(str(cijena1), 1, bojaCijena)
        self.POVRSINA.blit(lblCijena, (self.toranj1Rect.x + 36, self.toranj1Rect.y + 13))
        #upgrade 1
        self.toranj1_uRect = toranj1_u.get_rect()
        self.toranj1_uRect.x = self.toranj1Rect.x + 108 + 10
        self.toranj1_uRect.y = self.toranj1Rect.y
        lblCijenaU = self.fontDMG.render(str(cijenau1), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (self.toranj1_uRect.x + 10, self.toranj1_uRect.y + 31))
        self.POVRSINA.blit(toranj1_u, self.toranj1_uRect)
        #toranj2
        self.toranj2Rect = slikaToranj2.get_rect()
        self.toranj2Rect.x = 640 + 30
        self.toranj2Rect.y = pocetak + 48
        self.POVRSINA.blit(slikaToranj2, self.toranj2Rect)
        lblDMG = self.fontDMG.render(str(dmg2), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (self.toranj2Rect.x + 96, self.toranj2Rect.y + 23))
        lblDomet = self.fontDMG.render(str(domet2), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (self.toranj2Rect.x + 90, self.toranj2Rect.y + 11))
        lblCijena = self.fontDMG.render(str(cijena2), 1, bojaCijena)
        self.POVRSINA.blit(lblCijena, (self.toranj2Rect.x + 36, self.toranj2Rect.y + 13))
        #upgrade 2
        self.toranj2_uRect = toranj2_u.get_rect()
        self.toranj2_uRect.x = self.toranj2Rect.x + 108 + 10
        self.toranj2_uRect.y = self.toranj2Rect.y
        lblCijenaU = self.fontDMG.render(str(cijenau2), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (self.toranj2Rect.x + 108 + 10 + 10, self.toranj2Rect.y + 31))
        self.POVRSINA.blit(toranj2_u, self.toranj2_uRect)
        #toranj3
        self.toranj3Rect = slikaToranj3.get_rect()
        self.toranj3Rect.x = 640 + 30
        self.toranj3Rect.y = pocetak + 48 + 48
        self.POVRSINA.blit(slikaToranj3, self.toranj3Rect)
        lblDMG = self.fontDMG.render(str(dmg3), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (self.toranj3Rect.x + 96, self.toranj3Rect.y + 23))
        lblDomet = self.fontDMG.render(str(domet3), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (self.toranj3Rect.x + 90, self.toranj3Rect.y + 11))
        lblCijena = self.fontDMG.render(str(cijena3), 1, bojaCijena)
        self.POVRSINA.blit(lblCijena, (self.toranj3Rect.x + 36, self.toranj3Rect.y + 13))
        #upgrade 3
        self.toranj3_uRect = toranj3_u.get_rect()
        self.toranj3_uRect.x = self.toranj3Rect.x + 108 + 10
        self.toranj3_uRect.y = self.toranj3Rect.y
        lblCijenaU = self.fontDMG.render(str(cijenau3), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (self.toranj3Rect.x + 108 + 10 + 10, self.toranj3Rect.y + 31))
        self.POVRSINA.blit(toranj3_u, self.toranj3_uRect)
        #snajper
        self.snajperRect = slikaSnajper.get_rect()
        self.snajperRect.x = 640 + 30
        self.snajperRect.y = pocetak + 48 + 48 + 48
        self.POVRSINA.blit(slikaSnajper, self.snajperRect)
        lblDMG = self.fontDMG.render(str(dmg4), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (self.snajperRect.x + 96, self.snajperRect.y + 23))
        lblDomet = self.fontDMG.render(str(domet4), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (self.snajperRect.x + 90, self.snajperRect.y + 11))
        lblCijena = self.fontDMG.render(str(cijena4), 1, bojaCijena)
        self.POVRSINA.blit(lblCijena, (self.snajperRect.x + 36, self.snajperRect.y + 13))
        #upgrade 4
        self.snajper_uRect = toranj4_u.get_rect()
        self.snajper_uRect.x = self.snajperRect.x + 108 + 10
        self.snajper_uRect.y = self.snajperRect.y
        lblCijenaU = self.fontDMG.render(str(cijenau4), 0, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (self.snajperRect.x + 108 + 10 + 10, self.snajperRect.y + 31))
        self.POVRSINA.blit(toranj4_u, self.snajper_uRect)
        #mitraljez
        self.mitraljezRect = slikaMitraljez.get_rect()
        self.mitraljezRect.x = 640 + 30
        self.mitraljezRect.y = pocetak + 48 + 48 + 48 + 48 
        self.POVRSINA.blit(slikaMitraljez, self.mitraljezRect)
        lblDMG = self.fontDMG.render(str(dmg5), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDMG, (self.mitraljezRect.x + 96, self.mitraljezRect.y + 23))
        lblDomet = self.fontDMG.render(str(domet5), 1, (220, 0, 0))
        self.POVRSINA.blit(lblDomet, (self.mitraljezRect.x + 90, self.mitraljezRect.y + 11))
        lblCijena = self.fontDMG.render(str(cijena5), 1, bojaCijena)
        self.POVRSINA.blit(lblCijena, (self.mitraljezRect.x + 36, self.mitraljezRect.y + 13))
        #upgrade 5
        self.mitraljez_uRect = toranj5_u.get_rect()
        self.mitraljez_uRect.x = self.mitraljezRect.x + 108 + 10
        self.mitraljez_uRect.y = self.mitraljezRect.y
        lblCijenaU = self.fontDMG.render(str(cijenau5), 1, (222, 0, 0))
        self.POVRSINA.blit(lblCijenaU, (self.mitraljezRect.x + 108 + 10 + 10, self.mitraljezRect.y + 31))
        self.POVRSINA.blit(toranj5_u, self.mitraljez_uRect)
        #start ikona
        self.startRect = start.get_rect()
        self.startRect.x = 640 + 10
        self.startRect.y = 480 - 38 - 10
        self.POVRSINA.blit(start, self.startRect)

    def gumbTornja(self, slikaGumba):
        if self.toranj1Rect is not None:
            self.POVRSINA.blit(slikaGumba, self.toranj1Rect)
            self.POVRSINA.blit(slikaGumba, self.toranj2Rect)
            self.POVRSINA.blit(slikaGumba, self.toranj3Rect)
            self.POVRSINA.blit(slikaGumba, self.mitraljezRect)
            self.POVRSINA.blit(slikaGumba, self.snajperRect)

    def CrtajPobjedu(self):
        self.ikonaPredjenRect.x = 100
        self.ikonaPredjenRect.y = 10
        self.POVRSINA.blit(self.ikonaPredjen, self.ikonaPredjenRect)
        self.ikonaGlavniRect.x = 100
        self.ikonaGlavniRect.y = 50 + 120 + 50
        self.POVRSINA.blit(self.ikonaGlavni, self.ikonaGlavniRect)

    def gumbPobjeda(self, gumb):
        self.POVRSINA.blit(gumb, self.ikonaGlavniRect)

    def kliknutoPobjeda(self, x, y, gumb):
        self.POVRSINA.blit(gumb, self.ikonaGlavniRect)
        if self.ikonaGlavniRect.collidepoint(x, y):
            return 1

    def kliknutoStart(self, x, y):
        if self.startRect.collidepoint(x, y):
            return 1

    def CrtajIzgubljeno(self, ikona):
        ikonaRect = ikona.get_rect()
        ikonaRect.x = 100
        ikonaRect.y = 10
        self.POVRSINA.blit(ikona, ikonaRect)
        self.ikonaGlavniRect.x = 100
        self.ikonaGlavniRect.y = 50 + 120 + 50
        self.POVRSINA.blit(self.ikonaGlavni, self.ikonaGlavniRect)

    def crtajPreostalo(self, trenutno, ukupno):
        lblBroj = self.font.render(('Preostalo neprijatelja: ' + str(trenutno) + '/' + str(ukupno)), 1, (255, 0, 0))
        self.POVRSINA.blit(lblBroj, (150, 150))

    def CrtajAudio(self, ikona):
        self.audioRect = ikona.get_rect()
        self.audioRect.x = 640 + 160
        self.audioRect.y = 10
        self.POVRSINA.blit(ikona, self.audioRect)

    def AudioKliknut(self, x, y):
        if self.audioRect.collidepoint(x, y):
            return 1

    def startKliknut(self, x, y):
        if self.startRect.collidepoint(x, y):
            self.POVRSINA.blit(self.ikonaStart_H, self.startRect)