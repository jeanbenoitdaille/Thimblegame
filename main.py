from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox



def jouer_de():

    numero_sorti = 0
    image_choisie = random.choice(liste_images)
    image1 = ImageTk.PhotoImage(Image.open(image_choisie))
    label_image.configure(image=image1)
    label_image.image = image1


    if image_choisie == "images/de1.png":
        numero_sorti = 1
    elif image_choisie == "images/de2.png":
        numero_sorti = 2
    elif image_choisie == "images/de3.png":
        numero_sorti = 3
    elif image_choisie == "images/de4.png":
        numero_sorti = 4
    elif image_choisie == "images/de5.png":
        numero_sorti = 5
    else:
        numero_sorti = 6

    if numero_choisi.get() != "":

        if int(numero_choisi.get()) <1 or int(numero_choisi.get())>6:
            messagebox.showerror("Erreurs", "veuillez saisir un nombre entre 1 et 6 ")
        elif numero_sorti != int(numero_choisi.get()):
            label_result.config(text="Vous avez perdu")
        else:
            label_result.config(text="Vous avez gagné")
    else:
        messagebox.showerror("Erreurs", "veuillez saisir un nombre entre 1 et 6 ")






root = Tk()
root.geometry('320x500+500+100')
root.title("Jeu de simulation de dé")

label1 = Label(root, text="Choisr un numéro entre 1 et 6", pady=10, bg = "blue", fg="white", font=("Arial",14,"bold"))
label1.grid(row=1, column=1, columnspan=2)

numero_choisi = Entry(root)
numero_choisi.grid(row=2, column=1, columnspan=2, pady=15)

liste_images = ['images/de1.png', 'images/de2.png','images/de3.png','images/de4.png','images/de5.png','images/de6.png']

image_de = ImageTk.PhotoImage(Image.open(random.choice(liste_images)))

label_image = Label(root, image=image_de)
label_image.image = image_de
label_image.grid(row=3, column=1, columnspan = 2)


bouton_lancer = Button(root, text="Lancer dé", fg= "blue", font=("Arial",14,"bold"), width=15, height= 3, command= jouer_de, cursor="hand2")
bouton_lancer.grid(row=4, column=1, padx=20, pady=20)

bouton_quitter = Button(root, text="Quitter", fg= "red", font=("Arial",14,"bold"), width=15, height= 3, command= root.quit, cursor="hand2")
bouton_quitter.grid(row=4, column=2, padx=20, pady=20)


label_result = Label(root, text="", pady=20, fg="red",font=("Arial",14,"bold"))
label_result.grid(row=5, column=1, columnspan=2)










root.mainloop()
