import pygame

pygame.init()

windowsSize = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello World Printer")

myFont = pygame.font.SysFont("DejaVu Sans Mono", 90)

helloWorld = myFont.render("Hello World!", 1, (255, 0, 255), (255, 255, 255))

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
    windowsSize.blit(helloWorld, (0, 0))
    pygame.display.update()