# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self,a,b,c):
        self.nume = a
        self.prenume = b
        self.salariu = c

    def descrie(self):
        print(f'Numele angajatului este: {self.nume} ')
        print(f'Prenumele angajatului este: {self.prenume}')
        print(f'Are salariul {self.salariu}')

    def nume_complet(self):
        print(self.nume +' ' + self.prenume)

    def salariu_lunar(self):
        print(f'salariul lunar este de {self.salariu}')

    def salariu_anual(self):
        salriu_anual = self.salariu * 12
        print(f'salariul anual este {salriu_anual}')

    def marire_salariu(self,procent):
        self.salariu = self.salariu + self.salariu/100*procent
