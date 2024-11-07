import tkinter as tk
from tkinter import *


class Application(tk.Tk):
    def __init__(fenetre):
        tk.Tk.__init__(fenetre)

        fenetre.nombreElementParLigneMax = 5
        fenetre.nombreDeBouton = 7
        fenetre.nombreDePotentiometre = 2

        fenetre.configurer_la_fenetre()
        fenetre.creer_elements()

        fenetre.bind("<Configure>", fenetre.redimensionner_la_fenetre)

    def configurer_la_fenetre(fenetre):
        fenetre.configure(bg="#222222")
        fenetre.geometry("800x400")

    def creer_elements(fenetre):
        uniform_size = (800 - (fenetre.nombreElementParLigneMax + 1) * 5) // fenetre.nombreElementParLigneMax

        for i in range(fenetre.nombreDeBouton + fenetre.nombreDePotentiometre):
            ligne = i // fenetre.nombreElementParLigneMax
            colonne = i % fenetre.nombreElementParLigneMax

            cadre = tk.Frame(
                master=fenetre,
                # relief=tk.FLAT,
                # borderwidth=1,
                # bg="lightgray"
            )
            cadre.grid(row=ligne, column=colonne, padx=5, pady=5, sticky="nsew")

            if i < fenetre.nombreDeBouton:
                
                bouton = tk.Button(
                    master=cadre,
                    text=f"Bouton {i + 1}\nRelache",
                    font=("Inter", 12),  # Changer la police et la taille du texte
                    #anchor="n",  # Coller le texte en haut
                    relief=tk.FLAT,
                    width=uniform_size // 2,
                    bg="#2D2D2D", #Couleur du background
                    fg="#FFFFFF", #Couleur du texte
                    highlightthickness=0,  # Épaisseur de la bordure (Désactiver)
                )
                bouton.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)
            else:
                potentiometre = tk.Scale(
                    master=cadre,
                    from_=0, to=100,
                    orient=tk.HORIZONTAL,
                    label=f"Potentiomètre {i - fenetre.nombreDeBouton + 1}",
                    length=uniform_size,
                    bg="#2D2D2D", #Couleur du background
                    fg="#FFFFFF", #Couleur du texte
                    highlightthickness=0  # Épaisseur de la bordure (Désactiver)
                    #highlightbackground="#2D2D2D",  # Couleur de la bordure
                    #highlightcolor="#2D2D2D",  # Couleur de la bordure (peut être la même que highlightbackground)
                )
                potentiometre.pack(expand=True, fill=tk.BOTH, padx=0, pady=0)

            cadre.grid_propagate(False)
            cadre.update_idletasks()
            cadre.place(in_=fenetre, anchor="c", relx=(colonne + 0.5) / fenetre.nombreElementParLigneMax,
                        rely=(ligne + 0.5) / (fenetre.nombreDeBouton // fenetre.nombreElementParLigneMax + 1))

        for i in range(fenetre.nombreElementParLigneMax):
            fenetre.grid_columnconfigure(i, weight=1)

        for i in range(ligne + 1):
            fenetre.grid_rowconfigure(i, weight=1)

    def redimensionner_la_fenetre(fenetre, event):
        for widget in fenetre.winfo_children():
            widget.grid_configure(padx=5, pady=5)


# if __name__ == "__main__":
#     app = Application()
#     app.mainloop()
