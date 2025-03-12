from tkinter import *

from tkinter import messagebox

class ToDOList:
    def __init__(self):
        self.do_list = []  # Initialisation 

    # Ajouter une tâche
    def ajouter_tache(self, tache):
        self.do_list.append({"tache": tache, "fait": False})
        print(f"Tâche '{tache}' ajoutée !")

    # Afficher toutes les tâches
    def afficher(self):
        if not self.do_list:
            print("Aucune tâche dans la liste.")
        else:
            print("Liste des tâches :")
            for i, tache in enumerate(self.do_list, 1):
                statut = "✔" if tache["fait"] else "❌"
                print(f"{i}. {tache['tache']} [{statut}]")


# Back end 

## gestion des erreurs

## supprimer taches specifique
def delete(): 
     pass


def exit():
     pass


def afficher_tache():
     pass






# front end
task_list = []

counter = 1





    # definition des variables et de la fenetre tkinter
if __name__ == "__main__" :
     # la fenetre
     gui = Tk()

     # le titre
     gui.title("To Do List")

     #resolution de la fenetre
     gui.geometry("250x300")


     gui.configure(background="light green")

     enterTaskField = Entry(gui)
     
     enterTask = Label(gui, text = "Enter Your Task", bg = "light green")
 

     delete = Button(gui, text="delete", fg = "black", bg = "red", command = delete)
     Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

     taskNumber = Label(gui, text = "delete task number", bg = "blue")

     taskNumberField = Text(gui, height= 1, width=2, font="lucida 13")

     TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

     Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = afficher_tache)
     
     delete.grid(row = 6, column = 2, pady = 5)

     TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
     enterTask.grid(row = 0, column = 2)

     enterTaskField.grid(row = 1, column = 2, ipadx = 50)
     
     taskNumber.grid(row = 4, column = 2, pady = 5)

     taskNumberField.grid(row = 5, column = 2)

     Submit.grid(row = 2, column = 2)
     Exit.grid(row = 7, column = 2)
         
     #demarrage
     gui.mainloop()
