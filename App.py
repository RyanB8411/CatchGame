# This will be our main app page for the game
# Author RyanB8411

import pygame
import sys
import random

#Variables
pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Yellow Fox Mini Game")
run = True
clock = pygame.time.Clock()

class Mower:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
        
    def move(self):
        self.rect.y += self.speed
        
        
speed = 3
score = 0
lives = 10

#Constants
TILESIZE = 64

#Lower Screen
floor_image = pygame.image.load('assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE*10, TILESIZE))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))

#Fox Character
player_image = pygame.image.load('assets/player_fox.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE*1.5, TILESIZE*1.5))
player_rect = player_image.get_rect(center = (200, 750))

#Mower
mower_image = pygame.image.load('assets/mower.png').convert_alpha()
mower_image = pygame.transform.scale(mower_image, (TILESIZE, TILESIZE))

mowers = [Mower(mower_image, (100, -200), 3),
          Mower(mower_image, (300, -100), 3),
          Mower(mower_image, (200, -300), 3),
          Mower(mower_image, (400, -400), 3),
          Mower(mower_image, (200, 0), 3)]

font = pygame.font.Font(None, 32)


def update():
    global speed, score, lives, run
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        if player_rect.x > 0:
            player_rect.x -= 8
    if keys[pygame.K_RIGHT]:
        if player_rect.x < 300:
            player_rect.x += 8
    if keys[pygame.K_0]:
        lives = 10
        score = 0
        update()
    if mowers.__sizeof__() > 0:        
        for mower in mowers:
            mower.move()
            if mower.rect.colliderect(floor_rect):
                mowers.remove(mower)
                mowers.append(Mower(mower_image, (random.randint(25, 300), -50), random.randint(3, 10)))
                lives -= 1
            if mower.rect.colliderect(player_rect):
                mowers.remove(mower)
                mowers.append(Mower(mower_image, (random.randint(25, 300), -50), random.randint(3, 10)))
                speed += .1
                score += 1
        

def draw():
    screen.fill('light blue')
    screen.blit(floor_image, floor_rect)
    screen.blit(player_image, player_rect)
    
    for mower in mowers:
        screen.blit(mower.image, mower.rect)
        
    score_text = font.render(f"Score: {score}", True, "white") 
    screen.blit(score_text, (5,5))      

def gameover():
    screen.fill('light blue')
    screen.blit(floor_image, floor_rect)
    screen.blit(player_image, player_rect)
    score_text = font.render(f"Score: {score}", True, "white") 
    screen.blit(score_text, (screen.get_width()//2 - 40, screen.get_height()//2)) 
    game_over = font.render("Game Over!", True, ("red"))
    screen.blit(game_over, (screen.get_width()//2 - 58, screen.get_height()//2 - 20))
    
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lives > 0:
        update()  
        draw()
    elif lives == 0:
        gameover()
        pygame.time.wait(2000)
        
    clock.tick(60)
    pygame.display.update()
