def arbitrage_betting(odds, total_stake=None, fixed_index=None, fixed_stake=None):
    """
    identifies the possibilities of betting arbitrage, for many types of events

    args:
        odds (list): list of odds for the outcomes.
        total_stake (float, optional): total stake for all bets.
        fixed_index (int, optional): index of the fixed outcome (0-based).
        fixed_stake (float, optional): fixed stake for one specific outcome.


    return:
        dict: a dictionary with stakes for each outcome and additional info.
    """
    #on arbitrage possibilities
    inverse_sum = sum(1 / odd for odd in odds)

    if inverse_sum >= 1:
        print("the odds do not form an arbitrage opportunity.")

    stakes = [0] * len(odds)

    if total_stake is not None:
        #calculate stakes based on total stake
        for i, odd in enumerate(odds):
            stakes[i] = total_stake / (odd * inverse_sum)

    elif fixed_stake is not None and fixed_index is not None:
        #calculate stakes based on a fixed stake for one outcome (typically maximum for one option)
        fixed_odd = odds[fixed_index]
        for i, odd in enumerate(odds):
            if i == fixed_index:
                stakes[i] = fixed_stake
            else:
                stakes[i] = (fixed_stake * fixed_odd) / odd
        total_stake = sum(stakes)

    else:
        print("either a total stake or a fixed stake with an index must be provided")

    return {
        "stakes": stakes,
        "total stake": total_stake,
        "profit percentage": (1 - inverse_sum) * 100 if inverse_sum < 1 else 0
    }


def elokelly(e1, e2, o1, o2, m, b, j):
    """para dois jogadores, sem a possibilidade de empate
       e1 = elo do jogador 1
       e2 = elo do jogador 2
       o1 = odds para jogador 1
       o2 = odds para jogador 2
       m = multiplicador, a fração confortável de aposta. decimal
       b = banca
       j = jogador a avaliar"""

    if o1 < 1 or o2 < 1:
        raise ValueError("valores de odd devem ser superiores a 1")

    p1 = 1 - (1 / (1 + (10**((e1-e2) / 400))))
    p2 = 1 - (1 / (1 + (10**((e2-e1) / 400))))

    k1 = b*m*((p1)-((1-p1)/(o1-1)))
    k2 = b*m*((p2)-((1-p2)/(o2-1)))

    if j == 1:
        print(f"probabilidade de vitória do jogador: {p1}", end='\n')
        print(f"o quanto se deveria apostar: {k1}", end='\n')

        if k1 <= 0 or p1 < 0.5:
            print(f"a aposta não é aconselhada")

    elif j == 2:
        print(f"probabilidade de vitória do jogador: {p2}", end='\n')
        print(f"o quanto se deveria apostar: {k2}", end='\n')

        if k2 <= 0 or p2 < 0.5:
            print(f"a aposta não é aconselhada")

import math

def pontos(p, m, t1, t2=None):
    """calcula (como em um processo de Poisson) a probabilidade que se atinja, no mínimo, um
    determinado número de pontos para jogos de tempo finito.

    parâmetros:
    p = média de pontos (para apostas ao vivo, quantos já foram feitos)
    m = pontos a se atingir
    t1 = duração do jogo
    t2 = tempo corrido de jogo"""
