# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self,a,b,c):
        self.lungime = a
        self.latime = b
        self.culoare = c

    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}')
        print(f'Dreptunghiul are latimea {self.latime}')
        print(f'Dreptunghiul are culoarea {self.culoare}')

    def aria(self):
        a = self.latime * self.lungime
        print(f'Aria dreptunghiului este: {a}')

    def perimetrul(self):
        P = 2 * self.latime + 2 * self.lungime
        print(f'Perimetrul deptunghiului este: {P}')

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare



