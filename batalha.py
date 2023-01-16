# Requisito 5 - Método de batalha
def batalhaPokemon(treinador1, treinador2):

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Forca = p1._ataque + p1._defesa + p1._hp
    p2Forca = p2._ataque + p2._defesa + p2._hp

# Vantagem de tipo em 50% em cima do dano básico da Força do Pokemon

    if (p1._tipo == "Fogo") and (p2._tipo == "Grama"):
        p1Forca*1.5
    elif (p1._tipo == "Aquatico") and (p2._tipo == "Fogo"):
        p1Forca*1.5
    elif (p1._tipo == "Grama") and (p2._tipo == "Aquatico"):
        p1Forca*1.5
    elif (p1._tipo == "Psiquico") and (p2._tipo == "Lutador"):
        p1Forca*1.5

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e forca {p2Forca}")

    if (p1Forca > p2Forca):
        print(
            f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(
            f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")
