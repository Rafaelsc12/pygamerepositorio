from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		self.id = id
		self.blocos = {}
		self.espacobloco = 30
		self.rotacao = 0
		self.colors = Colors.cor_das_malhas()

	def draw(self, screen):
		tiles = self.cells[self.rotacao]
		for tile in tiles:
			tile_rect = pygame.Rect(tile.coluna * self.espacobloco + 1, tile.linha * self.espacobloco, self.espacobloco -1, self.espacobloco -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)
