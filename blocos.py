from posicao import Posicao
from cores import Cores
import pygame
class Bloco:
    def __init__(self, id):
        self.id = id
        self.celulas = {}
        self.tamanho_celula = 30
        self.deslocamento_linha = 0
        self.deslocamento_coluna = 0
        self.estado_rotacao = 0
        self.cores = Cores.obter_cores_celulas()

    def mover(self, linhas, colunas):
        self.deslocamento_linha += linhas
        self.deslocamento_coluna += colunas

    def obter_posicoes_celulas(self):
        celulas = self.celulas[self.estado_rotacao]
        celulas_movidas = []
        for posicao in celulas:
            posicao = Posicao(posicao.linha + self.deslocamento_linha, posicao.coluna + self.deslocamento_coluna)
            celulas_movidas.append(posicao)
        return celulas_movidas

    def rotacionar(self):
        self.estado_rotacao += 1
        if self.estado_rotacao == len(self.celulas):
            self.estado_rotacao = 0

    def desfazer_rotacao(self):
        self.estado_rotacao -= 1
        if self.estado_rotacao == -1:
            self.estado_rotacao = len(self.celulas) - 1

    def desenhar(self, tela, deslocamento_x, deslocamento_y):
        celulas = self.obter_posicoes_celulas()
        for celula in celulas:
            retangulo_celula = pygame.Rect(deslocamento_x + celula.coluna * self.tamanho_celula,
                                           deslocamento_y + celula.linha * self.tamanho_celula,
                                           self.tamanho_celula - 1, self.tamanho_celula - 1)
            pygame.draw.rect(tela, self.cores[self.id], retangulo_celula)

class BlocoL(Bloco):
    def __init__(self):
        super().__init__(id=1)
        self.celulas = {
            0: [Posicao(0, 2), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 0)],
            3: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(2, 1)]
        }
        self.mover(0, 3)

class BlocoJ(Bloco):
    def __init__(self):
        super().__init__(id=2)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 1), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 0), Posicao(2, 1)]
        }
        self.mover(0, 3)

class BlocoI(Bloco):
    def __init__(self):
        super().__init__(id=3)
        self.celulas = {
            0: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(1, 3)],
            1: [Posicao(0, 2), Posicao(1, 2), Posicao(2, 2), Posicao(3, 2)],
            2: [Posicao(2, 0), Posicao(2, 1), Posicao(2, 2), Posicao(2, 3)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(3, 1)]
        }
        self.mover(-1, 3)

class BlocoO(Bloco):
    def __init__(self):
        super().__init__(id=4)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)]
        }
        self.mover(0, 4)

class BlocoS(Bloco):
    def __init__(self):
        super().__init__(id=5)
        self.celulas = {
            0: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 0), Posicao(1, 1)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            2: [Posicao(1, 1), Posicao(1, 2), Posicao(2, 0), Posicao(2, 1)],
            3: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        self.mover(0, 3)

class BlocoT(Bloco):
    def __init__(self):
        super().__init__(id=6)
        self.celulas = {
            0: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        self.mover(0, 3)

class BlocoZ(Bloco):
    def __init__(self):
        super().__init__(id=7)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 2), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 0)]
        }
        self.mover(0, 3)