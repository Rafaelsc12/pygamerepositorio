import random
import pygame
from grid import Grid
from blocos import BlocoI, BlocoJ, BlocoL, BlocoO, BlocoS, BlocoT, BlocoZ
from cores import Cores

class Game:
    def _init_(self):
        self.grid = Grid()
        self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += move_down_points
        self.lines_cleared += lines_cleared
        self.level = self.lines_cleared // 10 + 1

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.mover(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.mover(0, 1)

    def move_right(self):
        self.current_block.mover(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.mover(0, -1)

    def move_down(self):
        self.current_block.mover(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.mover(-1, 0)
            self.lock_block()

    def lock_block(self):
        cells = self.current_block.obter_posicoes_celulas()
        for posicao in cells:
            self.grid.grade[posicao.linha][posicao.coluna] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.limpar_linhas_completas()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        self.grid.resetar()
        self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False

    def block_fits(self):
        cells = self.current_block.obter_posicoes_celulas()
        for cell in cells:
            if not self.grid.esta_vazia(cell.linha, cell.coluna):
                return False
        return True

    def rotate(self):
        self.current_block.rotacionar()
        if not self.block_inside() or not self.block_fits():
            self.current_block.desfazer_rotacao()

    def block_inside(self):
        cells = self.current_block.obter_posicoes_celulas()
        for cell in cells:
            if not self.grid.esta_dentro(cell.linha, cell.coluna):
                return False
        return True

    def draw(self, screen):
        self.grid.desenhar(screen)
        self.current_block.desenhar(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.desenhar(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.desenhar(screen, 255, 280)
        else:
            self.next_block.desenhar(screen, 270, 270)

    def display_game_info(self, screen, font):
        score_text = font.render(f"Pontuação: {self.score}", True, Cores.branco)
        level_text = font.render(f"Nível: {self.level}", True, Cores.branco)
        screen.blit(score_text, (320, 20))
        screen.blit(level_text, (320, 60))