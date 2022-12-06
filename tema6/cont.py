# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self,a,b,c):
        self.iban = a
        self.titular_cont = b
        self.sold = c

    def afisare_sold(self):
        print(f'Buna ziua {self.titular_cont}')
        print(f'Soldul dumneavoastra din contul {self.iban} este {self.sold}')

    def debitare_cont(self,suma):
        self.sold = self.sold - suma
        print(f'Ai facut o plata in valoare de {suma}')
        print(f'in contul {self.iban} ti-a ramas {self.sold}')

    def creditare_cont(self,suma):
        self.sold = self.sold + suma
        print(f'Ai adugat suma de {suma}')
        print(f'In contul {self.iban} ai disponibil {self.sold}')
        

