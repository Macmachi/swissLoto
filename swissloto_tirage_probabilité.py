#Dernières modifications : 06.10.2019

import random

listStat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

compteurTirage = 0

def statstirage():

    global compteurTirage

    while compteurTirage<10000000:

        compteurTirage +=1
        tirage = random.sample(range(1,43), 6)

        print(tirage)

        if 1 in tirage:
            listStat[1]+=1
        if 2 in tirage:
            listStat[2]+=1
        if 3 in tirage:
            listStat[3]+=1
        if 4 in tirage:
            listStat[4]+=1
        if 5 in tirage:
            listStat[5]+=1
        if 6 in tirage:
            listStat[6]+=1
        if 7 in tirage:
            listStat[7]+=1
        if 8 in tirage:
            listStat[8]+=1
        if 9 in tirage:
            listStat[9]+=1
        if 10 in tirage:
            listStat[10]+=1
        if 11 in tirage:
            listStat[11]+=1
        if 12 in tirage:
            listStat[12]+=1
        if 13 in tirage:
            listStat[13]+=1
        if 14 in tirage:
            listStat[14]+=1
        if 15 in tirage:
            listStat[15]+=1
        if 16 in tirage:
            listStat[16]+=1
        if 17 in tirage:
            listStat[17]+=1
        if 18 in tirage:
            listStat[18]+=1
        if 19 in tirage:
            listStat[19]+=1
        if 20 in tirage:
            listStat[20]+=1
        if 21 in tirage:
            listStat[21]+=1
        if 22 in tirage:
            listStat[22]+=1
        if 23 in tirage:
            listStat[23]+=1
        if 24 in tirage:
            listStat[24]+=1
        if 25 in tirage:
            listStat[25]+=1
        if 26 in tirage:
            listStat[26]+=1
        if 27 in tirage:
            listStat[27]+=1
        if 28 in tirage:
            listStat[28]+=1
        if 29 in tirage:
            listStat[29]+=1
        if 30 in tirage:
            listStat[30]+=1
        if 31 in tirage:
            listStat[31]+=1
        if 32 in tirage:
            listStat[32]+=1
        if 33 in tirage:
            listStat[33]+=1
        if 34 in tirage:
            listStat[34]+=1
        if 35 in tirage:
            listStat[35]+=1
        if 36 in tirage:
            listStat[36]+=1
        if 37 in tirage:
            listStat[37]+=1
        if 38 in tirage:
            listStat[38]+=1
        if 39 in tirage:
            listStat[39]+=1
        if 40 in tirage:
            listStat[40]+=1
        if 41 in tirage:
            listStat[41]+=1
        if 42 in tirage:
            listStat[42]+=1

    for i in range(1,43):
        print (i, listStat[i], round(listStat[i]/compteurTirage*100,2),"%")


statstirage()

