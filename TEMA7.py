# 1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
# acum la ore.
# Curs git/github https://bit.ly/3yfFvqL
# VIDEOS 1, 2 si 3
#####################################################

                    #link github#
          #https://github.com/macoveiandu

#####################################################

# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import abstractmethod

class FormaGeometrica():

    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura = latura

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self,latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

    def aria(self):
        a = self.__latura * self.__latura
        print(f'Aria patratului este: {a}')

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din
# clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

class Cerc(FormaGeometrica):

    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self,raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None

    def aria(self):
        a =self.__raza * self.__raza * FormaGeometrica.pi
        print(f'Aria cercului este: {a}')

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

    def descrie(self):
        print('Eu nu am colturi')

# Creează un obiect de tip Patrat și joacă-te cu metodele lui

patrat = Patrat(4)
patrat.descrie()
patrat.aria()
patrat.latura = 8
patrat.latura
patrat.aria()
del patrat.latura
print('--------------------------')

# Creează un obiect de tip Cerc și joacă-te cu metodele lui

cerc = Cerc(5)
cerc.descrie()
cerc.aria()
cerc.raza = 4
cerc.raza
cerc.aria()
del cerc.raza


# 3. Actualizează proiectul pe github facand un push la noul cod
# În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public