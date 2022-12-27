import os
import shutil
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# Créez la fenêtre principale
window = tk.Tk()
window.title("File Mover")
window.geometry("250x200")
window.resizable(False, False)


# Créez les champs d'entrée pour le répertoire source, de destination et l'extension de fichier
src_dir_label = tk.Label(text="Source directory:")
src_dir_entry = tk.Entry()
dest_dir_label = tk.Label(text="Destination directory:")
dest_dir_entry = tk.Entry()
file_ext_label = tk.Label(text="File extension:")
file_ext_entry = tk.Entry()

# Créez les boutons de commande "Déplacer" et "Copier"
move_button = tk.Button(text="Move", command=lambda: move_files(src_dir_entry.get(), dest_dir_entry.get(), file_ext_entry.get()))
copy_button = tk.Button(text="Copy", command=lambda: copy_files(src_dir_entry.get(), dest_dir_entry.get(), file_ext_entry.get()))

# Fonction pour déplacer les fichiers
def move_files(src_dir, dest_dir, file_ext):
  # Vérifiez si le répertoire de destination existe
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  
  # Parcourez les fichiers et les sous-dossiers du répertoire source
  for root, dirs, files in os.walk(src_dir):
    # Parcourez chaque fichier dans le répertoire actuel
    for file in files:
      # Si le fichier a l'extension souhaitée, déplacez-le dans le répertoire de destination
      if file.endswith(file_ext):
        shutil.move(os.path.join(root, file), dest_dir)
  # Affichez une fenêtre de message avec le texte "Déplacement terminé"
  messagebox.showinfo("Move completed", "The move of the files has been completed successfully.")

# Fonction pour copier les fichiers
def copy_files(src_dir, dest_dir, file_ext):
  # Vérifiez si le répertoire de destination existe
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  
  # Obtenez le nombre total de fichiers à copier
  total_files = len([file for file in os.listdir(src_dir) if file.endswith(file_ext)])
  copied_files = 0

  # Créez la barre de progression
  progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
  progress_bar.pack()

  # Parcourez les fichiers et les sous-dossiers du répertoire source
  for root, dirs, files in os.walk(src_dir):
    # Parcourez chaque fichier dans le répertoire actuel
    for file in files:
      # Si le fichier a l'extension souhaitée, copiez-le dans le répertoire de destination
      if file.endswith(file_ext):
        shutil.copy(os.path.join(root, file), dest_dir)
      
      # Mettez à jour la barre de progression
      copied_files += 1
      progress = copied_files / total_files
      progress_bar["value"] = progress * 100

      # Mettez à jour l'interface utilisateur
      window.update_idletasks()

  # Affichez une fenêtre de message avec le texte "Copy terminée"
  messagebox.showinfo("Copy completed", "The copy of the files has been completed successfully.")
  
  # Réinitialisez la barre de progression une fois que tous les fichiers ont été copiés
  progress_bar["value"] = 0
  progress_bar.destroy()

# Ajoutez tous les widgets à la fenêtre
src_dir_label.pack()
src_dir_entry.pack()
dest_dir_label.pack()
dest_dir_entry.pack()
file_ext_label.pack()
file_ext_entry.pack()
move_button.pack()
copy_button.pack()
window.mainloop()
