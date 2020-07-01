# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:12:09 2020

@author: india
"""

import pygame
import random

pygame.init()

#Create Screen
screen=pygame.display.set_mode((800,600))   #width,height  (x,y)

#Title and Logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player Image
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change=0

#Enemy Image
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,740)
enemyY = random.randint(50,250)
enemyX_change = -2

#Bullet Image
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -10
bullet_state = 'ready'

#Background Image
background = pygame.image.load('background.png')

def player(x,y):
    screen.blit(playerImg, (x,y))
    
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16,y + 10))
    

#Game Loop
running = True
while running:
    
    #RGB Color
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            elif event.key == pygame.K_RIGHT:
                playerX_change = +3
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    playerX += playerX_change
    
    #Player Boundary
    if playerX<0:
        playerX=0   
    if playerX>740:
        playerX=740
    
    enemyX += enemyX_change
    
    #Enemy Movement
    if enemyX<0:
        enemyY += 10 
        enemyX_change = 2
    if enemyX>740:
        enemyY += 10
        enemyX_change = -2
        
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
        if bulletY == 0:
            bulletY = 480
            bullet_state = 'ready'
    
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    
    pygame.display.update()  #updates display
    