from tkinter import *
import customtkinter as ctk
import tkinter as tk
root = ctk.CTk()
root.title("TO DO LIST")
root.geometry("900x400")
root.resizable(False, False)

ctk.CTkLabel(root, text="TO DO").grid(row=0, column=0)

ctk.set_appearance_mode("light")

limite = ctk.CTkLabel(root, text="você pode adicionar até 10 tarefas para realizar no seu dia, não se sobrecarregue :)")
limite.grid(row=1, column=0, padx=10)

frame_check = ctk.CTkFrame(root, fg_color=root.cget("bg"))

frame_check.grid(row= 4, column=0, sticky = "nsew")



check_buttons = []
delete_buttons = []
task_frames = []
labels = []

for i in range(10):
  tar = ctk.CTkLabel(root,text="", width=600, anchor=tk.W)
  labels.append(tar)

def add_tarefas_input():
   adicionar_t = input.get()
   print("Retrieved text:", adicionar_t)
   input.delete(0, END)
  
   if adicionar_t == "":
     return 
   
   for i in range(10):
     if labels[i].cget("text") == "" :
          labels[i].configure(text=adicionar_t)
          task_frame = ctk.CTkFrame(frame_check)
          task_frame.grid(row=(i + 5))
          task_frames.append(task_frame)
          labels[i].grid(in_=task_frame, row=(i + 6), column=0)
          check = ctk.CTkCheckBox(task_frame, text = "marcar concluído", onvalue=1, offvalue=0)
          check.grid(row=(i + 6), column=2, sticky="nsew")
          excluir = ctk.CTkButton(task_frame, text = "excluir tarefa", command=lambda tf=task_frame, idx=i: limpar_t(tf, idx))
          excluir.grid(row=(i + 6),sticky="nsew", column = 1)
          delete_buttons.append(excluir)
          break

def limpar_t(task_frame, idx):
   for widget in task_frame.winfo_children():
      widget.grid_forget()
   task_frame.grid_forget()
   labels[idx].configure(text="")

input = ctk.CTkEntry(root, width=400)
input.grid(row=2, column=0, padx=10)

adicionar_t = ctk.CTkButton(root, text="adicionar tarefa", command= add_tarefas_input, hover_color="lightblue")
adicionar_t.grid(row=3, column=0, padx=10)

root.grid_columnconfigure(0, weight=1)

root.bind('<Return>', lambda event:add_tarefas_input())

root.mainloop()
