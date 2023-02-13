import json
import random
import os

with open("words.json") as file:
    dat = json.load(file)
print(type(dat))
word_list=dat["data"]
print(type(word_list))
cant_num=len(word_list)

ran= random.randrange(0, cant_num)
word_select = word_list[ran].lower()

########################################################################
trys= 5

print(f"Para jugar este juego tienes que adivinar las letras o numeros y será revelada poco a poco,pero cuidado solo tienes {trys} intentos para ganar el juego. Iniciemos el juego :D")
input("Presione enter para iniciar")

hidden = '_'*len(word_select)
fail=0
count_try= trys
while hidden !=word_select and fail<trys:
    os.system("clear")
    print(f"Palabra escondida: {hidden}")
    digit_try = input("Intente adivinar una letra o numero: ")

    if digit_try in word_select:
        cant_reemp = word_select.count(digit_try)
        start = 0
        for i in range(cant_reemp):
            a = word_select.find(digit_try,start)
            hidden = hidden[:a] + digit_try + hidden[a+1:]
            start = a + 1
        print(f"La letra o numero {digit_try}  pertenece a la palabra escondida!")
    else:
        count_try -=1
        print(f"La letra o numero no pertenece a la palabra escondida, pierdes un intento. Te quedan {count_try} intentos")
        fail += 1 
    input("Presione enter para escribir la siguiente letra o numero")
    if hidden == word_select:
        print(f"Logró ganar el juego, la palabra es: {word_select}")
    else:
        print(f"Lo siento sus intentos se han acabado, la palabra es: {word_select}")
