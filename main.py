import pygame
import sys
from grid import Grid
from blocks import *

pygame.init() # Inicia o game
dark_blue = (60, 80, 140)

screen = pygame.display.set_mode((300, 600)) # Criação da resolução da janela
pygame.display.set_caption("Tetris") # Nome da janela

clock = pygame.time.Clock()
              
game_grid = Grid()

block=BlocoL() #So para testar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Cores da tela 
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Determina 60 frames por segundo
