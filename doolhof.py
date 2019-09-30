import os
import time
from worm import Worm
import random

max_generations = 120
max_worms = 100
generation = 0
average_fitness = 0
doolhof = []
fit_pool = []
total_fitness = 0
with open('doolhof1.txt', 'r') as file:
    for line in file:
        doolhof.append(line.rstrip())
doolhof_size = (len(doolhof[0]), len(doolhof))

worms = [Worm() for i in range(max_worms)]
exit_found = False

while not exit_found:
    os.system('clear')
    print(f"==== {generation} avg_fit:{average_fitness} total:{len(worms)} ====")
    for w in worms:
        w.tick()
    deaths = []
    for row in range(0, doolhof_size[1]):
        line = doolhof[row]
        for col in range(0, len(doolhof[row])):
            for w in worms:
                if w.pos[0] == col and w.pos[1] == row:
                    if doolhof[row][col] == '.':
                        exit_found = True
                    if doolhof[row][col] == "*" or w.life_index >= len(w.dna) - 1:
                        deaths.append(w)
                    else:
                        line = line[:col] + "o" + line[col + 1:]
        print(line)
    for d in deaths:
        worms.remove(d)
        fitness = d.pos[0] * 2 * (d.life_index + 1)
        total_fitness = total_fitness + fitness
        for i in range(0, fitness):
            fit_pool.append(d)
    time.sleep(.01)
    if len(worms) == 0:
        average_fitness = total_fitness / max_worms
        total_fitness = 0
        for i in range(max_worms):
            p1 = random.choice(fit_pool)
            p2 = random.choice(fit_pool)
            worms.append(Worm(dna1=p1.dna, dna2=p2.dna))
        fit_pool = []
        generation = generation + 1
print('Found the exit!!!')
