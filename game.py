import random
import pygame
from grid import Grid
from blocos import BlocoI, BlocoJ, BlocoL, BlocoO, BlocoS, BlocoT, BlocoZ
from cores import Cores

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.stored_block = None
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.turn_complete = True
        self.can_hold = True
        self.next_block_changed = False

    def hold_piece(self):
        if self.turn_complete and self.can_hold:
            if self.stored_block is None:
                self.stored_block = self.current_block.__class__()
                self.stored_block.celulas = self.current_block.celulas.copy()
                self.stored_block.estado_rotacao = self.current_block.estado_rotacao
                self.current_block = self.next_block
                self.next_block = self.get_random_block()
                self.turn_complete = False
            else:
                stored_copy = self.stored_block.__class__()
                stored_copy.celulas = self.stored_block.celulas.copy()
                stored_copy.estado_rotacao = self.stored_block.estado_rotacao
                self.stored_block = self.current_block.__class__()
                self.stored_block.celulas = self.current_block.celulas.copy()
                self.stored_block.estado_rotacao = self.current_block.estado_rotacao
                self.current_block = stored_copy
                self.turn_complete = False
                self.can_hold = False

    def lock_block(self):
        cells = self.current_block.obter_posicoes_celulas()
        for posicao in cells:
            self.grid.grade[posicao.linha][posicao.coluna] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.next_block_changed = True
        rows_cleared = self.grid.limpar_linhas_completas()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True
        self.turn_complete = True

    def update_score(self, lines_cleared, move_down_points):
        points = {1: 100, 2: 300, 3: 500, 4: 1000}
        self.score += points.get(lines_cleared, 0) + move_down_points
        self.lines_cleared += lines_cleared
        self.level = self.lines_cleared // 10 + 1

    def get_random_block(self):
        if not self.blocks:
            self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.mover(0,-1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.mover(0,1)

    def move_right(self):
        self.current_block.mover(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.mover(0, -1)

    def move_down(self):
        self.current_block.mover(1, 0)
        if not self.block_inside() or not self.block_fits() :
            self.current_block.mover(-1, 0)
            self.lock_block()

    def reset(self):
        self.grid.resetar()
        self.blocks = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.stored_block = None  # Define a peça armazenada como None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.can_hold = True
        self.next_block_changed = False

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

    def draw(self, screen, font):
        self.grid.desenhar(screen)
        self.current_block.desenhar(screen, 11, 11)
        

        if self.next_block_changed:
            self.can_hold = True
            self.next_block_changed = False
        
        if self.next_block.id == 3:
            self.next_block.desenhar(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.desenhar(screen, 255, 280)
        else:
            self.next_block.desenhar(screen, 270, 270)
        
        # Desenha a peça armazenada (se houver)
        if self.stored_block is not None:
            if self.stored_block.id == 3:
                self.stored_block.desenhar(screen, 253, 505)
            elif self.stored_block.id == 4:
                self.stored_block.desenhar(screen, 255, 490)
            else:
                self.stored_block.desenhar(screen, 270, 485)
