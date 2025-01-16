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
