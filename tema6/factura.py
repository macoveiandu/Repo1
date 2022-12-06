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

class Factura:
    seria = 'XV'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self,numar,nume_produs,cant,pretb):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cant
        self.pret_buc = pretb

    def schimba_cantitatea(self,cantitate):
        self.cantitate = cantitate
        print(f'Am schimbat canitatea in {cantitate}')

    def schimba_pret(self,pret):
        self.pret_buc = pret
        print(f'Am schimbat pretul {self.numar} {self.pret_buc}')

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume
        print(f'Am schimbat numele produsului in {self.nume_produs}')

    def total(self):
        total = self.cantitate * self.pret_buc
        return total

    def genereaza_factura(self):
        from datetime import date
        print(f'Factura cu seria {self.seria} numar {self.numar} ')
        print(f'Data {date.today()}')
        print("  Produs | Cantitate | pret/bucata | Total ")
        print(f" {self.nume_produs} |      {self.cantitate}    |     {self.pret_buc}     |  {self.total()} ")
