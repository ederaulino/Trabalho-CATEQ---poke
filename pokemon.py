# Requisito 1 - Modelar classe pokemon com uma série de atributos

class Pokemon:
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        self._nome = nome
        self._especie = especie
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Movimento de ataque"

# Requisito 2 - Criar 3 subclasses de Pokemon com base em seu tipo


class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)

        self._tipo = "Aquatico"
        self._movimento = "Jato de água"


class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Fogo"
        self._movimento = "Lança chamas"


class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "Grama"
        self._movimento = "Chicote de cipó"


class Psiquico(Pokemon):
    def _init_(self, nome, tipo, hp, level):
        super()._init_(nome, tipo, hp, level)
        self._tipo = "Psiquico"
        self._movimento = "Controle da mente"


class Lutador(Pokemon):
    def _init_(self, nome, tipo, hp, level):
        super()._init_(nome, tipo, hp, level)
        self._tipo = "Lutador"
        self._movimento = "Chute duplo"


pokemonsDisponiveis = [
    Fogo("Charmander", "Charmander", "Fogo", 100, 50, 50),
    Grama("Bulbasauro", "Bulbasauro", "Grama", 200, 50, 50),
    Aquatico("Squirtle", "Squirtle", "Aquatico", 300, 50, 50),
    Fogo("Charmeleon", "Charmeleon", "Fogo", 200, 100, 100),
    Grama("Ivysauro", "Ivysauro", "Grama", 300, 50, 50),
    Aquatico("Wartortle", "Wartortle", "Aquatico", 300, 100, 50),
    Psiquico("Abra", "Abra", "Psiquico", 220, 150, 100),
    Lutador("Machop", "Machop", "Lutador", 150, 200, 80),
]
