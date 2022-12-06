'''
2. Noteaza in limbajul de programare Python, in cadrul unui comentariu,
ce este o variabila string – explica cu cuvintele tale.
'''

# boolean - este tipul de date in care se poate verifica daca este True sau False
# spre deosebire de Java in pyton trebuie ca prima litera sa se scrie cu majuscula

'''4. Declara si initializeaza in limbajul de programare python cate o
variabila din fiecare din urmatoarele tipuri: string, integer, float,
boolean. Alege valorile dupa preferinta ta.
'''
#string
nume = 'Macovei'
prenume = 'Andrei'
nickname = 'Andu'

# int
varsta = 30

#double/flaot  = zecimal
inaltime = 169.3

# boolean
job = True

print(f'Ma numesc {nume} {prenume}') #afiseaza Ma numesc Macovei Andrei
print(f'Dar prietenii imi spun {nickname}') #afiseaza Dar prietenii imi spun Andu
print(f'Am varsta de {varsta} ani si inaltimea de {inaltime} cm') #afiseaza Am varsta de 30 ani si inaltimea de 169.3 cm
print(f'Am un job momentan {job}') #afiseaa Am un job momentan  - afirmatia este adevarata

'''
Ce tipăreşte următorul segment de cod Java? Scrie segmentul de cod
in limbajul de progrmare java si afla raspunsul.
int i;
for (i=1; i<20; i = i+3)
System.out.println( i );
6. Scrie segmentul de cod de la exercitiul 5 in limbajul de programare
python.'''

for i in range (1, 20, 3):
    print(i)
# Afiseaza cifrele din 3 in 3, de la 1 pana la 20, adica - 1 4 7 10 13 16 19