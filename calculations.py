import math


def t_area(ar):
    tot_area = float(ar) * float(0.4047)
    return tot_area

def t1_area(ar,au):
    tot_area = float(ar) * float(0.4047)
    return tot_area


def planting_calculation(tot_area, espace):
    no_of_plants = math.ceil((tot_area * 10000) / espace ** 2)
    return no_of_plants

