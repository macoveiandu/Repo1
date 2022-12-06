# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    raza = None
    culoare = None

    def __init__(self,a,b): #constructor
        self.raza = a
        self.culoare = b

    def descrie_cerc(self):
        if self.culoare == None:
            print('Cercul nu are culoare')
        else:
            print(f'Culoarea cercului este {self.culoare}')
        print(f'Raza cercului este {self.raza}')

    def aria(self):
        import math
        a = math.pi * self.raza * self.raza
        return a

    def diametru(self):
        a = self.raza*2
        print(f'Diamentrul este {a}')

    def circumferinta(self):
        import math
        L = math.pi * 2 * self.raza
        print((f'Circumferinta este {L}'))


