#!/usr/bin/python3
import csv

def removeWord(zeile, question):
    if len(question) >= 26 and question[len(zeile)] is not ' ':
        del zeile[len(zeile)-1]
        removeWord(zeile, question)
        return zeile
    else:
        for i in range(0, len(zeile)):
            del question[0]
        

def divide(question):
    try:
        zeile = [question[x] for x in range(0, 25)]
    except IndexError:
        zeile = [x for x in question]
    x = removeWord(zeile, question)
    return "".join(zeile)
    
    

name = input('name of quizpool: ')

with open(name+".quiz", "w") as f:
    c = csv.writer(f, delimiter=";", quoting=csv.QUOTE_ALL)
    
    run = 1

    while run is 1:
        #Input
        frage = input('question (to exit, type "stop"): ')
        if frage != "stop":
            #In Array umwandeln
            frage_array = [x for x in frage]
            
            #Zählerwerte
            x, y, z = 0, 0, 0
            
            #Zeilen
            row1 = divide(frage_array)
            row2 = divide(frage_array)
            row3 = divide(frage_array)
            
            #Gesamt Tupel
            line = [row1, row2, row3]
            
            
            #Restliche Inputs
            line.append(input('answer A: '))
            line.append(input('answer B: '))
            line.append(input('answer C: '))
            line.append(input('answer D: '))
            line.append(int(input("correct answer (1-4): "))-1)
            
            c.writerow(line)
            print("That is your csv-line:", line)
        
        else:
            run = 0
    
    f.close()
