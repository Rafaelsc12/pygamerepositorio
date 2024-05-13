import pygame

class Grid:
    def __init__ (self):
        self.linhas = 22
        self.colunas = 11
        self.cell_tamanho = 33
        self.grid = [[0 for i in range (self.colunas)]for j in range(self.linhas)]
        self.cores = self.cor_das_malhas()

    def print_grid(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                print(self.grid[linha][coluna], end = ' ') 
            print ()

    def cor_das_malhas (self):
        cinza_escuro = (26, 31, 40)
        verde = (47, 230, 23)
        vermelho = (232, 18, 18)
        laranja = (226, 116, 15)
        amarelo = (237, 233, 4)
        roxo = (166, 0, 247)
        azul_ciano = (21, 204, 209)
        azul = (17, 65, 216)
    
        return [cinza_escuro, verde, vermelho, laranja, amarelo, roxo, azul_ciano, azul]

    def pintura(self, tela):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                valor_malha = self.grid[linha][coluna]
                malha_hit = pygame.Rect(coluna*self.cell_tamanho + 1, linha*self.cell_tamanho + 1, self.cell_tamanho - 1, self.cell_tamanho)
                pygame.draw.rect(tela, self.cores[valor_malha], malha_hit)