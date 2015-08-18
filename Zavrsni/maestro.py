class maestro(object):
    """description of class"""
    def __init__(self):
        self.Lvl = []
    def lvlLoad(self, odabraniLvl):
        f = open('lvl/' + str(odabraniLvl) + '.txt')
        redovi = f.readlines()
        f.close()
        for red in redovi:
            self.Lvl.append(red.split())
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
    def obrisiLvl(self):
        self.Lvl = []