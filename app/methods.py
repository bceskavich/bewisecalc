def calculate(drinks, weight, period, gender):
    # Gender specific variables
    if gender == "male":
        r = .66      # Distribution ration
    else:
        r = .73

    # Loops thru drinks dictionary to get total drink oz.
    # Ex. dict format -- drinks = {"beer":1, "wine":2, "liqour":1}
    total = 0
    for drink in drinks.keys():
        if drink == "beer":
            total += 12 * .05 * drinks[drink]
            print "Beer:" + str(total)
        elif drink == "wine":
            total += 5 * .12 * drinks[drink]
            print "Wine:" + str(total)
        elif drink == "liqour":
            total += 1.25 * .4 * drinks[drink]
            print "Liqour:" + str(total)

    bac = ((total * 5.14) / (weight * r)) - .015 * period
    return bac
