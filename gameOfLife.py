import pygame
import sys
import time

BACKGROUND_BLUE = (218, 241, 242)
LIVE_CELL = (139, 188, 120)
DEAD_CELL = (37, 3, 71)
STEP = 5
xs = (-STEP, 0, STEP, -STEP, STEP, -STEP, 0, STEP)
ys = (-STEP, -STEP, -STEP, 0, 0, STEP, STEP, STEP)
time = 0

def set_live_cells(screen, cells):
    for point in cells:
        pygame.draw.rect(screen, LIVE_CELL, (point[0], point[1], 5, 5), 0)

def set_dead_cells(screen, cells):
    for point in cells:
        pygame.draw.rect(screen, DEAD_CELL, (point[0], point[1], 5, 5), 0)

def count(cell, living):
    global time
    val = 0
    for i in range(0,8):
        #time = time+1
        if (cell[0]+xs[i], cell[1]+ys[i]) in living:
            val = val+1
    return val

def check_cells(living, dead):
    global time
    dying = []
    #check dying cells
    for cell in living:
        #time = time+1
        #overpopulation
        if count(cell,living)>3:
            dying.append(cell)
        #underpopulation
        if count(cell,living)<2:
            dying.append(cell)

    next_generation = []
    #check births
    for cell in living:
        for i in range(0,8):
            #time = time+1
            if count((cell[0]+xs[i],cell[1]+ys[i]),living)==3:
                next_generation.append((cell[0]+xs[i],cell[1]+ys[i]))

    #update cells
    for cell in dying:
        if cell in living:
            time = time+1
            living.remove(cell)
        #dead.append(cell)
    for cell in next_generation:
        #time = time+1
        living.append(cell)


def display_window(living, dead):
    global time
    pygame.init()
    (width, height) = (800,800)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Conway's Game of Life Simulation")
    done = False
    clock = pygame.time.Clock()
    val = 1
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BACKGROUND_BLUE)
        val = (val+1)%120
        if(val==0):
            time = 0
            print("Start checks ", time)
            check_cells(living, dead)
            print (time)
        set_live_cells(screen, living)
        #set_dead_cells(screen, dead)
        pygame.display.flip()
        clock.tick(60)

def spaceship_glider(living):
    living.append((100,100))
    living.append((105,105))
    living.append((100,110))
    living.append((105,110))
    living.append((95,110))
    return living

def set_initial_live_cells(living):
    living = spaceship_glider(living)
    return living

if __name__ == "__main__" :
    living = []
    dead = []
    living = set_initial_live_cells(living)
    display_window(living, dead)
