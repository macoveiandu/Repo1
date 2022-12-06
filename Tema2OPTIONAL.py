'''1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''
x = input('Introdu X= ')


#2.Verifică dacă x are exact 6 cifre.

if len(x) == 6:
    print("Numarul x are 6 cifre")
else:
    print(f'Numarul x nu este format din 6 cifre, adica are {len(x)} cifre')


#3.Verifică dacă x este număr par sau impar (x e int).

if int(x) % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

#4. x, y, z (int)
#Afișează care este cel mai mare dintre ele?
x = int(x)
print(x)
y = int(input("Y ="))
z = int(input('z = '))
if x>y and x>z:
    print(f' x {x} este mai mare decat y {y} , z {z}')
elif y>x and y>z:
    print(f'y {y} este mai mare decat z {z} si x {x}')
else:
    print(f'z {z} este mai mare decat x {x} si y {y}')

# 5.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x = int(input('introdu x= '))
y = int(input('introdu y= '))
z = int(input('introdu z= '))
if x+y+z==180:      # suma unghiurilor trebuie sa fie egale cu 180 pentru ca triughiul sa fie valid
    print('Triunghiul este valid')
else:
    print("Triungiul nu este valid")

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
# ● Afișează stringul fără ultimele x caractere

propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu nr = '))
print(propozitie[0:len(propozitie)-x]) # merge pana la lungimea propozitiei minus valoare x pe care o dam de la tastatura

# '''7.Același string. Declară un string nou care să fie format din primele 5 caractere
# + ultimele 5
# print(propozitie[:5:]) =>afiseaza primele 5 caractere
# print(propozitie[-5::]) => afiseaza ultimele 5 caractere

print(propozitie[:5:]+propozitie[-5::])

# '''8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '

index = propozitie.index('rock')
print(f'Indexul de start este : {index}')
print(propozitie[0:index:])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

lista = input('Introdu un string: ')
assert lista[0:1].lower() == lista[-1::].lower()  #fortam primul si ultimul caracter in litere mici si facem verificarea


# '''10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)

t = '0123456789'
print(f'Numerele pare sunt: {t[::2]}')
print(f'Numerele impare sunt: {t[1::2]}')

# for nr in t:                             # am gandit-o prea deep :D apoi am vazut folosind sliceing
#     if int(nr) % 2 == 0:                 # m-am gadind sa verific caracterul din string
#         print(f'Numerele pare sunt: {nr}')
'''Exerciții Bonus (may need google) .
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y'''


import random
dice_roll = random.randint(1,6)
x = int(input('Alege un nr de zar: '))
if x<dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
elif x>dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
elif x==dice_roll:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
