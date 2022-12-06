# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# Variabila = zona din memorie pentru valori de diferite tipuri

''' 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
'''
nume = 'Macovei'
prenume = 'Andrei Alexandru'
varsta = 30
inaltime = 1.76
casatorit = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(nume))
print('Variabila nume este de tip string?', isinstance(nume,str))
print(type(varsta))
print('Variabila varsta este de tip integer?', isinstance(varsta,int))
print(type(inaltime))
print('Variabila inaltime este de tip float?', isinstance(inaltime,float))
print(type(casatorit))
print('Variabila casatorit este de tip bool?', isinstance(casatorit,bool))

''' 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.'''

inaltime = round(inaltime)
print(type(inaltime))

'''5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.'''

print(f'Ma numesc {nume} {prenume}')
print(f'Am varsta de {varsta} ani')
print(f'Am inaltimea de aproximativ {inaltime} m')
print(f'Sunt casatorit: {casatorit}')

'''6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''

numele = input('Completati numele: ')
prenumele = input('Completati prenumele: ')
print(f'Numele complet are', len(numele)+len(prenumele), 'caractere.')

'''7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.'''

lungimea = int(input('Completati lungimea dreptunghiului: '))
latimea = int(input('Completati latimea dreptunghiului: '))
print(f'Aria dreptunghiului este',lungimea * latimea)

'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';'''

print('Coral is either the stupidest animal or the smartest rock'.count('the'))

'''9.
acelasi string
inlocuieste the cu THE peste tot
printeaza rezultatul'''

variabila_string = 'Coral is either the stupidest animal or the smartest rock'
print(variabila_string.replace('the','THE'))


'''10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.'''

assert isinstance(variabila_string,int)
