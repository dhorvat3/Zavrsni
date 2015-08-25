import pygame

class neprijatelj(object):
    """Klasa neprijatelja"""
    def __init__(self, polje, Visina, Sirina, pocetak, kraj, POV, brzina, smjer, ikona, HP):
        self.grid = polje
        self.visina = Visina
        self.sirina = Sirina
        self.brojRedova = len(self.grid)
        self.brojStupaca = len(self.grid[0])
        self.start = pocetak
        self.kraj = kraj
        self.POVRSINA = POV
        self.v = brzina
        self.s = smjer
        self.ikona = ikona
        self.ikonaRect = self.ikona.get_rect()
        self.ikonaRect.x = self.visina/self.brojRedova*(self.start[1])
        self.ikonaRect.y = self.sirina/self.brojStupaca*(self.start[0] - 1)
        self.x = self.start[0]
        self.y = self.start[1]
        self.POVRSINA.blit(self.ikona, self.ikonaRect.topleft)
        self.MaxHP = HP
        self.trenutniHP = HP
        self.font = pygame.font.SysFont("monospace", 10)
    def lijevoGore(self, boxx, boxy, sirina, visina, brojRedova, brojStupaca):
        trecinax = int(sirina/brojRedova)
        trecinay = int(visina/brojStupaca)

        lijevo = boxx * trecinax
        gore = boxy * trecinay
        return (lijevo, gore)
    def poljeNaPixelu(self, gornja, lijeva, donja, desna, sirina, visina, brojRedova, brojStupaca):
        for boxx in range(brojRedova):
            for boxy in range(brojStupaca):
                lijevo, gore = self.lijevoGore(boxx, boxy, sirina, visina, brojRedova, brojStupaca)
                boxRect = pygame.Rect(lijevo, gore, sirina/brojRedova, visina/brojStupaca)
                if boxRect.collidepoint(gornja, lijeva) and boxRect.collidepoint(donja, desna):
                    return (boxx, boxy)
        return (None, None)

    def damage(self, iznos):
        self.trenutniHP = self.trenutniHP - iznos
    def vratiHP (self):
        return self.trenutniHP
    def Pomakni(self):
        Gore = self.ikonaRect.top
        Lijevo = self.ikonaRect.left
        Dolje = self.ikonaRect.bottom
        Desno = self.ikonaRect.right
        polaX = self.visina/self.brojRedova/2
        polaY = self.sirina/self.brojStupaca/2
        brzina = self.v
        brzinaX = 0
        brzinaY = 0
        PovratnaX, PovratnaY = self.poljeNaPixelu(Gore, Lijevo, Dolje, Desno, self.sirina, self.visina, self.brojRedova, self.brojStupaca)
        if self.v == 0:
            return
        if PovratnaX != None and PovratnaY != None and (self.x != PovratnaX or self.y != PovratnaY):
            self.x = PovratnaX
            self.y = PovratnaY
            if self.x < self.brojRedova - 1 and self.y < self.brojStupaca - 1:
                if self.s == 'U' and self.grid[self.x - 1][self.y] != 'Z':
                    if self.grid[self.x][self.y - 1] == 'Z':
                        self.s = 'L'
                    if self.grid[self.x][self.y + 1] == 'Z':
                        self.s = 'R'
                if self.s == 'R' and self.grid[self.x][self.y + 1] != 'Z':
                    if self.grid[self.x - 1][self.y] == 'Z':
                        self.s = 'U'
                    if self.grid[self.x + 1][self.y] == 'Z':
                        self.s = 'D'
                if self.s == 'L' and self.grid[self.x][self.y - 1] != 'Z':
                    if self.grid[self.x - 1][self.y] == 'Z':
                        self.s = 'U'
                    if self.grid[self.x + 1][self.y] == 'Z':
                        self.s = 'D'
                if self.s == 'D' and self.grid[self.x + 1][self.y] != 'Z':
                    if self.grid[self.x][self.y - 1] == 'Z':
                        self.s = 'L'
                    if self.grid[self.x][self.y + 1] == 'Z':
                        self.s = 'R'
            if self.x == self.brojRedova - 1 or self.x == 0 or self.y == self.brojStupaca - 1:
                if self.x == self.brojRedova - 1:
                    if self.y == 0:
                        if self.s == 'L':
                            self.s = 'U'
                        else:
                            self.s = 'R'
                    elif self.s == 'D':
                        if self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        else:
                            self.s = 'R'
                    elif self.s == 'R':
                        if self.grid[self.x][self.y + 1] == 'Z':
                            self.s = 'R'
                        elif self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        if self.grid[self.x - 1][self.y] == 'Z':
                            self.s = 'U'
                    elif self.s == 'L':
                        if self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        elif self.grid[self.x][self.y + 1] == 'Z':
                            self.s = 'R'
                        else:
                            self.s = 'U'
                elif self.x == 0:
                    if self.y == self.brojStupaca - 1:
                        if self.s == 'R':
                            self.s = 'D'
                        else:
                            self.s = 'L'
                    elif self.s == 'R':
                        if self.grid[self.x][self.y + 1] == 'Z':
                            self.s = 'R'
                        elif self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        if self.grid[self.x + 1][self.y] == 'Z':
                            self.s = 'D'
                    elif self.s == 'L':
                        if self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        elif self.grid[self.x][self.y + 1] == 'Z':
                            self.s = 'R'
                        else:
                            self.s = 'D'
                    elif self.s == 'U':
                         if self.grid[self.x][self.y - 1] == 'Z':
                                self.s = 'L'
                         elif self.grid[self.x][self.y + 1] == 'Z':
                                self.s = 'R'
                elif self.y == self.brojStupaca - 1:
                    if self.s == 'R':
                        if self.grid[self.x - 1][self.y] == 'Z':
                            self.s = 'U'
                        elif self.grid[self.x + 1][self.y] == 'Z':
                            self.s = 'D'
                    elif self.s == 'D':
                        if self.grid[self.x - 1][self.y] == 'Z':
                            self.s = 'U'
                        if self.grid[self.x + 1][self.y] == 'Z':
                            self.s = 'D'
                        else:
                            self.s = 'L'
                    elif self.s == 'U':
                        if self.grid[self.x - 1][self.y] == 'Z':
                            self.s = 'U'
                        elif self.grid[self.x][self.y - 1] == 'Z':
                            self.s = 'L'
                        elif self.grid[self.x + 1][self.y] == 'Z':
                            self.s = 'D'
        if self.s == 'D':
            brzinaY = brzina
        if self.s == 'U':
            brzinaY = -brzina
        if self.s == 'L':
            brzinaX = -brzina
        if self.s == 'R':
            brzinaX = brzina
        if self.x == self.kraj[0] and self.y == self.kraj[1]:
            self.v = 0;
        lblHP = self.font.render((str(self.trenutniHP) + "/" + str(self.MaxHP)), 1, (0, 0, 0))
        self.ikonaRect = self.ikonaRect.move([brzinaX, brzinaY])
        postotak = int((self.trenutniHP/self.MaxHP*100)/2)
        for i in range(50):
            if i < postotak:
                pygame.draw.rect(self.POVRSINA, (255, 47, 15), (self.ikonaRect.x + i, self.ikonaRect.y - 3, 1, 2))
            else:
                pygame.draw.rect(self.POVRSINA, (0 , 0, 0), (self.ikonaRect.x + i, self.ikonaRect.y - 3, 1, 2))
        self.POVRSINA.blit(self.ikona, self.ikonaRect.topleft)
        self.POVRSINA.blit(lblHP, self.ikonaRect.topleft)