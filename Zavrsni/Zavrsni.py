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
ikonaNeprijatelj2 = pygame.image.load('grafika/neprijatelji/neprijatelj2_idle.png')
ikonaNeprijatelj3 = pygame.image.load('grafika/neprijatelji/neprijatelj3_idle.png')
ikonaNeprijatelj4 = pygame.image.load('grafika/neprijatelji/neprijatelj4_idle.png')
dmgikonaNeprijatelj1 = pygame.image.load('grafika/neprijatelji/neprijatelj1_dmg.png')
dmgikonaNeprijatelj2 = pygame.image.load('grafika/neprijatelji/neprijatelj2_dmg.png')
dmgikonaNeprijatelj3 = pygame.image.load('grafika/neprijatelji/neprijatelj3_dmg.png')
dmgikonaNeprijatelj4 = pygame.image.load('grafika/neprijatelji/neprijatelj4_dmg.png')
glavnaZgrada = pygame.image.load('grafika\zgrada.png')
toranj1ikona = pygame.image.load('grafika/toranj1_ikona.png')
toranj2ikona = pygame.image.load('grafika/toranj2_ikona.png')
toranj3ikona = pygame.image.load('grafika/toranj3_ikona.png')
toranj1slika = pygame.image.load('grafika/tornjevi/toranj1.png')
toranj2slika = pygame.image.load('grafika/tornjevi/toranj2.png')
toranj3slika = pygame.image.load('grafika/tornjevi/toranj3.png')
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
toranj_upgrade_hover = pygame.image.load('grafika/tornjevi/toranj_upgrade_h.png')
izgubljenoSlika = pygame.image.load('grafika/izgubljenLvl.png')
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
toranj1 = 'Toranj1'
toranj2 = 'Toranj2'
toranj3 = 'Toranj3'
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

    dmg1 = 5
    dmg2 = 5
    dmg3 = 10

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    POVRSINA = pygame.display.set_mode((UkupnaVisina, SirinaProzora), 0, 32)

    lvlSeed = maestro()
    UI = sucelje(VisinaProzora, SirinaProzora, POVRSINA, menuHover, menuLvl1, menuLvl2, menuLvl3, glavniMenu, predjenLabel, toranj_upgrade_hover)
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
        if mod == modPobjeda:
            #UI.CrtajPobjedu()
            if kliknuto:
                if UI.kliknutoPobjeda(mousex, mousey):
                    mod = modMenu
            if not kliknuto:
                UI.hoverPobjeda(mousex, mousey)
            UI.CrtajPobjedu()
        if mod == modIzgubljeno:
            if kliknuto:
                if UI.kliknutoPobjeda(mousex, mousey):
                    mod = modMenu
            if not kliknuto:
                UI.hoverPobjeda(mousex, mousey)
            UI.CrtajIzgubljeno(izgubljenoSlika)
        elif mod == modMenu:
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
                    lvl = Mapa(grid, VisinaProzora, SirinaProzora, okolis, put_ravno, put_dole, put_kutLD, put_kutDD, put_kraj, put_kraj_D, put_pocetak_D, put_pocetak_G)
                    tornjevi = []
                    GlZgrada = zgrada(POVRSINA, glavnaZgrada, zgradaHP, kraj, VisinaProzora, SirinaProzora, grid)
            if not kliknuto:
                UI.hoverGlavniMenu(mousex, mousey)
            UI.crtajGlavniMenu()
        elif mod == modIgra:
            dmgLista = []
            lvl.crtajMrezu(POVRSINA, start, kraj)
            if lvlSeed.vrijeme():
                tip, brzina, HP = lvlSeed.vratiNeprijatelj()
                if tip is not None:
                    if tip == 1:
                        ikona = ikonaNeprijatelj1
                        dmgIkona = dmgikonaNeprijatelj1
                    elif tip == 2:
                        ikona = ikonaNeprijatelj2
                        dmgIkona = dmgikonaNeprijatelj2
                    elif tip == 3:
                        ikona = ikonaNeprijatelj3
                        dmgIkona = dmgikonaNeprijatelj3
                    else:
                        ikona = ikonaNeprijatelj4
                        dmgIkona = dmgikonaNeprijatelj4
                    listaNeprijatelj.append(neprijatelj(grid, VisinaProzora, SirinaProzora, start, kraj, POVRSINA, brzina, R, ikona, dmgIkona, HP))
                else:
                    pocetak = 0
            NeprijateljiRect = []
            GlZgrada.crtaj()
            for i in range (len(listaNeprijatelj)):
                listaNeprijatelj[i].Pomakni()
            for i in range (len(listaNeprijatelj)):
                NeprijateljiRect.append(listaNeprijatelj[i].ikonaRect)
            
            if kliknuto:
                lijevo, gore = UI.poljeNaPixelu(mousex, mousey)
                if lijevo is None and gore is None:
                    odabraniToranj = UI.odabraniToranj(mousex, mousey, slikaOdabrano)
                    odabraniUpgrade = UI.odabraniUpgrade(mousex, mousey)
                    if odabraniUpgrade is not None:
                        if odabraniUpgrade == upgrade1:
                            if UI.vratiNovce() >= 10:
                                dmg1 = dmg1 + 1
                                UI.azurirajNovce(-10)
                                for i in tornjevi:
                                    if i.vratiTip() == 1:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade2:
                            if UI.vratiNovce() >= 10:
                                dmg2 = dmg2 + 1
                                UI.azurirajNovce(-10)
                                for i in tornjevi:
                                    if i.vratiTip() == 2:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade3:
                            if UI.vratiNovce() >= 10:
                                dmg3 = dmg3 + 1
                                UI.azurirajNovce(-10)
                                for i in tornjevi:
                                    if i.vratiTip() == 3:
                                        i.upgradeDMG(1)
                elif not grid[gore][lijevo] == Z and not grid[gore][lijevo] == T:
                    if odabraniToranj is not None:
                        if odabraniToranj == toranj1:
                            if UI.vratiNovce() >= 10:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(1, 3, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 100, dmg1, 2000, toranj1slika))
                                UI.azurirajNovce(-10)
                        if odabraniToranj == toranj2:
                            if UI.vratiNovce() >= 20:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(2, 3, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 200, dmg2, 2000, toranj2slika))
                                UI.azurirajNovce(-20)
                        if odabraniToranj == toranj3:
                            if UI.vratiNovce() >= 30:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(3, 4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 200, dmg3, 2000, toranj3slika))
                                UI.azurirajNovce(-30)
            if not kliknuto:
                UI.crtajObrub(mousex, mousey, slikaHover)
                if odabraniToranj == toranj1:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == toranj2:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
                if odabraniToranj == toranj3:
                    UI.pozadina(odabraniToranj, slikaOdabrano)
            for i in range (len(tornjevi)):
                tornjevi[i - 1].Crtaj()
                dmgLista.append(tornjevi[i - 1].Ciljanje(NeprijateljiRect, metakIkona))
            if dmgLista != []:
                for j in dmgLista:
                    for i in j:
                        if i[0] > -1 and listaNeprijatelj:
                            print("Indeks: ", i[0], " damage: ", i[1])
                            listaNeprijatelj[i[0]].damage(i[1])
                            if listaNeprijatelj[i[0]].vratiHP() < 1:
                                UI.azurirajNovce(5)
                                listaNeprijatelj.remove(listaNeprijatelj[i[0]])
            indekas = GlZgrada.damage(NeprijateljiRect)
            if indekas > -1:
                print ("Damage: ", indekas)
                listaNeprijatelj.remove(listaNeprijatelj[indekas])
                indekas = -1
            UI.ispisStanja(GlZgrada.vratiHP())
            if GlZgrada.vratiHP()[0] <= 0:
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
                lvlSeed.reset()
            if len(listaNeprijatelj) < 1 and pocetak == 0:
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
            UI.menu(menuSlika, toranj1ikona, toranj2ikona, toranj3ikona, toranj1_upgrade, toranj2_upgrade, toranj3_upgrade, dmg1, dmg2, dmg3)
        pygame.display.update()
        POVRSINA.fill((0,15,0))
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()