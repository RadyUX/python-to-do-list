from tkinter import *

from tkinter import messagebox

# Back end 
task_list = []

counter = 1



## gestion des erreurs

## supprimer taches specifique
def delete(): 
     pass


def exit():
     pass


def afficher_tache():
     pass






# front end





    # definition des variables et de la fenetre tkinter
if __name__ == "__main__" :
     # la fenetre
     gui = Tk()

     # le titre
     gui.title("To Do List")

     #resolution de la fenetre
     gui.geometry("250x300")

    # couleur de fond
     gui.configure(background="light green")

     # cree une boite de texte pour entré une nouvelle tache
     enterTaskField = Entry(gui)


     # cree un label entrez votre taches
     enterTask = Label(gui, text = "Enter Your Task", bg = "light green")
 
    # bouton pour supprimer la tache
     delete = Button(gui, text="delete", fg = "black", bg = "red", command = delete)
     # bouton pour quitter l'application
     Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
     #label qui dit de selectionner un chiffre
     taskNumber = Label(gui, text = "delete task number", bg = "blue")

     # champ pour entrer le chiffre
     taskNumberField = Text(gui, height= 1, width=2, font="lucida 13")
     # rentrer le contenu de la tache
     TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")


     # la tache est afficher dans la liste apres actionner ce bouton
     Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = afficher_tache)


     ## affiche les label et champ de text 
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
