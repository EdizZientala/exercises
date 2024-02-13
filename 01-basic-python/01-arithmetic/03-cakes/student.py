def cakes(eggs, butter, flour):
    cake_amounts = set()
    cake_amounts.add(eggs//5)
    cake_amounts.add(butter//250)
    cake_amounts.add(flour//250)
    return min(cake_amounts)
