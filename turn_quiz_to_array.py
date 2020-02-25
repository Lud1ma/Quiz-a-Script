import csv

def main(input):
    with open(input) as f:
        c = csv.reader(f, delimiter=";")
        i = 0
        print("var questions = [")
        for line in c:
            print(str(line)+",")
            i+=1
        print('];')

while True:
    main(input()+".quiz")
