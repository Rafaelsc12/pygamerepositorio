import main, sys
from grid import Grid
azul = (60, 80, 140)
main.init() #inicia o game

tela = main.display.set_mode((500, 900)) # criação da resolução da janela
main.display.set_caption("Tetris") # nome da janela

fps = main.time.Clock()
              
game_grid = Grid()

game_grid.print_grid

game = True 

while game: # loop do jogo
    for event in main.event.get():
        if event.type == main.QUIT:
            main.quit()
            sys.exit()
    
    # cores da tela 
    tela.fill(azul)

    game_grid.pintura()
    main.display.update()
    fps.tick(60) # determina 60 frames por segundo 



