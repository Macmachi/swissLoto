#Dernières modifications : 06.10.2019

import random

def lotosimurandom():

        argentGagne = 0
        argentDepense = 0
        compteurSemaine = 0
        comparaisonTirage1 = 0
        comparaisonTirage2 = 0
        grillesjouees = 0

        while compteurSemaine<2600:

            comparaisonTirage1 = 0
            comparaisonTirage2 = 0

            tirage = random.sample(range(1,43), 6)
            numChancetirage =  random.sample(range(1,7), 1)
            grille1 = random.sample(range(1,43), 6)
            numChance1 =  random.sample(range(1,7), 1)
            grille2 = random.sample(range(1,43), 6)
            numChance2 =  random.sample(range(1,7), 1)
            compteurSemaine +=0.5
            argentDepense +=5
            grillesjouees +=2

            tirageNum1 = tirage[0]
            tirageNum2 = tirage[1]
            tirageNum3 = tirage[2]
            tirageNum4 = tirage[3]
            tirageNum5 = tirage[4]
            tirageNum6 = tirage[5]

            if tirageNum1 in grille1:
                comparaisonTirage1 +=1
            if tirageNum2 in grille1:
                comparaisonTirage1 +=1
            if tirageNum3 in grille1:
                comparaisonTirage1 +=1
            if tirageNum4 in grille1:
                comparaisonTirage1 +=1
            if tirageNum5 in grille1:
                comparaisonTirage1 +=1
            if tirageNum6 in grille1:
                comparaisonTirage1 +=1

            if comparaisonTirage1 == 3:
                argentGagne += 10
            if comparaisonTirage1 == 3 and numChancetirage==numChance1:
                argentGagne += 25
            if comparaisonTirage1 == 4:
                argentGagne += 75
            if comparaisonTirage1 == 4 and numChancetirage==numChance1:
                argentGagne += 150
            if comparaisonTirage1 == 5:
                argentGagne += 1000
            if comparaisonTirage1 == 5 and numChancetirage==numChance1:
                argentGagne += 10000
            if comparaisonTirage1 == 6:
                argentGagne += 1000000
            if comparaisonTirage1 == 6 and numChancetirage==numChance1:
                argentGagne += 2700000
                benefice = argentGagne - argentDepense
                print("Jackpot gagné après",round(compteurSemaine/52),"ans (en jouant 2 grilles par tirage (2 tirages semaine))")
                print("Bénéfice total :", benefice,"CHF")
                print("Total des lots (sans prix des grilles) :", argentGagne,"CHF")
                print("Nombre de grilles jouées :", grillesjouees, "(",grillesjouees*2.5,"CHF )")
                #break

            if tirageNum1 in grille2:
                comparaisonTirage2 +=1
            if tirageNum2 in grille2:
                comparaisonTirage2 +=1
            if tirageNum3 in grille2:
                comparaisonTirage2 +=1
            if tirageNum4 in grille2:
                comparaisonTirage2 +=1
            if tirageNum5 in grille2:
                comparaisonTirage2 +=1
            if tirageNum6 in grille2:
                comparaisonTirage2 +=1

            if comparaisonTirage2 == 3:
                argentGagne += 10
            if comparaisonTirage2 == 3 and numChancetirage==numChance2:
                argentGagne += 25
            if comparaisonTirage2 == 4:
                argentGagne += 75
            if comparaisonTirage2 == 4 and numChancetirage==numChance2:
                argentGagne += 150
            if comparaisonTirage2 == 5:
                argentGagne += 1000
            if comparaisonTirage2 == 5 and numChancetirage==numChance2:
                argentGagne += 10000
            if comparaisonTirage2 == 6:
                argentGagne += 1000000
            if comparaisonTirage2 == 6 and numChancetirage==numChance2:
                argentGagne += 2700000
                benefice = argentGagne - argentDepense
                print("Jackpot gagné après",round(compteurSemaine/52),"ans (en jouant 2 grilles par tirage (2 tirages semaine))")
                print("Bénéfice total :", benefice,"CHF")
                print("Total des lots (sans prix des grilles) :", argentGagne,"CHF")
                print("Nombre de grilles jouées :", grillesjouees, "(",grillesjouees*2.5,"CHF )")
                #break

            #benefice = argentGagne - argentDepense
            #print("Années :", round(compteurSemaine/52),"- Bénéfice total :", benefice,"CHF - Total des lots", argentGagne,"CHF")

        benefice = argentGagne - argentDepense
        print("Nombre d'années de jeu",round(compteurSemaine/52),"ans (2 tirages semaine avec 2 grilles à chaque fois)")
        print("Bénéfice total :", benefice,"CHF")
        print("Total des lots (sans prix des grilles) :", argentGagne,"CHF")
        print("Nombre de grilles jouées :", grillesjouees, "(",grillesjouees*2.5,"CHF )")

def lotosimustatic():

        argentGagne = 0
        argentDepense = 0
        compteurSemaine = 0
        comparaisonTirage1 = 0
        grillesjouees = 0

        while compteurSemaine<2600:

            comparaisonTirage1 = 0

            tirage = random.sample(range(1,43), 6)
            numChancetirage =  random.sample(range(1,7), 1)
            compteurSemaine +=0.5
            argentDepense +=2.5
            grillesjouees +=1

            #debug
            #print(tirage)
            #print(grilleinput)
            #print(numChancetirage)
            #print(numchanceinput)

            tirageNum1 = tirage[0]
            tirageNum2 = tirage[1]
            tirageNum3 = tirage[2]
            tirageNum4 = tirage[3]
            tirageNum5 = tirage[4]
            tirageNum6 = tirage[5]

            if tirageNum1 in grilleinput:
                comparaisonTirage1 +=1
            if tirageNum2 in grilleinput:
                comparaisonTirage1 +=1
            if tirageNum3 in grilleinput:
                comparaisonTirage1 +=1
            if tirageNum4 in grilleinput:
                comparaisonTirage1 +=1

            if tirageNum5 in grilleinput:
                comparaisonTirage1 +=1
            if tirageNum6 in grilleinput:
                comparaisonTirage1 +=1

            #debug
            #print(comparaisonTirage1)

            if comparaisonTirage1 == 3:
                argentGagne += 10
            if comparaisonTirage1 == 3 and numChancetirage==numchanceinput:
                argentGagne += 25
            if comparaisonTirage1 == 4:
                argentGagne += 75
            if comparaisonTirage1 == 4 and numChancetirage==numchanceinput:
                argentGagne += 150
            if comparaisonTirage1 == 5:
                argentGagne += 1000
            if comparaisonTirage1 == 5 and numChancetirage==numchanceinput:
                argentGagne += 10000
            if comparaisonTirage1 == 6:
                argentGagne += 1000000
            if comparaisonTirage1 == 6 and numChancetirage==numchanceinput:
                argentGagne += 2700000
                benefice = argentGagne - argentDepense
                print("Jackpot gagné après",round(compteurSemaine/52),"ans (en jouant 1 grille par tirage (2 tirages semaine))")
                print("Bénéfice total :", benefice,"CHF")
                print("Total des lots (sans prix des grilles) :", argentGagne,"CHF")
                print("Nombre de grilles jouées :", grillesjouees, "(",grillesjouees*2.5,"CHF )")
                #break

            #benefice = argentGagne - argentDepense
            #print("Années :", round(compteurSemaine/52),"- Bénéfice total :", benefice,"CHF - Total des lots", argentGagne,"CHF")

        benefice = argentGagne - argentDepense
        print("")
        print("Nombre d'années de jeu",round(compteurSemaine/52),"ans (2 tirages semaine avec 1 grille à chaque fois)")
        print("Bénéfice total :", benefice,"CHF")
        print("Total des lots (sans prix des grilles) :", argentGagne,"CHF")
        print("Nombre de grilles jouées :", grillesjouees, "(",grillesjouees*2.5,"CHF )")

while True:
    d1a = input ("Simulation 50 ans - A) Grilles aléatoires B) Grilles personnalisées. [A/B]? : ")
    # check if d1a is equal to one of the strings, specified in the list
    if d1a in ['A', 'B']:
        # if it was equal - break from the while loop
        break
# process the input
if d1a == "A":
    lotosimurandom()
elif d1a == "B":
    num1 = input('1/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num1) < 1 or int(num1) > 42:
        print("Entrée non valide dépassant l'intervalle demandé")
        num1 = input('1/6 Entrez 1 numéro unique entre 1 et 42 : ')
    num2 = input('2/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num2) < 1 or int(num2) > 42 or num2==num1:
        print("Entrée non valide dépassant l'intervalle demandé ou nombre déjà rentré")
        num2 = input('2/6 Entrez 1 numéro unique entre 1 et 42 : ')
    num3 = input('3/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num3) < 1 or int(num3) > 42 or num3==num1 or num3==num2:
        print("Entrée non valide dépassant l'intervalle demandé ou nombre déjà rentré")
        num3 = input('3/6 Entrez 1 numéro unique entre 1 et 42 : ')
    num4 = input('4/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num4) < 1 or int(num4) > 42 or num4==num1 or num4==num2 or num4==num3:
        print("Entrée non valide dépassant l'intervalle demandé ou nombre déjà rentré")
        num4 = input('4/6 Entrez 1 numéro unique entre 1 et 42 : ')
    num5 = input('5/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num5) < 1 or int(num5) > 42 or num5==num1 or num5==num2 or num5==num3 or num5==num4:
        print("Entrée non valide dépassant l'intervalle demandé ou nombre déjà rentré")
        num5 = input('5/6 Entrez 1 numéro unique entre 1 et 42 : ')
    num6 = input('6/6 Entrez 1 numéro unique entre 1 et 42 : ')
    if int(num6) < 1 or int(num6) > 42 or num6==num1 or num6==num2 or num6==num3 or num6==num4 or num6==num5:
        print("Entrée non valide dépassant l'intervalle demandé ou nombre déjà rentré")
        num6 = input('6/6 Entrez 1 numéro unique entre 1 et 42 : ')

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    num5 = int(num5)
    num6 = int(num6)

    grilleinput = [num1,num2,num3,num4,num5,num6]
    numchanceinput = input('Entrez le numéro chance entre 1 et 6 : ')
    if int(numchanceinput) < 1 or int(numchanceinput) > 42:
        print("Entrée non valide dépassant l'intervalle demandé")
        numchanceinput = input('Entrez le numéro chance entre 1 et 6 : ')
    numchanceinput = int(numchanceinput)
    lotosimustatic()