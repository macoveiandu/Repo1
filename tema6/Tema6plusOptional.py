# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
# metodele clasei.

# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


from Cerc import Cerc

cerc = Cerc(12,'albastru')

Cerc.descrie_cerc(cerc)
Cerc.aria(cerc)
Cerc.diametru(cerc)
Cerc.circumferinta(cerc)
cerc.culoare = 'Rosu'
Cerc.descrie_cerc(cerc)
print('-----------------------------------------------------------------------------')

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

from Dreptunghi import Dreptunghi

D = Dreptunghi(3,5,'rosie')
Dreptunghi.descrie(D)
D.aria()
D.perimetrul()
D.schimba_culoare('Portocalie')
Dreptunghi.descrie(D)
print('-----------------------------------------------------------------------------')

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
from angajat import Angajat

a = Angajat('Andrei','Macovei',1200)
Angajat.descrie(a)
Angajat.nume_complet(a)
Angajat.salariu_anual(a)
Angajat.marire_salariu(a,10)
Angajat.descrie(a)
print('-----------------------------------------------------------------------------')

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

from cont import Cont

t = Cont('RO123456','Macovei Andei',450)
Cont.afisare_sold(t)
Cont.debitare_cont(t,55)
Cont.creditare_cont(t,1000)
print('-----------------------------------------------------------------------------')

#___________________________________________________________________________________
''' Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.'''
#----------------------------------------------------------------------------------

# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

from factura import Factura

f = Factura(27,'Telefon',7,300)
Factura.genereaza_factura(f)
print('-----------------------------------------------------------------------------')

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

from masina import Masina
m = Masina('A1',200)
Masina.descrie(m)
print('--')
Masina.inmatriculare(m)
Masina.vopseste(m,'verde')
print('--')
Masina.descrie(m)
Masina.accelereaza(m,-2)
Masina.accelereaza(m,180)
Masina.accelereaza(m,200)
Masina.franeaza(m)
print('-----------------------------------------------------------------------------')
# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
#
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict

from todolist import ToDoList
k = ToDoList.todo
ToDoList.adauga_task(ToDoList,'spalat',True)
ToDoList.adauga_task(ToDoList,'calcat',False)
ToDoList.adauga_task(ToDoList,'alimentare',200)
ToDoList.adauga_task(ToDoList,'masina','vulcanizare')
print(k)
ToDoList.finalizeaza_task(ToDoList,'calcat')
print(k)
ToDoList.afiseaza_todo_list(ToDoList)
ToDoList.afiseaza_detalii_suplimentare(ToDoList,'condus')
print(k)
