import random
import os

os.system("cls")

print("Witaj w swiecie wisielca, podaj swoj nick: ")
pseudonim = input()


kat2=("Kot", "Pies", "Owca", "Krowa")
kat1=("Banan","Gruszka","Arbuz","Brzoskwinia")

print("")
print("* jesli bd chcial sie poddac wpisz \"end\"")
print("")  
print("* podawaj tylko małe cyfry")
print("")
    
print("wybierz kategorie")
print("1 - owoce")
print("2 - zwierzeta")
lista=int(input())
if(lista==2):
    lista=kat2
elif(lista==1):
    lista=kat1

haslo = str(lista[random.randint(0, len(lista) - 1)])
tablica = list(haslo)


for i in range(len(haslo)):
    tablica[i] = "_"




zycia = 7
ztab=0 
odp = []
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    | 
 |    |
 |   | |
 |   | |
 |  
----------
""")



while zycia > 0:
    os.system("cls")
    if(lista==kat2):
        print("kategoria zwierzeta")
    elif(lista==kat1):
        print("kategoria owoce")  
    print("")
    print(pseudonim, " pozostalo ci ", zycia, " zyc")
    print("")
    print(" ".join(tablica))
    print(" ")
    if(ztab>=1):
        print(HANGMAN[ztab])
    if(len(odp)>0):
        print("podane",odp)   
    print("Podaj swoja litere: ")
    litera = input()
    if(litera=="q"): 
        break
    if litera in odp:
        continue
    else:
        odp.append(litera)

    if litera.lower()  in haslo or litera.upper() in haslo:

        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera
            elif haslo[i] == litera.lower():
                tablica[i] = (litera.lower())
            elif haslo[i] == litera.upper():
                tablica[i] = (litera.upper())

        if litera == haslo or "".join(map(str, tablica)) == haslo:
            os.system("cls")
            print("")
            print("haslo to ", haslo)
            print(" ")
            print(pseudonim, " wygrales!")
            break
    
    else:
        zycia -= 1        
        ztab +=1

        print(HANGMAN[ztab])        
        if(zycia==0):
            os.system("cls")
            print("")
            print(pseudonim, " no niestety")
            print("")
            print("haslo to: ",haslo)
            break   