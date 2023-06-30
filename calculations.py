def t_area(ar, ar_unit):
    tot_area = 0
    if ar_unit == "h":
        tot_area = ar
    elif ar_unit == "a":
        tot_area = ar * 0.4047
    return tot_area
