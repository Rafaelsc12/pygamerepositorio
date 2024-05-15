class Cores:
    cinza_escuro = (26, 31, 40)
    verde = (47, 230, 23)
    vermelho = (232, 18, 18)
    laranja = (226, 116, 17)
    amarelo = (237, 234, 4)
    roxo = (166, 0, 247)
    ciano = (21, 204, 209)
    azul = (13, 64, 216)
    branco = (255, 255, 255)
    azul_escuro = (44, 44, 127)
    azul_claro = (59, 85, 162)

    @classmethod
    def obter_cores_celulas(cls):
        return [cls.cinza_escuro, cls.verde, cls.vermelho, cls.laranja, cls.amarelo, cls.roxo, cls.ciano, cls.azul]