import pygame
import pymunk
pygame.init()
window=pygame.display.set_mode((506,862))
pygame.display.set_caption("Rasitin Oyunu")
close=True
arka_plan = pygame.image.load("background-day.png")
window.blit(arka_plan, (0,0))
pygame.display.flip()
x=253
y=431
hiz=0.4
space = pymunk.Space()
space.gravity = (0.0, -900.0)

while close:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            close=False


    keys= pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        y-=hiz


    bird = pygame.image.load("yellowbird-upflap.png")
    window.blit(bird, (x,y))
    pygame.display.flip()


pygame.quit()
