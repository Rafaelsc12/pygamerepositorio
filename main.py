import sys
import pygame
from grid import Grid
azul = (60, 80, 140)
pygame.init() #Inicia o game

tela = pygame.display.set_mode((330, 660)) #Criação da resolução da janela
pygame.display.set_caption("Tetris") #Nome da janela

fps = pygame.time.Clock()
              
game_grid = Grid()

game_grid.print_grid

game = True 

while game: #Loop do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Cores da tela 
    tela.fill(azul)

    game_grid.pintura(tela)
    pygame.display.update()
    fps.tick(60) #Determina 60 frames por segundo 



