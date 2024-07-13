import time
import math
import random


#VARIABLES

sPATTACK = 0        #Amount of sP applied in ATK
spDEFENCE = 0       #Amount of sP applied in DEF
sPSPEED = 0         #Amount of sP applied in SPD
sPINTELLIGENCE = 0  #Amount of sP applied in INT
sPHP = 0            #Amount of sP applied in HP
playMode = "x"

#FUNCTIONS

def sPASSIGNMENT():
    global sPATTACK
    global spDEFENCE
    global sPSPEED
    global sPINTELLIGENCE
    global sPHP
    SPUsage = input("You have levelled up! Would you like to use you sP now? (Y/N): ")
    if SPUsage == "Y":
        print("Which attribute would you like to add it to?")
        print("ATK: " + str(sPATTACK))
        print("DEF: " + str(spDEFENCE))
        print("SPD: " + str(sPSPEED))
        print("INT: " + str(sPINTELLIGENCE))
        print("HP: " + str(sPHP))
        spUSE = input("Type the attribute's name here: ")
        if spUSE == "ATK":
            sPATTACK += 1
        elif spUSE == "DEF":
            spDEFENCE += 1
        elif spUSE == "SPD":
            sPSPEED += 1
        elif spUSE == "INT":
            sPINTELLIGENCE += 1
        elif spUSE == "HP":
            sPHP += 1
        else:
            print("It will be cancelled. Try with the command.")
    else:
        print("It will be cancelled. Try with the command.")
    #return sPATTACK, spDEFENCE, sPSPEED, sPINTELLIGENCE, sPHP

def attributeOutPut():
    print("ATK: " + str(sPATTACK))
    print("DEF: " + str(spDEFENCE))
    print("SPD: " + str(sPSPEED))
    print("INT: " + str(sPINTELLIGENCE))
    print("HP: " + str(sPHP))

def userStatsOutPut():
    print("HP: " + str(sPATTACK))

def slowText(text):
    global sleepTime
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sleepTime)

#def singlePlayerSaveFile():
#    global savefileInput
#    savefileInput = input(print("Hello, user! Do you have a savefile you would like to load? (Y/N): "))
#    if savefileInput == "Y":
#        savefilePath = input(print("Type out the path in which you have your save-file: "))
#        savefile = open(savefilePath, "rt")
#        print(savefile)
#    elif savefileInput == "N":
#        savefileName = input(print("We will be creating one for you. Name your save: "))
#        savefile = open(savefileName, "x")
#        print(savefile)

def menu():
    global sleepTime
    global playMode
    global savefileInput
    global savefileName
    global savefile
    sleepTime = 0.05
    slowText("Hello user, to the game!\n")
    slowText("What mode would you like to play today?\n")
    playMode = input("Lonely... I'm so lonely... (singleplayer)         Friends! (multiplayer)\n")
    if playMode == "singleplayer":
        savefileInput = input("Great, loner! Do you have a savefile? (Y/N): ")
        if savefileInput == "Y":
            savefilePath = input("Type out the path in which you have your save-file: ")
            savefile = open(savefilePath, "rwt")
            print(savefile)
        else:
            savefileName = input("We will be creating one for you. Name your save: ")
            savefile = open(savefileName, "xrwt")
            print(savefile)
    elif playMode == "multiplayer":
        slowText("On BETA phase. Please try again after the next update. Thank you!")
        menu()
    else:
        slowText("Wrong input? We will take you to the menu. Please don't do it again.\n")
        menu()

#ARRAYS

ClassName = ["TEST","Warrior","Archer","Tank","Mage","Paladin","Arbalist","Mech","Pyromancer","Assasin","Sheriff","Air Bomber","Necromancer"]
ClassData = [
                 [0, 0, 100, 0, 0, 0, 10, 0, 0], #SELECTION CLASS
                #ORIGINALS
                 [3, 3, 97, 1, 15, 0, 10, 0, 0], #Warrior
                 [4, 2, 95, 1, 10, 0, 10, 0, 0], #Archer
                 [3, 4, 99, 1, 25, 0, 10, 0, 0], #Tank
                 [4, 2, 97, 2, 10, 0, 10, 0, 0], #Mage
                #VARIANTS S1
                 [6, 7, 94, 2, 30, 0, 10, 0, 0], #Paladin
                 [8, 4, 96, 2, 25, 0, 10, 0, 0], #Arbalist
                 [6, 5, 95, 2, 50, 0, 10, 0, 0], #Mech
                 [9, 5, 94, 4, 20, 0, 10, 0, 0], #Pyromancer
                #VARIANTS S2
                 [5, 4, 92, 2, 25, 0, 10, 0, 0], #Assasin
                 [7, 5, 94, 2, 25, 0, 10, 0, 0], #Sheriff
                [10, 3, 97, 2, 40, 0, 10, 0, 0], #Air bomber
                 [4, 3, 95, 4, 25, 0, 10, 0, 0]  #Necromancer
                #Attack, Defence, Speed, Intelligence, Health, XP obtained, XP required, Level, sP obtained
                ]

EnemyName = ["TEST", "Ant", "Skeleton Warrior", "Skeleton Archer", "Miltank", "Horness", "Kraken", "Siren"]
EnemyData = [
                [0, 0, 100, random(0, 0), 0], #TEST
                [1, 0, 99, 1, 3] #Ant
                #Birth Guardian
                [5, 6, 95, random(), 25], #Skeleton Warrior
                [7, 4, 94, random(), 20], #Skeleton Archer
                #Skeletor
                [6, 8, 97, random(), 30], #Miltank
                [9, 4, 94, random(), 20], #Horness
                #Minotaur
                [12, 10, 93, random(), 35], #Kraken
                [6, 9, 90, random(), 40] #Siren
                #Poseidon
                #Attack, Defence, Speed, XP Drop, Health
]

BossName = ["TEST", "Birth Guardian", "Skeletor", "Minotaur", "Poseidon"]
BossData = [
                [0, 0, 100, 0, 0], #TEST
                [3, 2, 98, 9, 0],  #Birth Guardian
                [],
                [],
                [],
                #Attack, Defence, Speed, XP Drop, Health
]
#TEST
#x = int(input("Input a value to add to the XP: "))
#ClassData[0][5] += x
#TESTEND
sleepTime = 0.1
slowText("Loading..............\n")
slowText("Patching up resources.......\n")
slowText("Booting v1.0.1...........\n")
menu()
#TEST
#i = 0
#for i in range(len(ClassData)):
#    if ClassData[i][5] >= ClassData[i][6]:
#        sPASSIGNMENT()
#        ClassData[i][5] -= ClassData[i][6]
#        ClassData[i][6] *= 1.2
#        ClassData[i][7] += 1
#        ClassData[i][8] += 1
#attributeOutPut()
#TESTEND