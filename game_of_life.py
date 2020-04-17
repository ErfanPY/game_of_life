import random
import os
import time

class universe :
    def __init__ (self, h, w):
        self.w = w
        self.h = h
        self.world = self.rand_world()

    def clear (self):
        for y in range(self.h):
            for x in range(self.w):
                self.world[y][x] = 0
    
    def rand(self):
        ran = random.random()
        if ran < 0.1:
            return 1
        return 0

    def rand_world (self):
        new = []
        for y in range(self.h):
            new.append([])
            for x in range(self.w):
                new[-1].append(self.rand())
        return new

    def draw(self):
        os.system('cls')
        for y in range(self.h):
            for x in range(self.w):
                if self.world[y][x]:
                    print('#', end=' ')
                else :
                    print(' ', end=' ')
            print()

    def asci_to_pat (self, asci, distance=' '):
        res_pat = []
        list_asci = asci.split('\n')
        
        for yd, y in enumerate(list_asci) :
            res_pat.append([])
            for xd, x in enumerate(y):
                if x != distance :
                    res_pat[-1].append(1)
                else :
                    res_pat[-1].append(0)
        return res_pat
    
    def add_pat (self, pat, y_start = 0, x_start = 0):
        for y, y_value in enumerate(pat):
            for x, x_value in enumerate(y_value):
                self.world[(y + y_start + self.h) % self.h][(x + x_start + self.w) % self.w] = x_value

    def evolution(self):
        new = []
        for y in range(self.h):
            new.append([])
            for x in range(self.w):
                new[-1].append(self.world[y][x])

        for x in range(self.w):
            for y in range(self.h):
                lives = 0
                for xd in range(x-1, x+2):
                    for yd in range(y-1, y+2):
                        if self.world[( yd + self.h) % self.h][(xd + self.w) % self.w]:
                            lives += 1
                if self.world[y][x]: lives -= 1
                if lives == 3 :
                    new[y][x] = 1
                elif lives == 2 and self.world[y][x]==1 :
                    new[y][x] = 1
                else:
                    new[y][x] = 0
        self.world = new


if __name__ == "__main__":
    h,w = 40, 40
    u = universe(h, w)
    while 1:
        u.draw()
        u.evolution()
        time.sleep(1)
