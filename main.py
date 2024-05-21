import pygame, sys
from game import Game
from cores import Cores

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Cores.branco)
next_surface = title_font.render("Next", True, Cores.branco)
game_over_surface = title_font.render("GAME OVER", True, Cores.branco)
hold_surface = title_font.render("Hold", True, Cores.branco)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
hold_rect = pygame.Rect(320, 430, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

# Definindo uma variável para controlar se a seta para baixo está pressionada continuamente
down_pressed = False

fall_speed=1000 #Vel inicial


GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, fall_speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            if not game.game_over:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    down_pressed = True
                    fall_speed = 150  # 50 milissegundos
                    pygame.time.set_timer(GAME_UPDATE, fall_speed)
                if event.key == pygame.K_UP:
                    game.rotate()
                # Se pressionar a tecla "C" para armazenar a peça
                if event.key == pygame.K_c:
                    game.hold_piece()
        # Verificar se a seta para baixo foi solta
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                down_pressed = False
                # Restaurar a velocidade de queda normal
                fall_speed = 1000  # 1000 milissegundos
                pygame.time.set_timer(GAME_UPDATE, fall_speed)
        if event.type == GAME_UPDATE and not game.game_over:
            # Se a seta para baixo está pressionada continuamente, mover para baixo
            if down_pressed:
                game.move_down()
                game.update_score(0, 1)
            # Se não, continuar o jogo normalmente
            else:
                game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Cores.branco)
    screen.fill(Cores.azul_escuro)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    screen.blit(hold_surface, (365, 395, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Cores.azul_claro, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Cores.azul_claro, next_rect, 0, 10)
    pygame.draw.rect(screen, Cores.azul_claro, hold_rect, 0, 10)
    game.draw(screen, title_font)

    pygame.display.update()
    clock.tick(60)
