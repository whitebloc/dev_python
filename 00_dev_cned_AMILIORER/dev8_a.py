from random import *
from math import *
def main():
    lancer4piece()
def lancer4piece() :
    result = []
    posibilite = ["P", "F"]
    tirage1 = choice(posibilite)
    result.append(tirage1)
    tirage2 = choice(posibilite)
    result.append(tirage2)
    tirage3 = choice(posibilite)
    result.append(tirage3)
    tirage4 = choice(posibilite)
    result.append(tirage4)
    print(result)
    bien_repartie(result)
def bien_repartie(result):
    lengh = len(result)
    lengh_done = 0
    reading = 0
    P_count = 0
    F_count = 0
    while lengh > lengh_done :
        read = result[reading]
        if read == "P" :
            P_count = P_count + 1
        else :
            if read == "F":
                F_count = F_count + 1
        reading = reading + 1
        lengh_done = lengh_done + 1
    print ("  F = " + str(F_count) + "  P = " + str(P_count) )
    if P_count == F_count :
        print("bien repartie")
    else :
        print("mal repartie")
            
main()
