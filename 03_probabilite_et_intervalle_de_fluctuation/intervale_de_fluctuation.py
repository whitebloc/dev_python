from math import *
def main() :
    print("intervale de fluctuation de 95%")
    print("hypothese")
    print("1 = en pourcent decimal 2= en nombre relatif a l'effectif")
    choix_a = int(input())
    if choix_a == 1 :
        print("hypothese en pourcent deimal")
        hyp = float(input())
    else : 
        if choix_a == 2 :
            print("effectif de l'hypothese=")
            hyp = float(input())
            print("effectif de total l'hypothese=")
            nhyp = float(input())
            hyp = hyp/nhyp
        else :
            main()
    print("effectif total")
    n = int(input())
    print("probabilite")
    print("1 = en pourcent decimal 2= en nombre relatif a l'effectif")
    choix_b = int(input())
    if choix_b == 1 :
        print("p=")
        p = float(input())
    else : 
        if choix_b == 2 :
            print("p=")
            p = float(input())
            p = p/n
        else :
            main()
    calcule_intervale(p, n, hyp)
def calcule_intervale(p, n, hyp) :
    mini = p-(1/sqrt(n))
    maxi = p+(1/sqrt(n))
    print(str(mini) + " " + str(maxi))
    verification(hyp, maxi, mini)
def verification(hyp, maxi, mini) :
    if hyp >= mini :
        if hyp <= maxi :
            print ("hypothese verifier")
        else :
            print ("hypothese errone")
    else :
        print ("hypothese errone")
    main()
    print(" ")
main()

