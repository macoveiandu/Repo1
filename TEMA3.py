
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

#x= int(input('Valoarea x este: '))

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do

note_muzicale = [ 'do', 're', 'mi', 'fa', 'so', 'la', 'si', 'do']

# ● Afișeaz-o
print(f'Lista de note muzicale cuprinde: {note_muzicale}')

# ● Inversează ordinea folosind slicing și suprascrie această listă.

note_muzicale = note_muzicale[::-1]

# ● Printează varianta actuală (inversată).
print(f'Noua lista inversata este: {note_muzicale}')

# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.

note_muzicale= note_muzicale[::-1]

# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
print(f'varianta actuala a listei: {note_muzicale}')

'''Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
 suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
 suprascrierea automat și permanentizează aceste modificări. Ambele variante
 își găsesc utilitatea în funcție de ce ne dorim în acel moment.'''

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista_completa = lista1 + lista2
lista1.extend(lista2)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.

print(f'Afiseaza lista completa: {lista_completa}')
# ● Sortează numărul 0 folosind o funcție.
print(f'am scos numarul {lista_completa.pop(2)}')
# ● Afișaza iar lista.
print(f'noua lista : {lista_completa}')

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

if len(lista_completa) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

lista_completa.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if len(lista_completa) != 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 8. Având dicționarul
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
print(dict1.keys())
# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1.update({'Dorel': 6})

print(f'Dupa contestatie Dorel aluat nota {dict1["Dorel"]}')

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Gigel')
print(dict1)
dict1['Ionica']=9
print(dict1)

# 12.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt.add('luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")
# 14. Afișează diferențele dintre aceste 2 seturi.
print(f'Diferentele sunt: {zile_sapt-weekend}')
# 15. Afișază intersecția elementelor din aceste 2 seturi.
print(f'Zilele comune sunt: {zile_sapt.intersection(weekend)}')