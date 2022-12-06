# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
    # ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
    # ○ Dacă acesta răspunde nu - la revedere
    # ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class ToDoList:
    todo = {}

    def adauga_task(self,nume,descriere):
        self.todo.update({nume:descriere})

    def finalizeaza_task(self,nume):
        ToDoList.todo.pop(nume)

    def afiseaza_todo_list(self):
        for key in self.todo:
            print(key)

    def afiseaza_detalii_suplimentare(self,nume_task):
        if not nume_task in self.todo:
            print('Task ul nu este in todo list')
            raspuns = input('Vrei sa il adaugi?')
            if raspuns == 'nu':
                print('La revedere')
            else:
                detalii = input('Detalii task: ')
                self.todo.update({nume_task:detalii})








