import csv
import sys
def lire(search, culumn):
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        #print (ligne)
        prenom = ligne['prenom']
        nom = ligne['nom']
        carte = ligne['carte']
        achat = ligne['achat']
        date = ligne['date']
        mois = ligne['mois']
        if culumn == "1" :
            culumna = prenom
        else :
            if culumn == "2":
                culumna = nom
            else :
                if culumn == "3":
                    culumna = carte
                else :
                    if culumn == "4":
                        culumna = achat
                    else :
                        if culumn == "5":
                            culumna = date
                        else :
                            if culumn == "6":
                                culumna = mois
                            else :
                                main()
        #print ( prenom + " " + nom + " " + carte + " " + achat + " " + date)
        if  culumna == search :
            print( search + " TROUVE pour " + prenom + " " + nom + " " + carte + " " + achat + " " + date + " " + mois)
    print(" ")
def ecrire():
    with open('data1.csv', 'a', newline='') as fichier:
        fieldnames = ['prenom', 'nom', 'carte', 'achat', 'date', 'mois']
        fichier = csv.DictWriter(fichier, fieldnames=fieldnames, delimiter=';')
        print ("prenom?")
        prenomr = input()
        print ("nom?")
        nomr = input()
        print ("carte? forme xxxx-xxxx-xxxx-xxxx")
        case1r = input()
        print ("achat?")
        case2r = input()
        print ("date? forme xx-xx-xx ex 06-03-18")
        case3r = input()
        print ("mois? forme 00-xx-xx ex 00-03-18")
        case4r = input()
        fichier.writerow({'prenom': prenomr , 'nom' : nomr , 'carte' : case1r , 'achat' : case2r , 'date' : case3r, 'mois' : case4r })
    print(" ")
def erase():
    print("confirm y/n ?")
    confirm = 0
    confirm = input()
    if confirm == "y":
        with open('data1.csv', 'w', newline='') as fichier:
            fieldnames = ['prenom', 'nom', 'carte', 'achat', 'date', 'mois']
            fichier = csv.DictWriter(fichier, fieldnames=fieldnames, delimiter=';')
            fichier.writeheader()
            fichier.writerow({'prenom' :'', 'nom' :'' , 'carte' :'' , 'achat': '0' , 'date' :'0', 'mois' : '0' })
        print(" ")
    else :
        print(" ")
def status(prenomre, nomre):
    achatr = int(0)
    achatt = int(0)
    achatp = int(0)
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        #print (ligne)
        prenom = ligne['prenom']
        nom = ligne['nom']
        carte = ligne['carte']
        achat = ligne['achat']
        date = ligne['date']
        mois = ligne['mois']
        if  nom == nomre :
            if prenomre == prenom : 
                print( nomre + prenomre + " TROUVE pour " + prenom + " " + nom + " " + carte + " " + achat + " " + date + " " + mois)
                achatr = float(float(achat) + achatr)
        achatt = float(float(achat) + achatt)
    achatp = float(achatr/achatt)
    achatp = float(achatp * int(100))
    print( str(nomre) + " " + str(prenomre) + " represente " + str(round(achatp, 2)) + "% des achat total qui sont de " + str(round(achatt, 2)) + " euro")
    print( str(nomre) + " " + str(prenomre) + " = " + str(round(achatr, 2)) + " euro depenser par cette persone contre " + str(round(achatt, 2))+ " euro au total")
    print(" ")
def statusmois(moisre):
    achatr = int(0)
    achatt = int(0)
    achatp = int(0)
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        #print (ligne)
        prenom = ligne['prenom']
        nom = ligne['nom']
        carte = ligne['carte']
        achat = ligne['achat']
        date = ligne['date']
        mois = ligne['mois']
        if  moisre == mois :
            print( mois + " TROUVE pour " + prenom + " " + nom + " " + carte + " " + achat + " " + date + " " + mois)
            achatr = float(float(achat) + achatr)
        achatt = float(float(achat) + achatt)
    achatp = float(achatr/achatt)
    achatp = float(achatp * int(100))
    print( str(moisre)  + " represente " + str(round(achatp, 2)) + "% des achat total qui sont de " + str(round(achatt, 2)) + " euro")
    print( str(moisre)  + " = " + str(round(achatr, 2)) + " euro depenser ce mois contre " + str(round(achatt, 2)) + " euro au total")
    print(" ")
def statusauto():
    achatr = int(0)
    achatt = int(0)
    achatp = int(0)
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    with open('data2.csv', 'w', newline='') as fichier_name:
        fieldnames = ['prenom', 'nom']
        fichier_name = csv.DictWriter(fichier_name, fieldnames=fieldnames, delimiter=';')
        fichier_name.writeheader()
        fichier_name.writerow({'prenom' : "" , 'nom': ""    })
        for ligne in fichier:
            #print (ligne)
            prenom = ligne['prenom']
            nom = ligne['nom']
            carte = ligne['carte']
            achat = ligne['achat']
            date = ligne['date']
            mois = ligne['mois']
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        prenom = ligne['prenom']
        nom = ligne['nom']
        carte = ligne['carte']
        achat = ligne['achat']
        date = ligne['date']
        mois = ligne['mois']
        prenomr = prenom
        nomr = nom
        fichier_namer= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')
        stop = 0
        for ligner in fichier_namer:
            prenomop = ligner['prenom']
            nomop = ligner['nom']
            if (prenomop == prenomr) & (nomop == nomr):
                stop = 1
        if (stop == 0):
                with open('data2.csv', 'a', newline='') as fichier_name:
                    stop = 1
                    #print (ligne)
                    fieldnames = ['prenom', 'nom']
                    fichier_name = csv.DictWriter(fichier_name, fieldnames=fieldnames, delimiter=';')
                    fichier_name.writerow({'prenom': prenomr , 'nom' : nomr })
                    fichier_namer= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')               
    fichier_name= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')
    for ligne_name in fichier_name:
        achatt = 0
        achatr = 0
        achatp = 0
        prenomre = ligne_name['prenom']
        nomre = ligne_name['nom']
        f_achat= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
        for ligne in f_achat:
            #print (ligne)
            prenom = ligne['prenom']
            nom = ligne['nom']
            carte = ligne['carte']
            achat = ligne['achat']
            date = ligne['date']
            mois = ligne['mois']
            if  (nom == nomre) :
                if (prenomre == prenom) : 
                    achatr = float(float(achat) + achatr)
            achatt = float(float(achat) + achatt)
        # close file fichier
        # close(f_achat)
        achatp = float(achatr/achatt)
        achatp = float(achatp * int(100))
        print( str(nomre) + " " + str(prenomre) + " represente " + str(round(achatp, 2)) + "% des achat total qui sont de " + str(round(achatt, 2)) + " euro")
        print( str(nomre) + " " + str(prenomre) + " = " + str(round(achatr, 2)) + " euro depenser par cette persone contre " + str(round(achatt, 2)) + " euro au total")
        print(" ")
    
def statusmoisauto():
    achatr = int(0)
    achatt = int(0)
    achatp = int(0)
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    with open('data2.csv', 'w', newline='') as fichier_name:
        fieldnames = ['mois']
        fichier_name = csv.DictWriter(fichier_name, fieldnames=fieldnames, delimiter=';')
        fichier_name.writeheader()
        fichier_name.writerow({'mois' : "" })
        for ligne in fichier:
            #print (ligne)
            prenom = ligne['prenom']
            nom = ligne['nom']
            carte = ligne['carte']
            achat = ligne['achat']
            date = ligne['date']
            mois = ligne['mois']
    fichier= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
    for ligne in fichier:
        prenom = ligne['prenom']
        nom = ligne['nom']
        carte = ligne['carte']
        achat = ligne['achat']
        date = ligne['date']
        mois = ligne['mois']
        moisr = mois
        fichier_namer= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')
        stop = 0
        for ligner in fichier_namer:
            moisop = ligner['mois']
            if (moisop == moisr):
                stop = 1
        if (stop == 0):
                with open('data2.csv', 'a', newline='') as fichier_name:
                    stop = 1
                    #print (ligne)
                    fieldnames = ['mois']
                    fichier_name = csv.DictWriter(fichier_name, fieldnames=fieldnames, delimiter=';')
                    fichier_name.writerow({'mois': moisr })
                    fichier_namer= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')               
    fichier_name= csv.DictReader(open("data2.csv", "r", newline=''), delimiter=';')
    for ligne_name in fichier_name:
        achatt = 0
        achatr = 0
        achatp = 0
        moisre = ligne_name['mois']
        f_achat= csv.DictReader(open("data1.csv", "r", newline=''), delimiter=';')
        for ligne in f_achat:
            #print (ligne)
            prenom = ligne['prenom']
            nom = ligne['nom']
            carte = ligne['carte']
            achat = ligne['achat']
            date = ligne['date']
            mois = ligne['mois']
            if  (mois == moisre) :
                achatr = float(float(achat) + achatr)
            achatt = float(float(achat) + achatt)
        # close file fichier
        # close(f_achat)
        achatp = float(achatr/achatt)
        achatp = float(achatp * int(100))
        print( str(moisre)  + " represente " + str(round(achatp, 2)) + "% des achat total qui sont de " + str(round(achatt, 2)) + " euro")
        print( str(moisre)  + " = " + str(round(achatr, 2)) + " euro depenser ce mois contre " + str(round(achatt, 2)) + " euro au total")
        print(" ")
def main(stopp):
    sysvar = 0 
    if stopp == 0:
        try :
            sysvar = sys.argv[1]
            nb_line = 0
            sysvar = int(sysvar[0])
            stopp = 1
        except :
            print("no sysvar found!")
            sysvar = 0
            stopp = 1
    if sysvar != int(0) :
        if sysvar == 1 :
            print("quelle colone")
            print("1:prenom")
            print("2:nom")
            print("3:carte format : xxxx-xxxx-xxxx-xxxx")
            print("4:achat prix")
            print("5:date xx-xx-xx ex 06-03-18 ")
            print("6:mois format 00-xx-xx ex 00-10-18 ")
            culumn = str(input())        
            print("rechercher quoi?")
            search = str(input())
            lire(search, culumn)
            sysvar = 0
            main(stopp)
        else :
            if sysvar == 2 :
                ecrire()
                sysvar = 0
                main(stopp)
            else :
                if sysvar == 3 :
                    erase()
                    sysvar = 0
                    main(stopp)
                else :
                    if sysvar == 4:
                        print("prenom")
                        prenomre = str(input())
                        print("nom")
                        nomre = str(input())
                        status(prenomre, nomre)
                        sysvar = 0
                        main(stopp)
                    else :
                         if sysvar == 5:
                            print("mois format 00-xx-xx ex 00-10-18")
                            moisre = str(input())
                            statusmois(moisre)
                            sysvar = 0
                            main(stopp)
                         else :
                            if sysvar == 6:
                                statusauto()
                                sysvar = 0
                                main(stopp)
                            else :
                                if sysvar == 7:
                                    statusmoisauto()
                                    sysvar = 0
                                    main(stopp)
                                else :
                                    main(stopp)
    print("########################Program de traitement donné####################################")
    print("#                       Par PAUL MILLET                                               #")
    print("#                                                                                     #")
    print("#######################################################################################")
    print("lire = 1 ecrire = 2 erase = 3 status = 4  status/mois = 5 auto_status = 6 auto_status_mois = 7 ")
    choix = int(input())
    nb_line = 0
    if choix == 1 :
        print("quelle colone")
        print("1:prenom")
        print("2:nom")
        print("3:carte format : xxxx-xxxx-xxxx-xxxx")
        print("4:achat prix")
        print("5:date xx-xx-xx ex 06-03-18 ")
        print("6:mois format 00-xx-xx ex 00-10-18 ")
        culumn = str(input())        
        print("rechercher quoi?")
        search = str(input())
        lire(search, culumn)
        main(stopp)
    else :
        if choix == 2 :
            ecrire()
            sysvar = 0
            main(stopp)
        else :
            if choix == 3 :
                erase()
                sysvar = 0
                main(stopp)
            else :
                if choix == 4:
                    print("prenom")
                    prenomre = str(input())
                    print("nom")
                    nomre = str(input())
                    status(prenomre, nomre)
                    sysvar = 0
                    main(stopp)
                else :
                        if choix == 5:
                            print("mois format 00-xx-xx ex 00-10-18")
                            moisre = str(input())
                            statusmois(moisre)
                            sysvar = 0
                            main(stopp)
                        else :
                            if choix == 6:
                                statusauto()
                                sysvar = 0
                                main(stopp)
                            else :
                                if choix == 7:
                                    statusmoisauto()
                                    sysvar = 0
                                    main(stopp)
                                else :
                                    main(stopp)
stopp = 0
main(stopp)

