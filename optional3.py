# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
#       3 Schimbări maxime admise:
#           ● Declară o Listă cu 5 jucători
#           ● Schimbari_efectuate = te joci tu cu valori diferite
#           ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
    # - Efectuează schimbarea
    # - Șterge jucătorul scos din listă
    # - Adaugă jucătorul intrat
    # - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
    # - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
    # teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori

echipa = ['Ion', 'Alex', 'Stefan', 'Cristi', 'Vasile']
schimbari_max = 3
schimbari_efectuate = int(input('Introdu nr de schimbari efectuate: '))
if schimbari_efectuate == schimbari_max:
    print(f'Nu mai poti efectua schimbari, s-au efectuat {schimbari_efectuate} schimbari in total')
else:
    jucator = input('introdu jucatorul: ')
    if  jucator in echipa and schimbari_efectuate < schimbari_max:
        echipa.pop(echipa.index(jucator))
        x = input('Introduceti numele jucatorului care intra in joc: ')
        schimbari_efectuate = schimbari_max - schimbari_efectuate
        echipa.append(x)
        print(f'A intrat jucatorul {x}, a iesit {jucator}, mai ai {schimbari_efectuate} schimbari')
        print(f'Noua echipa este formata din: {echipa}')
    else:
        print(f'Nu se poate efectua schimbarea deoarece {jucator} nu este in teren')
        schimbari_efectuate = schimbari_max - schimbari_efectuate
        print(f'Mai ai {schimbari_efectuate} schimbari')















