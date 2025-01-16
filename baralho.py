import random
import sys

def tarot(n):
    if n > 78:
        print(f'amostragem maior que o baralho')
        sys.exit()
    
    list1 = ["ouros", "copas", "espadas", "paus", "arcano maior"]
    arcanos = ["o louco", "o mago", "a sacerdotisa", "a imperatriz", "o imperador",
                          "o hierofante", "os amantes", "o carro", "a força", "o eremita",
                          "a roda da fortuna", "a justiça", "o enforcado", "a morte",
                          "a temperança", "o diabo", "a torre", "a estrela", "a lua", "o sol",
                          "o julgamento", "o mundo"]
    list2 = ["ás", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "valete", "cavaleiro", "rainha", "rei"]

    deck = set()

    while len(deck) < n:
        naipe = random.choice(list1)

        if naipe == "arcano maior":
            carta = random.choice(arcanos)
        else:
            carta = random.choice(list2)

        deck.add((carta, naipe))

    for carta, naipe in deck:
        print(f"carta: {carta} - naipe: {naipe}")
