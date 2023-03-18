import pygame
import sys
import os

pygame.init()  # initialize pygame

clock = pygame.time.Clock()
screenwidth = 480
screenheight = 640
screen = pygame.display.set_mode((screenwidth, screenheight))

# set framerate

framerate = 60

# set background scrolling speed
bg_speed = 100

# load bg image

pygame.mouse.set_visible(0)

pygame.display.set_caption('Queer Space Game')

class HeroShip:
    def __init__(self, screenheight, screenwidth, imagefile):
        self.shape = pygame.image.load(imagefile)
        self.top = screenheight = self.shape.get_height()
         # self.left = screenwidth := screenwidth / 2 = self.shape.get_width()/2  This line is broken
    def Show(self, surface):
        surface.blit(self.shape, (self.left, self.top))
    def UpdateCoords(self, x):
        self.left = x-self.shape.get_width()/2


class ScrollingBackground:
    def __init__(self, screenheight, imagefile):
        self.img = pygame.image.load(imagefile)
        self.coord = [0, 0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]

    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

    def UpdateCoords(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y

        if self.coord2[1] >= 0:
            self.coord[1] = self.y_original
            self.coord2[1] = self.y2_original


StarField = ScrollingBackground(screenheight, "20_(2).jpg")
Hero = HeroShip(screenheight, screenwidth, "Spaceship0-0-1.png")

# fix indentation

while True:
    time = clock.tick(framerate)/1000.0
    print(screenwidth)
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    StarField.UpdateCoords(bg_speed, time)
    StarField.Show(screen)
    pygame.display.update()
