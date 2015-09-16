#Glavna klasa
import pygame
import sys
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
slikaOdabrano = pygame.image.load('grafika/odabrano.png')
slikaGumb = pygame.image.load('grafika/gumb_toranj.png')
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
pozadina = pygame.image.load('grafika/pozadina.png')
naslov = pygame.image.load('grafika/naslov.png')
audioON = pygame.image.load('grafika/audio_on.png')
audioOFF = pygame.image.load('grafika/audio_off.png')
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
    pocetak = 1
    listaNeprijatelj = []
    izvrsavaj = True
    audio = True
    while izvrsavaj:
        kliknuto = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                #pygame.quit()
                izvrsavaj = False
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                kliknuto = True
        if mod == modMenu:
            POVRSINA.blit(naslov, ((0, 0), (840, 480)))
            #varijable tornjeva
            #Tetejac
            dmg1 = 10
            domet1 = 100
            ASpeed1 = 700
            brzinaP1 = 15
            cijena1 = 10
            cijenau1 = 5
            #Kalašnjikov
            dmg2 = 15
            domet2 = 200
            ASpeed2 = 900
            brzinaP2 = 15
            cijena2 = 20
            cijenau2 = 5
            #Karabin
            dmg3 = 20
            domet3 = 200
            ASpeed3 = 900
            brzinaP3 = 20
            cijena3 = 50
            cijenau3 = 10
            #snajper
            dmg4 = 100
            domet4 = 500
            ASpeed4 = 7000
            brzinaP4 = 40
            cijena4 = 100
            cijenau4 = 30
            #mitraljez
            dmg5 = 5
            domet5 = 90
            ASpeed5 = 333
            brzinaP5 = 20
            cijena5 = 100
            cijenau5 = 50
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
                    #pygame.mixer.music.set_volume(0.3)
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
            UI.menuObrub(menuSlika)
            UI.gumbTornja(slikaGumb)
            if odabraniToranj is not None:
                UI.odabraniGumb(odabraniToranj, slikaOdabrano)
            UI.menu(toranj1ikona, toranj2ikona, toranj3ikona, snajperikona, mitraljezikona, \
                toranj1_upgrade, toranj2_upgrade, toranj3_upgrade, toranj4_upgrade, toranj5_upgrade, \
                dmg1, dmg2, dmg3, dmg4, dmg5, \
                domet1, domet2, domet3, domet4, domet5, \
                cijena1, cijena2, cijena3, cijena4, cijena5, \
                cijenau1, cijenau2, cijenau3, cijenau4, cijenau5, ikonaStart)
            if audio:
                UI.CrtajAudio(audioON)
            else:
                UI.CrtajAudio(audioOFF)
            #print ("Pocetak: ", startVrijeme)
            #print ("Start: ", startKliknut)
            dmgLista = []
            lvl.crtajMrezu(POVRSINA, start, kraj)
            #neprijatelji
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
            #Gradnja
            if kliknuto:
                UI.startKliknut(mousex, mousey)
                if UI.AudioKliknut(mousex, mousey):
                    audio = not audio
                if not startKliknut:
                    startKliknut = UI.kliknutoStart(mousex, mousey)
                lijevo, gore = UI.poljeNaPixelu(mousex, mousey)
                #gradnja upgradea
                if lijevo is None and gore is None:
                    odabraniToranj = UI.odabraniToranj(mousex, mousey, slikaOdabrano)
                    odabraniUpgrade = UI.odabraniUpgrade(mousex, mousey)
                    #postavljanje parametara upgradeova
                    if odabraniUpgrade is not None:
                        if odabraniUpgrade == upgrade1:
                            if UI.vratiNovce() >= cijenau1:
                                dmg1 = dmg1 + 1
                                UI.azurirajNovce(-cijenau1)
                                cijenau1 = cijenau1 + 1
                                for i in tornjevi:
                                    if i.vratiTip() == 1:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade2:
                            if UI.vratiNovce() >= cijenau2:
                                dmg2 = dmg2 + 1
                                UI.azurirajNovce(-cijenau2)
                                cijenau2 = cijenau2 + 1
                                for i in tornjevi:
                                    if i.vratiTip() == 2:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade3:
                            if UI.vratiNovce() >= cijenau3:
                                dmg3 = dmg3 + 1
                                UI.azurirajNovce(-cijenau3)
                                cijenau3 = cijenau3 + 1
                                for i in tornjevi:
                                    if i.vratiTip() == 3:
                                        i.upgradeDMG(1)
                        if odabraniUpgrade == upgrade4:
                            if UI.vratiNovce() >= cijenau4:
                                dmg4 = dmg4 + 50
                                UI.azurirajNovce(-cijenau4)
                                cijenau4 = cijenau4 + 3
                                for i in tornjevi:
                                    if i.vratiTip() == 4:
                                        i.upgradeDMG(50)
                        if odabraniUpgrade == upgrade5:
                            if UI.vratiNovce() >= cijenau5:
                                dmg5 = dmg5 + 2
                                UI.azurirajNovce(-cijenau5)
                                cijenau5 = cijenau5 + 5
                                for i in tornjevi:
                                    if i.vratiTip() == 5:
                                        i.upgradeDMG(2) 
                #gradnja tornja
                elif not grid[gore][lijevo] == Z and not grid[gore][lijevo] == T:
                    print(odabraniToranj)
                    #stvaranje tornjeva
                    if odabraniToranj is not None:
                        if odabraniToranj == toranj1:
                            if UI.vratiNovce() >= cijena1:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(1, brzinaP1, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet1, dmg1, ASpeed1, toranj1slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena1)
                                cijena1 = cijena1 + 10
                        if odabraniToranj == toranj2:
                            if UI.vratiNovce() >= cijena2:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(2, brzinaP2, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet2, dmg2, ASpeed2, toranj2slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena2)
                                cijena2 = cijena2 + 10
                        if odabraniToranj == toranj3:
                            if UI.vratiNovce() >= cijena3:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(3, brzinaP3, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet3, dmg3, ASpeed3, toranj3slika, pucanjZvuk))
                                UI.azurirajNovce(-cijena3)
                                cijena3 = cijena3 + 10
                        if odabraniToranj == snajper:
                            if UI.vratiNovce() >= cijena4:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(4, brzinaP4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet4, dmg4, ASpeed4, snajperslika, pucanjZvuk))
                                UI.azurirajNovce(-cijena4)
                                cijena4 = cijena4 + 20
                        if odabraniToranj == mitraljez:
                            if UI.vratiNovce() >= cijena5:
                                grid[gore][lijevo] = T
                                tornjevi.append(toranj(5, brzinaP5, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, domet5, dmg5, ASpeed5, mitraljezslika, pucanjZvuk))
                                UI.azurirajNovce(-cijena5)
                                cijena5 = cijena5 + 20
            if not kliknuto:
                UI.crtajObrub(mousex, mousey)
            #Damage
            for i in range (len(tornjevi)):
                tornjevi[i - 1].Crtaj()
                dmgLista.append(tornjevi[i - 1].Ciljanje(NeprijateljiRect, metakIkona))
            if dmgLista != []:
                for j in dmgLista:
                    for i in j:
                        if i[0] > -1 and listaNeprijatelj:
                            listaNeprijatelj[i[0]].damage(i[1])
                            if listaNeprijatelj[i[0]].vratiHP() < 1:
                                smrtZvuk.play(0)
                                UI.azurirajNovce(5)
                                listaNeprijatelj.remove(listaNeprijatelj[i[0]])
            indekas = GlZgrada.damage(NeprijateljiRect)
            if indekas > -1:
                listaNeprijatelj.remove(listaNeprijatelj[indekas])
                indekas = -1
            trenutnoNeprijatelja, ukupnoNeprijatelja = lvlSeed.ukupnoNeprijatelja()
            UI.ispisStanja(GlZgrada.vratiHP(), trenutnoNeprijatelja, ukupnoNeprijatelja)
            #uvijeti kraja igre
            if GlZgrada.vratiHP()[0] <= 0 or (len(listaNeprijatelj) < 1 and pocetak == 0):
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('glazba/menu.ogg')
                pygame.mixer.music.play()
                pocetak = 1
                if GlZgrada.vratiHP()[0] <= 0:
                    print("Izgubljeno")
                    mod = modIzgubljeno
                else:
                    print("Pobjeda")
                    mod = modPobjeda
                odabraniLvl = None
                listaNeprijatelj = []
                grid = []
                UI.postaviNovce(0)
                lvlSeed.reset()
                startVrijeme = 1
                startKliknut = 0
        if audio:
            pygame.mixer.unpause()
            pygame.mixer.music.set_volume(0.3)
        else:
            pygame.mixer.pause()
            pygame.mixer.music.set_volume(0)
        pygame.display.update()
        POVRSINA.blit(pozadina, ((0, 0), (840, 480)))
        FPSCLOCK.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()