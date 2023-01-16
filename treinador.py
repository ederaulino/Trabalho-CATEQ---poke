import random  # Biblioteca de funções de aleatoriedade

# Requisito 3 - Modelar classe Treinador


class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

# Requisito 4 - Modelar as subclasses Jogador e Inimigo


class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

# Esse método permite que o jogador escolha um Pokemon de sua lista para batalhar
    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else:
                print("Você escreveu um caractere inválido")

# Requisito 6  - Essa função captura o pokemon

    def capturarPokemon(self, pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")

# Requisito 7 - Essa função lista todos os pokemons
    def listarPokemons(self):
        for i in range(len(self._pokemons)):
            print(f"{i+1}. {self._pokemons[i]._nome}")


class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
