''' Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.'''


# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
from calendar import monthrange
def nr_zile_pe_luni(an,luna):
    return monthrange(an,luna)[1]

# print(nr_zile_pe_luni(2022,11))
#------------------------------------------------------------------------------------

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(x, y):
    def adunare(x,y):
        return x+y
    def scadere(x,y):
        return x-y
    def inmultire(x,y):
        return x*y
    def impartire(x,y):
        return x/y
    return adunare(x, y),scadere(x, y),inmultire(x, y),impartire(x, y)
# print(calculator(10,2))

#------------------------------------------------------------------------------------
# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def dictionar(l1):
    l2 = []
    for x in range(len(l1)):
        for y in range(len(l1)):
            if l1[x] == l1[y]:
                l2.append(l2.count(l1[x]))
    return l2
ex = [1,3,1,5,9,7,7,5,5]
print(dictionar(ex))         #m-am pierdut aici . . .







#------------------------------------------------------------------------------------
# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def nr_max(a,c,z):
    b = [a,c,z]
    return max(b)

# print(nr_max(2,10,6))

#------------------------------------------------------------------------------------
# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def adunare_nr(n):
    return sum(range(0,n+1))

# print(adunare_nr(3))

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# Exerciții Opționale - Bonus
#------------------------------------------------------------------------------------
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
# Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
l3 = []
def nr_comune(l1,l2):
    for x in range(len(l1)):
        for y in range(len(l2)):
            if l1[x]==l2[y]:
                l3.append(l1[x])
    return l3
# print(set(nr_comune(list1,list2)))

#------------------------------------------------------------------------------------
# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

def reducere(a):
    x = int(input('introduceti reducerea (%): '))
    if x >= 100:
        print('Reducere invalida')
    else:
        b = a - (a*(x/100))
    return b
# print(reducere(int(input('introduceti pretul produsului: '))))


#------------------------------------------------------------------------------------
# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

def data_ora():
    from datetime import datetime
    return (datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# print(data_ora()) # ora din ro

def data_oraCH():
    from datetime import datetime
    import pytz
    return (datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime("%d-%m-%Y %H:%M:%S"))
# print(data_oraCH()) ora curenta din china


#------------------------------------------------------------------------------------
# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

from datetime import datetime
from datetime import date
import time

zi_curenta = date.today()

def timp_ramas(ziua_mea):
    zi_curenta == date.fromtimestamp(time.time())
    ziua_mea = date(zi_curenta.year, ziua_mea.month, ziua_mea.day)
    if ziua_mea < zi_curenta:
        ziua_mea = ziua_mea.replace(year=zi_curenta.year + 1)
        return ziua_mea
    else:
        return ziua_mea


zi_nastere = date(1992,7,25)
t = timp_ramas(zi_nastere)
zile_ramase = abs(t - zi_curenta)
zile = str(zile_ramase.days)
# print("Mai sunt " + zile + " zile pana la ziua mea")