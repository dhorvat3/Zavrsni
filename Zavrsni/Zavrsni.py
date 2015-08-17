﻿#Glavna klasa
import pygame
import sys
from random import randrange
from mapa import Mapa
from neprijatelj import neprijatelj
from sucelje import sucelje
from toranj import toranj
from zgrada import zgrada
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEBUTTONUP, MOUSEMOTION

metakIkona = pygame.image.load('grafika\metak.png')
neprijateljPlaceholder = pygame.image.load('grafika\enemy.png')
glavnaZgrada = pygame.image.load('grafika\zgrada.png')
menuSlika = pygame.image.load('grafika\menu_obrub.png')
toranj1ikona = pygame.image.load('grafika/toranj1_ikona.png')
toranj2ikona = pygame.image.load('grafika/toranj2_ikona.png')
toranj3ikona = pygame.image.load('grafika/toranj3_ikona.png')
slikaHover = pygame.image.load('grafika/hover.png')
slikaOdabrano = pygame.image.load('grafika/odabrano.png')
menuLvl1 = pygame.image.load('grafika/menuLvl1.png')
menuHover = pygame.image.load('grafika/menuHover.png')

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
toranj1 = 'Toranj1'
toranj2 = 'Toranj2'
toranj3 = 'Toranj3'
modMenu = 'menu'
modIgra = 'igra'
#mod = modMenu

#opis mape
grid = [
#0  1  2  3  4  5  6  7  8  9
[S, S, S, S, S, S, S, S, S, S],#0
[Z, Z, Z, S, S, S, S, S, S, S],#1
[S, S, Z, S, S, S, S, S, S, S],#2
[Z, Z, Z, S, S, S, S, S, S, S],#3
[Z, S, S, S, Z, Z, Z, S, S, S],#4
[Z, Z, S, S, Z, S, Z, S, S, S],#5
[S, Z, Z, Z, Z, S, Z, Z, Z, S],#6
[S, S, S, S, S, S, S, S, Z, S],#7
[S, S, S, S, S, S, S, S, Z, S],#8
[S, S, S, S, S, S, S, S, Z, S] #9
]
start = [2, 0]
kraj = [9, 8]
brojNeprijatelja = 4
startGold = 100
#kraj opisa mape

def main ():
    global FPSCLOCK, POVRSINA;

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    POVRSINA = pygame.display.set_mode((UkupnaVisina, SirinaProzora), 0, 32)

    ##lvl = Mapa(grid, VisinaProzora, SirinaProzora)
    ##listaNeprijatelj = [neprijatelj(grid, VisinaProzora, SirinaProzora, start, kraj, POVRSINA, randrange(10) + 1, R, neprijateljPlaceholder, 15) for i in range (brojNeprijatelja)]
    ##tornjevi = []
    ##GlZgrada = zgrada(POVRSINA, glavnaZgrada, 15, kraj, VisinaProzora, SirinaProzora, grid)
    UI = sucelje(VisinaProzora, SirinaProzora, grid, POVRSINA, startGold, menuHover, menuLvl1)
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Saki dan dolazu')
    odabraniToranj = None
    odabraniLvl = None
    mod = modMenu

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
            #UI.crtajGlavniMenu()
            if kliknuto:
                odabraniLvl = UI.kliknutoGlavniMenu(mousex, mousey)
                if odabraniLvl == 'Lvl1':
                    mod = modIgra
                    ##Tu bi trebalo maestro pozivi biti tipa if odabraniLvl is not None: grid = maestro.grid(odabraniLvl), start = maestro.start(odaraniLvl) itd.
                    lvl = Mapa(grid, VisinaProzora, SirinaProzora)
                    listaNeprijatelj = [neprijatelj(grid, VisinaProzora, SirinaProzora, start, kraj, POVRSINA, randrange(10) + 1, R, neprijateljPlaceholder, 15) for i in range (brojNeprijatelja)]
                    tornjevi = []
                    GlZgrada = zgrada(POVRSINA, glavnaZgrada, 15, kraj, VisinaProzora, SirinaProzora, grid)
                    ##do ovđe
            if not kliknuto:
                UI.hoverGlavniMenu(mousex, mousey)
            UI.crtajGlavniMenu()
        if mod == modIgra:
            NeprijateljiRect = []
            GlZgrada.crtaj()
            for i in range (len(listaNeprijatelj)):
                listaNeprijatelj[i].Pomakni()
            for i in range (len(listaNeprijatelj)):
                NeprijateljiRect.append(listaNeprijatelj[i].ikonaRect)
            lvl.crtajMrezu(POVRSINA)
            if kliknuto:
                lijevo, gore = UI.poljeNaPixelu(mousex, mousey)
                if lijevo is None and gore is None:
                    odabraniToranj = UI.odabraniToranj(mousex, mousey, slikaOdabrano)
                elif not grid[gore][lijevo] == Z:
                    if odabraniToranj is not None:
                        grid[gore][lijevo] = T
                        if odabraniToranj == toranj1:
                            if UI.vratiNovce() > 10:
                                tornjevi.append(toranj(4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 100, 5))
                                UI.azurirajNovce(-10)
                        if odabraniToranj == toranj2:
                            if UI.vratiNovce() > 20:
                                tornjevi.append(toranj(4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 200, 5))
                                UI.azurirajNovce(-20)
                        if odabraniToranj == toranj3:
                            if UI.vratiNovce() > 30:
                                tornjevi.append(toranj(4, gore, lijevo, grid, POVRSINA, VisinaProzora, SirinaProzora, 200, 10))
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
                index, damage = tornjevi[i - 1].Ciljanje(NeprijateljiRect, metakIkona)
                #print (index)
                if index > -1:
                    print (index)
                    listaNeprijatelj[index].damage(damage)
                    if listaNeprijatelj[index].vratiHP() < 1:
                        UI.azurirajNovce(30)
                        listaNeprijatelj.remove(listaNeprijatelj[index])
                    index = -1
            indekas = GlZgrada.damage(NeprijateljiRect)
            if indekas > -1:
                print ("Damage: ", indekas)
                listaNeprijatelj.remove(listaNeprijatelj[indekas])
                indekas = -1
            UI.ispisStanja(GlZgrada.vratiHP())
            if len(listaNeprijatelj) < 1:
                print ("Pobeda")
                mod = modMenu
                #main()
            UI.menu(menuSlika, toranj1ikona, toranj2ikona, toranj3ikona)
        pygame.display.update()
        POVRSINA.fill((0,15,0))
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()