import csv
def lire():
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        print (ligne)
        prenom = ligne['prenom']
        nom = ligne['nom']
        case1 = ligne['case1']
        case2 = ligne['case2']
        case3 = ligne['case3']
        print ( prenom + " " + nom + " " + case1 + " " + case2 + " " + case3)
        if case3 == "pp" :
            print("PP TROUVE pour " + prenom + " " + nom)
    main()
def ecrire():
    with open('data1.csv', 'a', newline='') as fichier:
        fieldnames = ['prenom', 'nom', 'case1', 'case2', 'case3']
        fichier = csv.DictWriter(fichier, fieldnames=fieldnames, delimiter=';')
        print ("prenom?")
        prenomr = input()
        print ("nom?")
        nomr = input()
        print ("case1?")
        case1r = input()
        print ("case2?")
        case2r = input()
        print ("case3?")
        case3r = input()
        fichier.writerow({'prenom': prenomr , 'nom' : nomr , 'case1' : case1r , 'case2' : case2r , 'case3' : case3r})
    main()
def erase():
    with open('data1.csv', 'w', newline='') as fichier:
        fieldnames = ['prenom', 'nom', 'case1', 'case2', 'case3']
        fichier = csv.DictWriter(fichier, fieldnames=fieldnames, delimiter=';')
        fichier.writeheader()
        fichier.writerow({'prenom' :'', 'nom' :'' , 'case1' :'' , 'case2':'' , 'case3' :'' })
    main()
def main():
    print("lire = 1 ecrire = 2 erase = 3")
    choix = int(input())
    nb_line = 0
    if choix == 1 :
        lire()
    else :
        if choix == 2 :
            ecrire()
        else :
            if choix == 3 :
                erase()
            else :
                main()
main()
