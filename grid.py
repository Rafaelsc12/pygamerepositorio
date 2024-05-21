import pygame
from cores import Cores

class Grid:
    def __init__(self):
        self.num_linhas = 20
        self.num_colunas = 10
        self.tamanho_celula = 30
        self.grade = [[0 for _ in range(self.num_colunas)] for _ in range(self.num_linhas)]
        self.cores = Cores.obter_cores_celulas()


    def imprimir_grade(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                print(self.grade[linha][coluna], end=" ")
            print()

    def esta_dentro(self, linha, coluna):
        return 0 <= linha < self.num_linhas and 0 <= coluna < self.num_colunas

    def esta_vazia(self, linha, coluna):
        return self.grade[linha][coluna] == 0

    def linha_cheia(self, linha):
        for coluna in range(self.num_colunas):
            if self.grade[linha][coluna] == 0:
                return False
        return True

    def limpar_linha(self, linha):
        for coluna in range(self.num_colunas):
            self.grade[linha][coluna] = 0

    def mover_linha_para_baixo(self, linha, num_linhas):
        for coluna in range(self.num_colunas):
            self.grade[linha + num_linhas][coluna] = self.grade[linha][coluna]
            self.grade[linha][coluna] = 0

    def limpar_linhas_completas(self):
        completadas = 0
        for linha in range(self.num_linhas - 1, 0, -1):
            if self.linha_cheia(linha):
                self.limpar_linha(linha)
                completadas += 1
            elif completadas > 0:
                self.mover_linha_para_baixo(linha, completadas)
        return completadas

    def resetar(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                self.grade[linha][coluna] = 0

    def desenhar(self, tela):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                valor_celula = self.grade[linha][coluna]
                retangulo_celula = pygame.Rect(coluna * self.tamanho_celula + 11, linha * self.tamanho_celula + 11,
                                               self.tamanho_celula - 1, self.tamanho_celula - 1)
                pygame.draw.rect(tela, self.cores[valor_celula], retangulo_celula)

    def preencher_posicao(self, linha, coluna, valor):
        if self.esta_dentro(linha, coluna):
            self.grade[linha][coluna] = valor

    def remover_linhas_vazias(self):
        linhas_removidas = 0
        nova_grade = [linha for linha in self.grade if any(celula != 0 for celula in linha)]
        linhas_removidas = self.num_linhas - len(nova_grade)
        self.grade = [[0 for _ in range(self.num_colunas)] for _ in range(linhas_removidas)] + nova_grade
        return linhas_removidas

    def imprimir_grade_colorida(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                valor_celula = self.grade[linha][coluna]
                cor = self.cores[valor_celula]
                print(f"\033[48;2;{cor[0]};{cor[1]};{cor[2]}m {valor_celula} \033[0m", end="")
            print()
