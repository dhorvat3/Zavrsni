import pygame

class maestro(object):
    """Klasa zadužena za kreiranje levela."""
    def __init__(self):
        self.Lvl = []
        self.seed = None
        self.index = 0
        self.pocetno = pygame.time.get_ticks()
        self.razmak = 500
    def postaviVrijeme(self):
        self.pocetno = pygame.time.get_ticks()
    def lvlLoad(self, odabraniLvl):
        f = open('lvl/' + str(odabraniLvl) + '.txt')
        redovi = f.readlines()
        f.close()
        for red in redovi:
            self.Lvl.append(red.split())
        self.seed = self.Lvl[15]
        #for i in self.seed:
        #    i = int(i)
        for i in range(len(self.seed)):
            self.seed[i] = int(self.seed[i])
    def grid(self):
        grid = []
        for i in range(0, 10):
            grid.append(self.Lvl[i])
        return grid
    def start(self):
        return int(self.Lvl[10][0]), int(self.Lvl[10][1])
    def kraj(self):
        return int(self.Lvl[11][0]), int(self.Lvl[11][1])
    def brNeprijatelja(self):
        return int(self.Lvl[12][0])
    def startGold(self):
        return int(self.Lvl[13][0])
    def zgradaHP(self):
        return int(self.Lvl[14][0])
    def obrisiLvl(self):
        self.Lvl = []
    def vrijeme(self):
        trenutno = pygame.time.get_ticks()
        if trenutno - self.pocetno >= (self.razmak * (self.index + 1)):
            print ("vrijeme ", trenutno - self.pocetno)
            self.pocetno = trenutno
            return 1
        else:
            return 0
    def vratiNeprijatelj(self):
        if self.index > self.brNeprijatelja() - 1:
            return None, None, None
        if self.seed[self.index] == 0:
            self.index = self.index + 1
        if self.index > self.brNeprijatelja() - 1:
            return None, None, None
        self.seed[self.index] = self.seed[self.index] - 1
        if self.index == 0:
            return 1, 3, 10
        elif self.index == 1:
            return 2, 2, 30
        elif self.index == 2:
            return 3, 2, 50
        elif self.index == 3:
            return 4, 1, 70
        elif self.index == 4:
            return 5, 2, 100
        elif self.index == 5:
            return 6, 3, 150
        elif self.index == 6:
            return 7, 2, 200
        elif self.index == 7:
            return 8, 3, 300
    def reset(self):
        self.Lvl = []
        self.seed = None
        self.index = 0
        self.pocetno = pygame.time.get_ticks()