class Posicao:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def mover(self, delta_linha, delta_coluna):
        self.linha += delta_linha
        self.coluna += delta_coluna

    def copiar(self):
        return Posicao(self.linha, self.coluna)

    def _eq_(self, other):
        if isinstance(other, Posicao):
            return self.linha == other.linha and self.coluna == other.coluna
        return False

    def _repr_(self):
        return f"Posicao(linha={self.linha}, coluna={self.coluna})"

    def _hash_(self):
        return hash((self.linha, self.coluna))