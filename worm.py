import random


class Worm:
    def __init__(self, dna1=None, dna2=None):
        if dna1 is None:
            self.dna = [(random.randint(-1, 1), random.randint(-1, 1)) for i in range(150)]
        else:
            self.dna = []
            r = random.randint(0, len(dna1))
            for i in range(0, len(dna1) - 1):
                if i < r:
                    self.dna.append(dna1[i])
                elif i < len(dna1) * .95:
                    self.dna.append(dna2[i])
                else:
                    self.dna.append((random.randint(-1, 1), random.randint(-1, 1)))
        self.pos = (2, 2)
        self.life_index = 0

    def tick(self):
        if self.life_index > len(self.dna) - 1:
            print('fout', self.life_index, len(self.dna))
        vector = self.dna[self.life_index]
        self.pos = (self.pos[0] + vector[0], self.pos[1] + vector[1])
        self.life_index = self.life_index + 1
