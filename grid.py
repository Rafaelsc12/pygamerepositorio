import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_linhas = 20
        self.num_colunas = 10
        self.cell_tamanho = 30 
        self.grid = [[0 for i in range(self.num_colunas)] for j in range(self.num_linhas)]
        self.cores = Colors.cor_das_malhas()

    def print_grid(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                print(self.grid[linha][coluna], end=" ") 
            print()
    def draw(self, screen):
        #Espaços do grid
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                valor_malha = self.grid[linha][coluna]
                malha_hit = pygame.Rect(coluna*self.cell_tamanho + 1, linha*self.cell_tamanho + 1, self.cell_tamanho - 1, self.cell_tamanho)
                pygame.draw.rect(screen, self.cores[valor_malha], malha_hit)
        
        # Linhas horizontais
        for linha in range(self.num_linhas + 1):
            pygame.draw.line(screen, (100, 0, 100), (0, linha*self.cell_tamanho), (self.num_colunas*self.cell_tamanho, linha*self.cell_tamanho), 1)
        
        # Linhas verticais
        for coluna in range(self.num_colunas + 1):
            pygame.draw.line(screen, (100, 0, 100), (coluna*self.cell_tamanho, 0), (coluna*self.cell_tamanho, self.num_linhas*self.cell_tamanho), 1)
