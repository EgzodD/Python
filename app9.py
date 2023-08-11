import pygame as pg
import numpy as np

clock = pg.time.Clock()
FPS = 30

WIDTH = 800
HEIGHT = 800

pg.init()


class Projection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        self.background = (10, 10, 60)
        pg.display.set_caption('ASCII 3D EARTH')
        self.surfaces = {}
    
    def addSurface(self, name, surface):
        self.surfaces[name] = surface

    def display(self):
        self.screen.fill(self.background)


class Object:
    def __init__(self):
        self.nodes = np.zeros((0, 4))

    def addNotes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

running = True
while running:

    clock.tick(FPS)

    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()