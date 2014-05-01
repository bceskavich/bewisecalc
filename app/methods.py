def calculate(drinks, weight, period, gender):
    # Gender distribution ration
    if gender == "male":
        r = .66
    else:
        r = .73

    # Loops thru drinks dictionary to get total drink oz.
    #   Proper Dict Format -- drinks = {"beer":1, "wine":2, "liqour":1}
    total = 0
    # Multiplies drink # by relative average ABV and ounce amount
    for drink in drinks.keys():
        if drink == "beer":
            total += 12 * .05 * drinks[drink]
        elif drink == "wine":
            total += 5 * .12 * drinks[drink]
        elif drink == "liqour":
            total += 1.25 * .4 * drinks[drink]

    # Runs calculation w/ total values, weight, gender constant (r) and other constants
    bac = ((total * 5.14) / (weight * r)) - .015 * period
    return bac
