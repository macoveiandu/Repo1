'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1.
----
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for x in alte_numere:
    if x > 0:
        numere_pozitive.append(x)
    elif x < 0:
        numere_negative.append(x)
    if x % 2 == 0:
        numere_pare.append(x)
    elif x % 2 !=0:
        numere_impare.append(x)
print(f'Numerle pare sunt: {numere_pare}')
print(f'Numerle impare sunt: {numere_impare}')
print(f'Numerle negative sunt: {numere_negative}')
print(f'Numerle pozitive sunt: {numere_pozitive}')


'''2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4'''


def bubbleSort(alte_numere):
    n = len(alte_numere)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if alte_numere[j] > alte_numere[j + 1]:
                swapped = True
                alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
        if not swapped:
            return

bubbleSort(alte_numere)
print("Lista sortata crescator este: ")
print(alte_numere)


'''3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!'''

import random
nume_secret = random.randrange(1,30)
numar_ghicit = None
while numar_ghicit != nume_secret:
    numar_ghicit = input('Alege un numar intre 1 si 30: ')
    numar_ghicit = int(numar_ghicit)
    if numar_ghicit == nume_secret:
        print('Felicitari! Ai ghicit! ')
        break
    elif numar_ghicit < nume_secret:
        print('Nr secret e mai mare')
    elif numar_ghicit > nume_secret:
        print('Nr secret e mai mic')

'''4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333'''

x= int(input('Alege un nr '))
for i in range(x):
    x += 1
    for j in range(i+1):
        print(i+1,end="")
    print('')

'''5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

# print(tastatura_telefon)

for a in tastatura_telefon: # amgasit ceva pe internet dar nu cred ca printeaza ce trebuie :D
    for b in tastatura_telefon:
        print(f'cifra curenta este: {b}')
    print()

