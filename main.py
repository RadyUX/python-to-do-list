from tkinter import *
from tkinter import messagebox

class ToDOList:
    def __init__(self):
        """Initialise la liste des tâches."""
        self.do_list = []
    def ajouter_tache(self,tache):
      self.do_list.append({"tache":tache,"fait" :False})
      print(tache)
      print(self.do_list)
    #   enterTaskField=input("une tache ")
      if tache =="":
          messagebox.showerror("L'input ne peut pas être vide!")
      else:
          self.do_list.append({"tache": tache, "fait": False})
          print(f"Tâche ajoutée : {tache}")
    
    def afficher_tache(self,tache):
      self.tache=tache
      if not self.do_list:
       return "Aucune tâche enregistrée."
      else:
       
          return "\n".join([f"{i+1}. {task['tache']}" for i, task in enumerate(self.do_list)])


         


          
    
def submit_task(enterTaskField, todo):
    task=enterTaskField.get()
    todo.ajouter_tache(task)
    enterTaskField.delete(0, END)
def update_task_display():
    TextArea.delete(1.0,END)    
    TextArea.insert(1.0,todo.afficher_tache)

        
       
      
      
      
      
      






# Back end 

## gestion des erreurs

## supprimer taches specifique
def delete(): 
     pass


def exit():
     pass







# front end
task_list = []

counter = 1





    # definition des variables et de la fenetre tkinter
if __name__ == "__main__" :
     todo = ToDOList()
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

     TextArea = Text(gui, height = 5, width = 25, font = "lucida 13" ,wrap=WORD )

     Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = lambda: submit_task(enterTaskField, todo))
     
     delete.grid(row = 6, column = 2, pady = 5)

     TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
     enterTask.grid(row = 0, column = 2)

     enterTaskField.grid(row = 1, column = 2, ipadx = 50)
     
     taskNumber.grid(row = 4, column = 2, pady = 5)

     taskNumberField.grid(row = 5, column = 2)

     Submit.grid(row = 2, column = 2)
     Exit.grid(row = 5, column = 2)
         
     #demarrage
     
     gui.mainloop()
     
