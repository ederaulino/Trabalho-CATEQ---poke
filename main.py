from pokemon import pokemonsDisponiveis
from treinador import Jogador, Inimigo
from batalha import batalhaPokemon

# Requisito opcional: Criar um menu para o jogador
nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(3):
    print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

pokemonInicial = pokemonsDisponiveis[int(
    input("Digite o pokemon escolhido: "))-1]

print(f"O pokemon escolhido foi o {pokemonInicial._nome}")

jogador = Jogador(nomeJogador, [pokemonInicial])
inimigo = Inimigo("Bob", pokemonsDisponiveis)
print(jogador)
while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    0. Sair do jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu == "0":
        print("Você saiu do jogo.")
        break
    elif menu == "1":
        jogador.listarPokemons()
    elif menu == "2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

        capturado = pokemonsDisponiveis[int(
            input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu == "3":
        batalhaPokemon(jogador, inimigo)
    else:
        print("Você digitou algo inválido, tente novamente.")
