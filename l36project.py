import pygame

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Colour Changing Sprite")

squarewidth = 60
squareheight = 60
squarewidth1 = 60
squareheight2 = 60
currentcolour = "green"
currentcolour1 = "orange"


squarex = 30
squarey = 30
squarex1 = 90
squarey2 = 90

run = True 
while run:
    screen.fill("red") 
    pygame.draw.rect(screen,currentcolour,(squarex, squarey, squarewidth, squareheight))
    pygame.draw.rect(screen,currentcolour1,(squarex1, squarey2, squarewidth, squareheight))
    for i in pygame.event.get():
        if i.type == pygame.QUIT: 
            pygame.quit()
        press = pygame.key.get_pressed() 
        if press[pygame.K_LEFT]: 
            squarex = squarex - 20
            squarex1 = squarex1 + 20
            currentcolour = "yellow"
            currentcolour1 = "black"
        elif press[pygame.K_RIGHT]: 
            squarex = squarex + 20
            squarex1 = squarex1 - 20
            currentcolour = "blue"
            currentcolour1 = "purple"
        elif press[pygame.K_UP]: 
            squarey = squarey + 20
            squarey2 = squarey2 - 20
            currentcolour = "pink"
            currentcolour1 = "white"
        elif press[pygame.K_DOWN]: 
            squarey = squarey + 20
            squarey2 = squarey2 - 20
            currentcolour = "orange"
            currentcolour1 = "brown"
        else:
            currentcolour = "green"
            currentcolour1 = "orange"


    pygame.display.update()
pygame.quit()