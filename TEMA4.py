# # 1.Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# # Folosește un for că să iterezi prin toată lista și să afișezi;
# # ● ‘Mașina mea preferată este x’.
# # ● Fă același lucru cu un for each.
# # ● Fă același lucru cu un while.
#
# for i in range(len(masini)): #for i merge de la valoare defaulth adica 0 pana la lungimea listei masini
#      print(f'Masina mea preferata este: {masini[i]}')
#      i += 1
#
# for masini in masini:  #for each isi schimba valoare de fiecare data
#     print(f'Masina mea preferata esteee {masini}')

x=0
while x<len(masini): #while cat timp x este mai mic decat lungimea listei afiseaza
    print(f'Masina mea preferata este {masini[x]}')
    x+=1

# # 2. Aceeași listă:
# # Folosește un for else
# # În for
# # - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# # exceptând primul și ultimul.
# # În else:
# # - Printează lista.
#
#
# for i in range(len(masini)):
#     masini[i] = masini[i].upper()
#     masini[0] = masini[0].lower()
#     masini[-1] = masini[-1].lower()
# else:
#     print(masini)
#
#
# # 3. Aceeași listă:
# # Vine un cumpărător care dorește să cumpere un Mercedes.
# # Itereaza prin ea prin modalitatea aleasă de tine.
# # Dacă mașina e mercedes:
# # Printează ‘am găsit mașina dorită de dvs’
# # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# # Altfel:
# # Printează ‘Am găsit mașina X. Mai căutam‘
#
# for cumparator in masini:
#     if cumparator == 'Mercedes':
#         print('Am gasit masina dorita de dvs ')
#         break
#     else:
#         print(f'Am gasit masina {cumparator}. Mai cautam...')
#
#
# # 4. Aceași listă;
# # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# # excepția Trabant și Lăstun.
# # - Dacă mașina e Trabant sau Lăstun:
# # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# # else).
# # - Printează S-ar putea să vă placă mașina x.
#
# for cumparator in masini:
#     if cumparator == 'Trabant' or cumparator == 'Lăstun':
#         continue
#     print(f'Sar putea sa va placa masina {cumparator}')
#
#
# # 5. Modernizează parcul de mașini:
# # ● Crează o listă goală, masini_vechi.
# # ● Itereaza prin mașini.
# # ● Când găsesti Lăstun sau Trabant:
# # - Salvează aceste mașini în masini_vechi.
# # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# # ● Printează Modele vechi: x.
# # ● Modele noi: x.
#
# masini_vechi = []
# for vehicul in masini:
#     if vehicul == 'Trabant' or vehicul == 'Lăstun':
#         masini_vechi.append(vehicul)
#         masini.remove(vehicul)
#         masini.append('Tesla')
# print(f'Modele vechi sunt: {masini_vechi}')
# print(f'Modelele noi sunt: {masini}')
#
#
# # 6. Având dict:
# pret_masini = {
#      'Dacia': 6800,
#      'Lăstun': 500,
#      'Opel': 1100,
#      'Audi': 19000,
#      'BMW': 23000
#  }
#
# # Vine un client cu un buget de 15000 euro.
#
# buget = 15000
# #brand = [k for k, pret in pret_masini.items() if pret <= buget ]
# #print(brand)
# # ● Prezintă doar mașinile care se încadrează în acest buget.
# for client in pret_masini:
#     if pret_masini[client] <= buget:
#         print(f'Masina ce se incadreaza in buget este: {client}')
# # ● Itereaza prin dict.items() și accesează mașina și prețul.
#
# print(pret_masini.items())
#
# # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină x Lastun
# # ● Iterează prin listă.
# for client in pret_masini:
#     if pret_masini[client] <= buget:
#         print(f'Pentru un buget de sub {buget} puteti alege masina {client}')
#
# # 7. Având lista:
# # numere =
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # ● Iterează prin ea.
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# y = 0
# for x in numere:
#     if x == 3:
#         y += 1
# print(f'Cifra 3 este afisate de {y} ori')
#
# # 8. Aceeași listă:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# y=0
# for x in range(len(numere)):
#     y+=numere[x]
# print(f'Suma numerelor din lista este: {y}')
#
#
# # 9. Aceeași listă:
# # ● Iterează prin ea.
# # ● Afișază cel mai mare număr (nu ai voie să folosești max).
# nr_mare=numere[0]
# for variabila in numere:
#     if variabila > nr_mare:
#         nr_mare= variabila
# print(f'Numarul ce mai mare este {nr_mare}')
# #
# # 10. Aceeași listă:
# # ● Iterează prin ea.
# # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # Ex: dacă e 3, să devină -3
# # ● Afișază noua listă.
# lista_noua = []
# for x in range(len(numere)):
#     if numere[x] > 0:
#         lista_noua=-numere[x]
#     elif numere[x] < 0:
#         lista_noua = numere[x]
#     elif numere[x] == 0:
#         lista_noua = numere[x]
#     print(lista_noua)
