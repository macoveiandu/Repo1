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

class Masina:
    marca = 'Audi'
    model = ['A1','A2','A3']
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu','albastru','negru','galben','verde','portocaliu'}
    inmatriculata = False

    def __init__(self,mo,vm):
        self.model = mo
        self.viteza_maxima = vm

    def descrie(self):
        print(self.marca)
        print(self.model)
        print(self.viteza_maxima)
        print(self.culoare)
        print(self.inmatriculata)

    def inmatriculare(self):
        Masina.inmatriculata = True

    def vopseste(self,culoare):
        if culoare in self.culori_disponibile:
            Masina.culoare = culoare
        else:
            print('Nu exista in paleta de culori')

    def accelereaza(self,viteza):
        if viteza < 0:
            print('Viteza este negativa')
        elif viteza ==self.viteza_maxima:
            self.viteza_actuala=self.viteza_maxima
            print(f'Masina accelereaza la viteaza maxima {self.viteza_maxima}')
        else:
            self.viteza_actuala=viteza
            print(f'Masina accelereaza pana la viteza {viteza}')

    def franeaza(self):
        Masina.viteza_actuala = 0
        print('Masina s-a oprit!')

