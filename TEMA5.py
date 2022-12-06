'''Tema 5 - Funcții
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 5 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.

- OOP;

Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite
pentru a testa. Daca functia are return, printati raspunsul
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .'''

#------------------------------------------------------
#1.Funcție care să calculeze și să returneze suma a două numere

def suma(a,b):
    z = a+b
    return z
# print(suma(2,3))
#------------------------------------------------------

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def parImpar(a):
    if a % 2 == 0:
        return True
    else:
        return False

# print(parImpar(6))
#------------------------------------------------------

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def totalchar(nume,prenume,nume_mijlociu):
    total = len(nume)+len(prenume)+len(nume_mijlociu)
    return total
# print(totalchar('andu','macovei','alexandru'))

#------------------------------------------------------
# 4. Funcție care returnează aria dreptunghiului

def arieDreptunghi(L,l):
    z = L * l
    return z

# print(arieDreptunghi(2,3))

#------------------------------------------------------
# 5. Funcție care returnează aria cercului

def arieCerc(r):
    pi = 3.14
    a = pi * r * r
    return a
#print(arieCerc(4))

#------------------------------------------------------
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.
x = 'Macovei Andrei Alexandru'
def cautareChar(a):
    if x.find(a)>=0:
        return True
    else:
        return False

# print(cautareChar('z'))
# print(cautareChar('u'))

#------------------------------------------------------
# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def lowUpper(s):
    z = {'upper_case':0, 'lower_case':0}
    for x in s:
        if x.isupper():
            z['upper_case']+=1
        elif x.islower():
            z['lower_case']+=1
        else:
            pass
    print(f"Nr de caracter lower case este {z['lower_case']}")
    print(f"Nr de caracter upper case este {z['upper_case']}")
# print(lowUpper('AlexandRu'))

#------------------------------------------------------
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

def listaPozitiva(c):
    z = []
    for a in c:
        if a >=1:
            z.append(a)
        else:
            pass
    return z

# lista = [1,-2,-3,-4,6,10]
# print(listaPozitiva(lista))

#------------------------------------------------------
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def maremic(x,y):
    if x>y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif x<y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    elif x==y:
        print(f'Numerele sunt egale.')

print(maremic(3,4))
print(maremic(3,3))
#------------------------------------------------------
# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def addnr(a,x):
    if a in x:
        print(f'Nu am adaugat nr nou in set.Acesta exista deja')
        return False
    else:
        x.append(a)
        print(f'Am adaugat numarul nou in set')
        return True
print(addnr(1,[2,3,5,6]))
print(addnr(5,[2,3,5,6]))
