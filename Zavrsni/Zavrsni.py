#Glavna klasa
import pygame
import sys
#from random import randrange
from mapa import Mapa
from neprijatelj import neprijatelj
from sucelje import sucelje
from toranj import toranj
from zgrada import zgrada
from maestro import maestro
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONUP, MOUSEMOTION

#objekti igre
metakIkona = pygame.image.load('grafika\metak.png')
ikonaNeprijatelj1 = pygame.image.load('grafika/neprijatelji/neprijatelj1_idle.png')
ikonaNeprijatelj1a = pygame.image.load('grafika/neprijatelji/neprijatelj1a_idle.png')
ikonaNeprijatelj2 = pygame.image.load('grafika/neprijatelji/neprijatelj2_idle.png')
ikonaNeprijatelj2a = pygame.image.load('grafika/neprijatelji/neprijatelj2a_idle.png')
ikonaNeprijatelj3 = pygame.image.load('grafika/neprijatelji/neprijatelj3_idle.png')
ikonaNeprijatelj3a = pygame.image.load('grafika/neprijatelji/neprijatelj3a_idle.png')
ikonaNeprijatelj4 = pygame.image.load('grafika/neprijatelji/neprijatelj4_idle.png')
ikonaNeprijatelj4a = pygame.image.load('grafika/neprijatelji/neprijatelj4a_idle.png')
dmgikonaNeprijatelj1 = pygame.image.load('grafika/neprijatelji/neprijatelj1_dmg.png')
dmgikonaNeprijatelj2 = pygame.image.load('grafika/neprijatelji/neprijatelj2_dmg.png')
dmgikonaNeprijatelj3 = pygame.image.load('grafika/neprijatelji/neprijatelj3_dmg.png')
dmgikonaNeprijatelj4 = pygame.image.load('grafika/neprijatelji/neprijatelj4_dmg.png')
dmgikonaNeprijatelj1a = pygame.image.load('grafika/neprijatelji/neprijatelj1a_dmg.png')
dmgikonaNeprijatelj2a = pygame.image.load('grafika/neprijatelji/neprijatelj2a_dmg.png')
dmgikonaNeprijatelj3a = pygame.image.load('grafika/neprijatelji/neprijatelj3a_dmg.png')
dmgikonaNeprijatelj4a = pygame.image.load('grafika/neprijatelji/neprijatelj4a_dmg.png')
glavnaZgrada = pygame.image.load('grafika\zgrada.png')
toranj1ikona = pygame.image.load('grafika/toranj1_ikona.png')
toranj2ikona = pygame.image.load('grafika/toranj2_ikona.png')
toranj3ikona = pygame.image.load('grafika/toranj3_ikona.png')
snajperikona = pygame.image.load('grafika/snajper_ikona.png')
mitraljezikona = pygame.image.load('grafika/mitraljez_ikona.png')
toranj1slika = pygame.image.load('grafika/tornjevi/toranj1.png')
toranj2slika = pygame.image.load('grafika/tornjevi/toranj2.png')
toranj3slika = pygame.image.load('grafika/tornjevi/toranj3.png')
snajperslika = pygame.image.load('grafika/tornjevi/toranj4.png')
mitraljezslika = pygame.image.load('grafika/tornjevi/toranj5.png')
#UI
slikaHover = pygame.image.load('grafika/hover.png')
slikaOdabrano = pygame.image.load('grafika/odabrano.png')
menuSlika = pygame.image.load('grafika\menu_obrub.png')
menuLvl1 = pygame.image.load('grafika/menuLvl1.png')
menuLvl2 = pygame.image.load('grafika/menuLvl2.png')
menuLvl3 = pygame.image.load('grafika/menuLvl3.png')
menuHover = pygame.image.load('grafika/menuHover.png')
predjenLabel = pygame.image.load('grafika/predjenLvl.png')
glavniMenu = pygame.image.load('grafika/menuGlavni.png')
toranj1_upgrade = pygame.image.load('grafika/tornjevi/toranj1_upgrade.png')
toranj2_upgrade = pygame.image.load('grafika/tornjevi/toranj2_upgrade.png')
toranj3_upgrade = pygame.image.load('grafika/tornjevi/toranj3_upgrade.png')
toranj4_upgrade = pygame.image.load('grafika/tornjevi/toranj4_upgrade.png')
toranj5_upgrade = pygame.image.load('grafika/tornjevi/toranj5_upgrade.png')
toranj_upgrade_hover = pygame.image.load('grafika/tornjevi/toranj_upgrade_h.png')
izgubljenoSlika = pygame.image.load('grafika/izgubljenLvl.png')
ikonaStart = pygame.image.load('grafika/ikonaStart.png')
ikonaStart_H = pygame.image.load('grafika/ikonaStart_H.png')
#mapa
okolis = pygame.image.load('grafika/mapa/trava_okolis.png')
put_ravno = pygame.image.load('grafika/mapa/put_ravno.png')
put_dole = pygame.image.load('grafika/mapa/put_dole.png')
put_kutLD = pygame.image.load('grafika/mapa/put_kutLD.png')
put_kutDD = pygame.image.load('grafika/mapa/put_kutDD.png')
put_kraj = pygame.image.load('grafika/mapa/put_kraj.png')
put_kraj_D = pygame.image.load('grafika/mapa/put_kraj_D.png')
put_pocetak_D = pygame.image.load('grafika/mapa/pocetak_D.png')
put_pocetak_G = pygame.image.load('grafika/mapa/pocetak_G.png')

FPS = 30
VisinaProzora = 640
SirinaProzora = 480
UkupnaVisina = 840

S = 'S'
Z = 'Z'
L = 'L'
R = 'R'
U = 'U'
D = 'D'
T = 'T'
upgrade1 = 'Upgrade1'
upgrade2 = 'Upgrade2'
upgrade3 = 'Upgrade3'
upgrade4 = 'Upgrade4'
upgrade5 = 'Upgrade5'
toranj1 = 'Toranj1'
toranj2 = 'Toranj2'
toranj3 = 'Toranj3'
snajper = 'Toranj4'
mitraljez = 'Toranj5'
modMenu = 'menu'
modIgra = 'igra'
modPobjeda = 'Pobjeda'
modIzgubljeno = 'Izgubljeno'

grid = []
start = None
kraj = None
brojNeprijatelja = None
startGold = None

def main ():
    global FPSCLOCK, POVRSINA;

    #varijable tornjeva
    #toranj1
    dmg1 = 5
    domet1 = 100
    brzinaP1 = 10
    cijena1 = 10
    cijenau1 = 5
    #toranj2
    dmg2 = 5
    domet2 = 200
    brzinaP2 = 10
    cijena2 = 20
    cijenau2 = 5
    #toranj3
    dmg3 = 10
    domet3 = 200
    brzinaP3 = 15
    cijena3 = 30
    cijenau3 = 10
    #snajper
    dmg4 = 100
    domet4 = 500
    brzinaP4 = 50
    cijena4 = 100
    cijenau4 = 30
    #mitraljez
    dmg5 = 10
    domet5 = 80
    brzinaP5 = 20
    cijena5 = 100
    cijenau5 = 50

    startKliknut = 0
    startVrijeme = 1

    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    POVRSINA = pygame.display.set_mode((UkupnaVisina, SirinaProzora), 0, 32)

    #zvukovi
    pucanjZvuk = pygame.mixer.Sound("glazba/pucanj.ogg")
    ouchZvuk = pygame.mixer.Sound("glazba/ouch.ogg")
    smrtZvuk = pygame.mixer.Sound("glazba/smrt.ogg")

    pygame.mixer.music.load('glazba/menu.ogg')
    pygame.mixer.music.play(-1, 0.0)

    lvlSeed = maestro()
    UI = sucelje(VisinaProzora, SirinaProzora, POVRSINA, menuHover, menuLvl1, menuLvl2, menuLvl3, glavniMenu, predjenLabel, toranj_upgrade_hover, ikonaStart_H)
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Zavrsni')
    odabraniToranj = None
    odabraniUpgrade = None
    odabraniLvl = None
    mod = modMenu
    signal = 0
    pocetak = 1
    listaNeprijatelj = []
    while True:
        kliknuto = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                kliknuto = True
        if mod == modMenu:
            if kliknuto:
                odabraniLvl = UI.kliknutoGlavniMenu(mousex, mousey)
                if odabraniLvl is not None:
                    mod = modIgra
                    lvlSeed.lvlLoad(odabraniLvl)
                    grid = lvlSeed.grid()
                    start = lvlSeed.start()
                    kraj = lvlSeed.kraj()
                    startGold = lvlSeed.startGold()
                    brojNeprijatelja = lvlSeed.brNeprijatelja()
                    zgradaHP = lvlSeed.zgradaHP()
                    UI.postaviMrezu(grid)
                    UI.postaviNovce(startGold)
                    pygame.mixer.music.fadeout(1000)
                    pygame.mixer.music.load('glazba/' + odabraniLvl + '.ogg')
                    
                    pygame.mixer.music.play(-1, 0.0)
                    pygame.mixer.music.set_volume(0.3)
                    lvl = Mapa(grid, VisinaProzora, SirinaProzora, okolis, put_ravno, put_dole, put_kutLD, put_kutDD, put_kraj, put_kraj_D, put_pocetak_D, put_pocetak_G)
                    tornjevi = []
                    GlZgrada = zgrada(POVRSINA, glavnaZgrada, zgradaHP, kraj, VisinaProzora, SirinaProzora, grid)
            if not kliknuto:
                UI.hoverGlavniMenu(mousex, mousey)
            UI.crtajGlavniMenu()
        elif mod == modPobjeda:
            if kliknuto:
                if UI.kliknutoPobjeda(mousex, mousey):
                    mod = modMenu
            if not kliknuto:
                UI.hoverPobjeda(mousex, mousey)
            UI.CrtajPobjedu()
        elif mod == modIzgubljeno:
            if kliknuto:
                if UI.kliknutoPobjeda(mousex, mousey):
                    mod = modMenu
            if not kliknuto:
                UI.hoverPobjeda(mousex, mousey)
            UI.CrtajIzgubljeno(izgubljenoSlika)
        elif mod == modIgra:
            #print ("Pocetak: ", startVrijeme)
            #print ("Start: ", startKliknut)
            dmgLista = []
            lvl.crtajMrezu(POVRSINA, start, kraj)
            if startKliknut:
                if startVrijeme:
                    startVrijeme = 0
                    #print ("Vrijeme")
                    lvlSeed.postaviVrijeme()
                #stvaranje neprijatelja
                elif lvlSeed.vrijeme():
                    tip, brzina, HP = lvlSeed.vratiNeprijatelj()
                    if tip is not None:
                        if tip == 1:
                            ikona = ikonaNeprijatelj1
                            dmgIkona = dmgikonaNeprijatelj1
                        elif tip == 2:
                            ikona = ikonaNeprijatelj1a
                            dmgIkona = dmgikonaNeprijatelj1a
                        elif tip == 3:
                            ikona = ikonaNeprijatelj2
                            dmgIkona = dmgikonaNeprijatelj2
                        elif tip == 4:
                            ikona = ikonaNeprijatelj2a
                            dmgIkona = dmgikonaNeprijatelj2a
                        elif tip == 5:
                            ikona = ikonaNeprijatelj3
                            dmgIkona = dmgikonaNeprijatelj3
                        elif tip == 6:
                            ikona = ikonaNeprijatelj3a
                            dmgIkona = dmgikonaNeprijatelj3a
                        elif tip == 7:
                            ikona = ikonaNeprijatelj4
                            dmgIkona = dmgikonaNeprijatelj4
                        else:
                            ikona = ikonaNeprijatelj4a
                            dmgIkona = dmgikonaNeprijatelj4a
                        listaNeprijatelj.append(neprijatelj(grid, VisinaProzora, SirinaProzora, start, kraj, POVRSINA, brzina, R, ikona, dmgIkona, HP, ouchZvuk))
                    else:
                        pocetak = 0
            NeprijateljiRect = []
            GlZgrada.crtaj()

            for i in range (len(listaNeprijatelj)):
                listaNeprijatelj[i].Pomakni()
            for i in range (len(listaNeprijatelj)):
                NeprijateljiRect.append(listaNeprijatelj[i].ikonaRect)

            #for i in listaNeprijatelj:
            #    i.Pomakni()
            #for i in listaNeprijatelj:
            #    NeprijateljiRect.append(i.ikonaRect)

            if kliknuto:
                if not startKliknut:
                    startKliknut = UI.kliknutoStart(mousex, mousey)
                lijevo, gore = UI.poljeNaPixelu(mousex, mousey)
                if lijevo is None and gore is None:
                    odabraniToranj = UI.odabraniToranj(mousex, mousey, slikaOdabrano)
                    odabraniUpgrade = UI.odabraniUpgrade(mousex, mousey)
                    #postavljanje parametara upgradeova
                    if odabraniUpgrade is not None:
                        if odabraniUpgrade == upgrade1:
                            if UI.vratiNovce() >= cijenau1:
                                dmg1 = dmg1 + 1
                                UI.azurirajNovce(-cijenau1)
                                for i in tornjevi:
                                    if i.vratiTip() == 1:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade2:
                            if UI.vratiNovce() >= cijenau2:
                                dmg2 = dmg2 + 1
                                UI.azurirajNovce(-cijenau2)
                                for i in tornjevi:
                                    if i.vratiTip() == 2:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade3:
                            if UI.vratiNovce() >= cijenau3:
                                dmg3 = dmg3 + 1
                                UI.azurirajNovce(-cijenau3)
                                for i in tornjevi:
                                    if i.vratiTip() == 3:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade4:
                            if UI.vratiNovce() >= cijenau4:
                                dmg4 = dmg4 + 1
                                UI.azurirajNovce(-cijenau4)
                                for i in tornjevi:
                                    if i.vratiTip() == 4:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade5:
                            if UI.vratiNovce() >= cijenau5:
                                dmg5 = dmg5 + 1
                                UI.azurirajNovce(-cijenau5)
                                for i in tornjevi:
                                    if i.vratiTip() == 5:
                                        i.upgradeDMG(1) 
                elif not grid[gore][lijevo] == Z and not grid[gore][lijevo] == T:
                    #stvaranje tornjeva
                    if odabraniToranj is not None:
                        if odabraniToranj == toranj1:
                            if UI.vratiNovce() >= cijena1:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(1, brzinaP1, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet1, dmg1, 2000, toranj1slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena1)
                        if odabraniToranj == toranj2:
                            if UI.vratiNovce() >= cijena2:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(2, brzinaP2, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet2, dmg2, 2000, toranj2slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena2)
                        if odabraniToranj == toranj3:
                            if UI.vratiNovce() >= cijena3:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(3, brzinaP3, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet3, dmg3, 2000, toranj3slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena3)
                        if odabraniToranj == snajper:
                            if UI.vratiNovce() >= cijena4:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(4, brzinaP4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet4, dmg4, 7000, snajperslika, pucanjZvuk))
                                UI.azurirajNovce(-cijena4)
                        if odabraniToranj == mitraljez:
                            if UI.vratiNovce() >= cijena5:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(5, brzinaP5, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet5, dmg5, 500, mitraljezslika, pucanjZvuk))
                                UI.azurirajNovce(-cijena5)
            if not kliknuto:
                UI.crtajObrub(mousex, mousey, slikaHover)
                if odabraniToranj == toranj1:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == toranj2:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == toranj3:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == snajper:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == mitraljez:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
            for i in range (len(tornjevi)):
                tornjevi[i - 1].Crtaj()
                dmgLista.append(tornjevi[i - 1].Ciljanje(NeprijateljiRect, metakIkona))
            if dmgLista != []:
                for j in dmgLista:
                    for i in j:
                        if i[0] > -1 and listaNeprijatelj:
                            #print("Indeks: ", i[0], " damage: ", i[1])
                            listaNeprijatelj[i[0]].damage(i[1])
                            if listaNeprijatelj[i[0]].vratiHP() < 1:
                                smrtZvuk.play(0)
                                UI.azurirajNovce(5)
                                listaNeprijatelj.remove(listaNeprijatelj[i[0]])
            indekas = GlZgrada.damage(NeprijateljiRect)
            if indekas > -1:
                #print ("Damage: ", indekas)
                listaNeprijatelj.remove(listaNeprijatelj[indekas])
                indekas = -1
            UI.ispisStanja(GlZgrada.vratiHP())
            #uvijeti kraja igre
            if GlZgrada.vratiHP()[0] <= 0:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('glazba/menu.ogg')
                pygame.mixer.music.play()
                pocetak = 1
                print("Izgubljeno")
                mod = modIzgubljeno
                odabraniLvl = None
                listaNeprijatelj = []
                grid = []
                lvlSeed.obrisiLvl()
                UI.postaviNovce(0)
                dmg1 = 5
                dmg2 = 5
                dmg3 = 10
                dmg4 = 100
                lvlSeed.reset()
                startVrijeme = 1
                startKliknut = 0
            if len(listaNeprijatelj) < 1 and pocetak == 0:
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('glazba/menu.ogg')
                pygame.mixer.music.play(-1, 0.0)
                pocetak = 1
                print ("Pobeda")
                mod = modPobjeda
                odabraniLvl = None
                grid = []
                lvlSeed.obrisiLvl()
                UI.postaviNovce(0)
                dmg1 = 5
                dmg2 = 5
                dmg3 = 10
                lvlSeed.reset()
                startVrijeme = 1
                startKliknut = 0
            UI.menu(menuSlika, toranj1ikona, toranj2ikona, toranj3ikona, snajperikona, mitraljezikona, \
                toranj1_upgrade, toranj2_upgrade, toranj3_upgrade, toranj4_upgrade, toranj5_upgrade, \
                dmg1, dmg2, dmg3, dmg4, dmg5, \
                domet1, domet2, domet3, domet4, domet5, \
                cijena1, cijena2, cijena3, cijena4, cijena5, \
                cijenau1, cijenau2, cijenau3, cijenau4, cijenau5, ikonaStart)
        pygame.display.update()
        POVRSINA.fill((0,15,0))
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()