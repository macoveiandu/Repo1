# #Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# '''Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.'''
#
x = int(input('Introdu X =  '))
#
# ''' 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
#  Functia if else evalueaza conditii'''
#
# # 2. Verifică și afișează dacă x este număr natural sau nu.
#
# if x >= 0: # verifica daca numarul introdus de la tastatura este mai mare sau egal cu 0
#     print('Numarul ales este natural')
# else: # altfel afiseaza mesajul de jos
#     print('Numarul NU este natural')
#
# # 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
#
# if x == 0: #verifica daca numarul introdus de la tastatura este egal cu 0
#     print('Numarul ales este neutru')
# elif x < 0: # verifica daca numarul introdus de la tastatura este mai mic decat 0
#     print('Numarul este negativ')
# elif x > 0: # verifica daca numarul introdus de la tastatura este mai mare decat 0
#     print('Numarul este pozitiv')
#
# # 4. Verifică și afișează dacă x este între -2 și 13.
#
# print(x >= -2 and x<=13) #verifica direct si afiseaza sau putem incerca cu funtia IF de la linia 31
#
# if x>= -2 and x<=13: #verifica daca este in acesa perioada si afiseaza mesajul de mai jos
#     print('Numarul se afla in aceasta perioada')
# else:  #altfel afiseaza mesajul de mai jos
#     print('Numarul este in afara acestei perioade')
#
# # 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
#
y=int(input('Introdu Y = ')) # introdu o cifra pentru Y
# if x-y <=4:
#     print('diferenta dintre x si y este mai mica')
# else:
#     print('Diferenta e mai mare')
#
# # 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
#
# if not x >= 5 and x <= 27: # verifica daca nu se afla intre 5 si 27
#     print("numarul nu este intre 5 si 27")
#
# # 7.
# # x și y (int)
# # Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# # mare.
#
# if x == y:
#     print('x si y sunt egale')
# elif x <= y:
#     print('Cifra Y este mai mare')
# elif x >= y:
#     print('Cifra X este mai mare')
#
# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
z = int(input('Introdu Z = '))
if (x == y == z): # verifica daca sunt toate egale
    print('Triunghiul este echilateral')
elif x == z or x==y: # verifica daca doua lature sunt egale
    print('Triunghiul este Isoscel')
elif y == z: # verifica daca doua lature sunt egale
    print('Triunghiul este Isoscel')
else: #altfel afiseaza msg de mai jos
    print('Este un triunghi oarecare')
#
# # 9. Citește o literă de la tastatură.
# # Verifică și afișează dacă este vocală sau nu
#
# litera = input("introdu litera: ")
# if litera == 'a':
#     print('Litera este Vocala')
# elif litera == 'e':
#     print('Litera este Vocala')
# elif litera == 'i':
#     print('Litera este Vocala')
# elif litera == 'o':
#     print('Litera este Vocala')
# elif litera == 'u':
#     print('Litera este Vocala')
# else:
#     print("Nu este Vocala")
# '''10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F'''
#
#
# nota = int(input('Introdu nota: ')) #introduce nota de la tastatura
# if nota >= 9: #daca nota este mai mare sau egal cu 9 afiseaza A
#     print('Ai luat calificativul A')
# elif nota >= 8:
#     print('Ai luat calificativul B')
# elif nota >= 7:
#     print('Ai luat calificativul C')
# elif nota >= 6:
#     print('Ai luat calificativul D')
# elif nota >= 4:
#     print('Ai luat calificativul E')
# else:
#     print('Ai luat calificativul F')
