import pygame
pygame.init()
import random
import time

width = 500
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flipbook")

image1 = pygame.image.load("gaming library/1flip.png")
image2 = pygame.image.load("gaming library/2flip.png")
image3 = pygame.image.load("gaming library/3flip.png")
image4 = pygame.image.load("gaming library/4flip.png")
image5 = pygame.image.load("gaming library/5flip.png")
image6 = pygame.image.load("gaming library/6flip.png")
image7 = pygame.image.load("gaming library/7flip.png")
image8 = pygame.image.load("gaming library/8flip.png")
image9 = pygame.image.load("gaming library/9flip.png")
image10 = pygame.image.load("gaming library/10flip.png")
image11 = pygame.image.load("gaming library/11flip.png")
image12 = pygame.image.load("gaming library/12flip.png")
image1 = pygame.transform.scale(image1,(width,height))
image2 = pygame.transform.scale(image2,(width,height)) 
image3 = pygame.transform.scale(image3,(width,height)) 
image4 = pygame.transform.scale(image4,(width,height))
image5 = pygame.transform.scale(image5,(width,height)) 
image6 = pygame.transform.scale(image6,(width,height)) 
image7 = pygame.transform.scale(image7,(width,height))
image8 = pygame.transform.scale(image8,(width,height)) 
image9 = pygame.transform.scale(image9,(width,height)) 
image10 = pygame.transform.scale(image10,(width,height))
image11 = pygame.transform.scale(image11,(width,height)) 
image12 = pygame.transform.scale(image12,(width,height))


run = True
while run:
    screen.fill("red") 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: 
            pygame.quit()

    #image1
    screen.blit(image1,(0,0))
    pygame.display.update()
    time.sleep(0.10) 
    #image2
    screen.blit(image2,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image3
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image4
    screen.blit(image4,(0,0))
    pygame.display.update()
    time.sleep(0.10) 
    #image5
    screen.blit(image5,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image6
    screen.blit(image6,(0,0))
    pygame.display.update()
    time.sleep(0.10)
     #image7
    screen.blit(image7,(0,0))
    pygame.display.update()
    time.sleep(0.10) 
    #image8
    screen.blit(image8,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image9
    screen.blit(image9,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image10
    screen.blit(image10,(0,0))
    pygame.display.update()
    time.sleep(0.10) 
    #image11
    screen.blit(image11,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    #image12
    screen.blit(image12,(0,0))
    pygame.display.update()
    time.sleep(0.10)
    