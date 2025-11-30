import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from tkinter import messagebox
import random
import win32gui
import sys

#________________________________________________________________________________________________options_des_fenetres____________________________________________________________________________________________________
def bouton_quitter(fenetre,  couleur_texte = '#D4A59A', couleur_fond = '#5C2018' ):
    def quitter():
        sys.exit()
    bouton = Button(fenetre, text='quitter le jeu', command= quitter, bg = couleur_texte, fg = couleur_fond )
    bouton.pack(side='top', anchor='ne')

def premier_plan(fenetre):
    handle_fenetre = fenetre.winfo_id()
    win32gui.SetForegroundWindow(handle_fenetre)

def message_erreur(titre, texte):
    messagebox.showerror(titre, texte)

def fermer_fenetre(fenetre):
    fenetre.destroy()

def fermer_si_entrer(fenetre):
    fenetre.bind("<Return>", lambda event: fenetre.destroy())

def options_fenetre(fenetre):
    #logo
    fenetre.iconbitmap("logo.ico")
    #centrer
    hauteur_ecran = fenetre.winfo_screenwidth()
    largeur_ecran = fenetre.winfo_screenheight()
    fenetre.update_idletasks()
    x  = (hauteur_ecran - fenetre.winfo_width())//2
    y = (largeur_ecran - fenetre.winfo_height())//2
    fenetre.geometry(f"{fenetre.winfo_width()}x{fenetre.winfo_height()}+{x}+{y}")
    bouton_quitter(fenetre)

def fenetre_jauge(titre = "sans titre", texte = 'sans texte' ,valeur_max = 20, hauteur = 480, largeur = 840, couleur_texte = '#D4A59A', couleur_fond = '#5C2018' ):


    def mettre_a_jour_valeur(valeur):
        label_valeur.config(text=f"Valeur sélectionnée : {valeur}")

    def afficher_valeur():
        valeur_jauge = scale.get()
        print(str(texte), valeur_jauge)
        fenetre_jauge.valeur_selectionnee = valeur_jauge
        fenetre.destroy()
    fenetre = tk.Tk()
    fenetre.title(titre)
    fenetre.geometry(f"{largeur}x{hauteur}")
    fenetre.config(background=couleur_fond)
    options_fenetre(fenetre)
    frame = Frame(fenetre, bg= couleur_fond)
    scale = tk.Scale(frame, from_=1, to=valeur_max, orient=tk.HORIZONTAL, command=mettre_a_jour_valeur, font=("Helvetica", ) ,bg = couleur_fond, fg = couleur_texte)
    scale.pack()
    label_valeur = tk.Label(frame, text="Valeur sélectionnée : 0", bg = couleur_fond, fg = couleur_texte)
    label_valeur.pack()
    label_texte_supplementaire = tk.Label(frame, text=str(texte), font=("Helvetica", 20), bg = couleur_fond, fg = couleur_texte)
    label_texte_supplementaire.pack()
    bouton_valider = tk.Button(frame, text="Valider", command=afficher_valeur, font=("Helvetica", 20), bg = couleur_texte, fg = couleur_fond)
    bouton_valider.pack()
    frame.pack(expand = YES)
    fenetre_jauge.valeur_selectionnee = 0
    fenetre.mainloop()
    return fenetre_jauge.valeur_selectionnee

def fenetre_texte(titre = "sans titre", texte  = "pas de texte", texte_bouton = 'suivant', taille_texte = 20, hauteur =480, largeur=840, couleur_texte = '#D4A59A', couleur_fond = '#5C2018' ):
    global valeur
    valeur = 0
    def bouton_cliqué():
        valeur = 1
        fenetre.destroy()
    fenetre = tk.Tk()
    fenetre.title(str(titre))
    fenetre.config(background=couleur_fond)
    fenetre.geometry(f"{largeur}x{hauteur}")
    fermer_si_entrer(fenetre)
    options_fenetre(fenetre)
    frame = Frame(fenetre, bg = couleur_fond)
    texte = tk.Label(frame, text=texte,  font=("Helvetica", taille_texte), bg = couleur_fond, fg = couleur_texte, justify = "center", wraplength=800)
    bouton = Button(fenetre, text=texte_bouton, bg=couleur_fond, fg= couleur_texte, font=('Helvetica', 25), command= bouton_cliqué)
    texte.pack()
    frame.pack(expand = YES)
    bouton.pack(expand= YES)
    fenetre.mainloop()
    return valeur

def fenetre_question(titre = "sans titre", texte = 'sans texte', hauteur = 480, largeur = 840, couleur_texte = '#D4A59A', couleur_fond = '#5C2018'):


    def repondre():
        global nom_entre
        nom_entre = reponse.get()
        Fenetre.destroy()
        while nom_entre == "" : 
            message_erreur('erreur', "veuillez remplir ce champs")
            fenetre_question(titre, texte, hauteur, largeur, couleur_texte, couleur_fond)
            
        
    Fenetre = Tk()
    Fenetre.title(str(titre))
    Fenetre.config(background=couleur_fond)
    Fenetre.geometry(f"{largeur}x{hauteur}")
    premier_plan(Fenetre)
    options_fenetre(Fenetre)
    frame = Frame(Fenetre, background=couleur_fond, height=200, width=400)
    nom = Label(frame, text = str(texte), bg=couleur_fond, fg= couleur_texte, font=('Helvetica', 20))
    reponse = Entry(frame, bg=couleur_fond, fg= couleur_texte, width = 20, font=('Helvetica', 20 ), )
    bouton = Button(Fenetre, text='suivant', bg=couleur_fond, fg= couleur_texte, font=('Helvetica', 25), command= repondre)
    nom.pack()
    reponse.pack()
    frame.pack(expand=YES)
    bouton.pack(expand= YES)
    Fenetre.bind("<Return>", lambda event: [repondre(), Fenetre.destroy()])
    Fenetre.mainloop()
    return nom_entre

def fenetre_choix(titre = "sans titre", texte = "sans texte", premier_choix = "oui", Deuxieme_choix = "non", hauteur = 480, largeur = 840, couleur_texte = '#D4A59A', couleur_fond = '#5C2018'):
    global classes_info
    def recup():
        global choixxx
        choixxx = classes_info.get()
        fenetre_choix.destroy()
    fenetre_choix = tk.Tk()
    fenetre_choix.title(titre)
    fenetre_choix.geometry(f'{largeur}x{hauteur}')
    fenetre_choix.config(background=couleur_fond)
    frame = Frame(fenetre_choix, background= couleur_fond)
    classes_info = tk.IntVar()
    def changer_style():
        if classes_info.get() == 1:
            case_oui.config(bg = "#BC4639")
            case_non.config(bg = couleur_fond)
        else:
            case_non.config(bg = '#BC4639')
            case_oui.config(bg = couleur_fond)
    texte2 = Label(frame, text=texte, font=("Helvetica", 25), bg = couleur_fond, fg = couleur_texte)
    texte2.pack()
    case_oui = tk.Checkbutton(frame, text=premier_choix, variable=classes_info, onvalue=1, offvalue=0,font=("Helvetica", 20), bg = couleur_fond, fg = couleur_texte, command= changer_style)
    case_oui.pack()
    case_non = tk.Checkbutton(frame, text=Deuxieme_choix, variable=classes_info, onvalue=0, offvalue=1,font=("Helvetica", 20), bg = couleur_fond, fg = couleur_texte, command= changer_style)
    case_non.pack()
    bouton_afficher = tk.Button(frame, text='suivant', command=recup, font=("Helvetica", 25), bg = couleur_fond, fg = couleur_texte )
    bouton_afficher.pack()
    options_fenetre(fenetre_choix)
    frame.pack(expand= YES)
    fenetre_choix.mainloop()

def fenetre_selection(titre='sans titre', texte="sans texte", options=[], hauteur=480, largeur=840, couleur_texte='#D4A59A', couleur_fond='#5C2018'):
    choix = None

    def resultat():
        nonlocal choix
        choix = variable.get()
        if choix == str(len(options) + 1):
            message_erreur("Erreur", "Veuillez choisir une option")
        else:
            print(choix)
            fenetre.destroy()

    def changer_style():
        for i, option in enumerate(options):
            if option == variable.get():
                liste_boutons[i].config(bg=couleur_texte, fg=couleur_fond)
            else:
                liste_boutons[i].config(bg=couleur_fond, fg=couleur_texte)

    fenetre = tk.Tk()
    fenetre.title(titre)
    fenetre.geometry(f"{largeur}x{hauteur}")
    fenetre.config(background=couleur_fond)
    options_fenetre(fenetre)
    variable = tk.StringVar(value=str(len(options) + 1))
    cadre_options = tk.Frame(fenetre, bg=couleur_fond)
    cadre_options.pack(expand=YES)
    liste_boutons = []

    for i in range(len(options)):
        bouton = tk.Radiobutton(cadre_options, text=options[i], variable=variable, value=options[i], bg=couleur_fond,
                                fg=couleur_texte, font=("Helvetica", 20), command=changer_style)
        bouton.pack(anchor=tk.W, expand=YES)
        liste_boutons.append(bouton)

    bouton_afficher = tk.Button(fenetre, text="Valider", command=resultat, bg=couleur_texte, fg=couleur_fond,
                                height=2, width=20, font=("Helvetica", 20))
    bouton_afficher.pack(expand=YES)
    fenetre.mainloop()
    return str(choix)
    

    
    bouton_afficher = tk.Button(fenetre, text="Valider", command=resultat, bg = couleur_texte, fg = couleur_fond, height= 2, width=20, font = ("Helvetica", 20))
    bouton_afficher.pack(expand= YES)
    fenetre.mainloop()
    return str(choix) 

def tableau_combat(titre = "sans titre", texte = "sans texte", liste_personnages = None, hauteur = 480, largeur = 840, couleur_texte = '#D4A59A', couleur_fond = '#5C2018'):
    
    global fenetre_pricipale

    fenetre_principale = Tk()
    fenetre_principale.title(titre)
    fenetre_principale.geometry(f"{largeur}x{hauteur}")
    frame = Frame(fenetre_principale)
    tableau = ttk.Treeview(fenetre_principale)
    tableau["columns"] = ("Nom", "Classe", "Puissance", "Rapidité", "Résistance", "vie")
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("Nom", anchor=tk.CENTER, width=100)
    tableau.column("Classe", anchor=tk.CENTER, width=70)
    tableau.column("Puissance", anchor=tk.CENTER, width=100)
    tableau.column("Rapidité", anchor=tk.CENTER, width=100)
    tableau.column("Résistance", anchor=tk.CENTER, width=100)
    tableau.column("vie", anchor=tk.CENTER, width=100)


    tableau.heading("#0", text="", anchor="center")
    tableau.heading("Nom", text="Nom", anchor="center")
    tableau.heading("Classe", text="Classe", anchor="center")
    tableau.heading("Puissance", text="Puissance", anchor="center")
    tableau.heading("Rapidité", text="Rapidité", anchor="center")
    tableau.heading("Résistance", text="Résistance", anchor="center")
    tableau.heading("vie", text="vie", anchor="center")



    for index, personnage in enumerate(liste_personnages, start = 1):
        tableau.insert("", "end", text = str(index), values = (
                personnage.nom,
                personnage.classe,
                personnage.puissance,
                personnage.rapidité,
                personnage.résistance,
                personnage.vie
        ))

    tableau.pack(expand= YES)
    frame.pack()
    bouton_text = texte  
    bouton = tk.Button(fenetre_principale, text=bouton_text, command=fenetre_principale.destroy)
    bouton.pack() 
    fenetre_image_joueur(fenetre_principale, f"{joueur[0].classe}.png",f"fenetre de {joueur[0].nom}", joueur[0].nom, joueur[0].vie, 130, 280 )
    fenetre_image_joueur(fenetre_principale, f"{joueur[1].classe}.png",f"fenetre de {joueur[1].nom}", joueur[1].nom, joueur[1].vie, 1480,280 )
    options_fenetre(fenetre_principale)
    fenetre_principale.mainloop()

def fenetre_image_joueur(fenetre_principale, image, titre="sans titre", texte="sans texte", sous_texte = "sans sous texte", x = 0, y = 0, taille_texte=20, hauteur=250, largeur=500,  couleur_texte='#D4A59A', couleur_fond='#5C2018'):
    fenetre = Toplevel(fenetre_principale)
    fenetre.geometry(f"{hauteur}x{largeur}+{x}+{y}")
    fenetre.title(titre)
    fenetre.config(bg = couleur_fond)
    fenetre.overrideredirect(True)
    
    frame = Frame(fenetre)
    width = 236
    height = 430
    
    photo = PhotoImage(file=image).zoom(35).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg = couleur_fond, border= None)
    canvas.create_image(width / 2, height / 2, image=photo)
    canvas.pack(expand=YES)
    
    label_texte = Label(frame, text=texte, font=("Helvetica", taille_texte), fg=couleur_texte, bg = couleur_fond)
    label_texte.pack(expand=YES)
    sous_texte = Label(frame, text= sous_texte , fg = couleur_texte, bg = couleur_fond)
    sous_texte.pack()
    frame.config(bg= couleur_fond)
   
    fenetre.image_ref = photo

    frame.pack()

def fenetre_image(image, titre="sans titre", texte_titre = 'sans titre', texte="sans texte", sous_texte = "sans sous texte", taille_texte=20, hauteur=500, largeur=610,  couleur_texte='#D4A59A', couleur_fond='#5C2018'):
    fenetre = Tk()
    fenetre.geometry(f"{hauteur}x{largeur}")
    fenetre.title(titre)
    fenetre.config(bg = couleur_fond)
    options_fenetre(fenetre)
    
    frame = Frame(fenetre)
    width = 426
    height = 412
    
    photo = PhotoImage(file=image)
    canvas = Canvas(frame, width=width, height=height, bg = couleur_fond, border= None)
    canvas.create_image(width / 2, height / 2, image=photo)
    canvas.pack(expand=YES)
    
    texte_titree = Label(fenetre, text = texte_titre, font=("Helvetica", 40), fg=couleur_texte, bg = couleur_fond) 
    texte_titree.pack(expand= YES)
    label_texte = Label(frame, text=texte, font=("Helvetica", taille_texte), fg=couleur_texte, bg = couleur_fond)
    label_texte.pack(expand=YES)
    sous_texte = Button(frame, text= sous_texte , fg = couleur_texte, bg = couleur_fond, command= fenetre.destroy, font=("Helvetica", taille_texte))
    sous_texte.pack()
    frame.config(bg= couleur_fond)
   
    fenetre.image_ref = photo

    frame.pack()
    fenetre.mainloop()
#________________________________________________________________________________________________Classe_perso____________________________________________________________________________________________________


class Personnage:
    def __init__(self, nom, classe, puissance = 0, résistance=0, rapidité=0):
        self.nom = nom
        self.classe = classe
        self.puissance  = int(puissance)
        self.résistance = int(résistance)
        self.rapidité = int(rapidité)
        self.vie = 1000 +(self.résistance * 100)

    def afficher(self):
        print(f"Le personnage {str(self.nom)} a pour classe {str(self.classe)} : pour puissance {str(self.puissance)}: pour resistance {str(self.résistance)} : et pour rapidité : {str(self.rapidité)} ")


    def attaquer(self, cible):
        degats = self.puissance * random.randint(20,25)
        vitesse = cible.rapidité * random.randint(10,15)
        print(vitesse)
        hasard = random.randint(1,3)
        if vitesse > 30 and hasard == 1:
            fenetre_texte("combat", "il esquive")
            fenetre_texte("combat", f"Il reste {cible.vie} de vie à {cible.nom}")
        else : 
            cible.subir_degats(degats)





    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            fenetre_texte('combat', f"{self.nom} à été battu")
        else : 
            fenetre_texte('combat', f"{self.nom} à pris, degats, dégats, sa vie est maintenant à : {self.vie}")



#________________________________________________________________________________________________Explication_jeu____________________________________________________________________________________________________
            

def explication():
    fenetre_image("logo.png","Nom du jeu", "debut jeu", "Commencer le jeu", "Jouer")
    
    fenetre_texte('Règle du jeu', "Le jeu est un 1v1 entre 2 joueurs. Chaque joueur peut créer son personnage. Il doit choisir sa classe et peut attribuer 20 points de pouvoir   qui lui permettront d'améliorer la résistance, la puissance et la rapidité de leur personnage. Certaines classes sont plus vulnérables face à d'autres et inversement.",  "suivant", 20)
    fenetre_choix('infos classes', 'Afficher informations classes',"oui","non", 480, 840)
    if choixxx == 1 : 
        fenetre_texte("Informations classes", "Guerrier :  La classe guerrier est la classe la plus équilibrée,  il commence avec 2 points de pouvoirs supplémentaires pour chaque attribut.  Il craint particulièrement les Mages "
                            "  Mage :  Il possède une faible résistance mais est très puissant.  Il commence avec 6 points de puissance supplémentaires.  Il craint particulièrement les voleurs"
                            "  Voleur :  Très agile et furtif, il a plus de chance d'infliger des coups critiques.  Il commence avec 6 points de rapidité supplémentaires.  Il craint particulièrement les paladins " 
                            "  Paladin :  Très bon combattant, rapide et puissant.  Il commence avec 3 points de rapidité et 3 points de puissance supplémentaires.  Il craint particulièrement les guerriers"
                            "  Archer :  Fort dans les combats à distance, rapide et résistant.  Il commence avec 3 points de résistance et 3 points de puissance supplémentaires.  Il craint particulièrement les Berserkers"
                            "  Berserker :  Très puissant et résistant, il a de fortes chances d'infliger des dégâts critiques.  Il commence avec 4 points de puissance et 4 points de résistance supplémentaires  mais ses points de vitesse sont réduits de 2.  Il craint particulièrement les archers","suivant", 20, 650)

#________________________________________________________________________________________________création joueurs____________________________________________________________________________________________________


def création_joueurs():
    global joueur
    joueur = []
    for i in range(2):
            pts_restant  = 20
            nom =  fenetre_question("choix nom", f"Joueur numéro{i+1}, choisissez votre nom")
            classe  = str(fenetre_selection("choix classe", 'Quelle classe voulez vous choisir ?', ["guerrier", "mage", "voleur", "paladin", "archer", "berserker"]))
            pts_puissance = fenetre_jauge("points puissance", "puissance",pts_restant )
            pts_restant -= pts_puissance
            pts_resistance = fenetre_jauge("points resistance" , "resistance", pts_restant, )
            pts_restant -= pts_resistance
            pts_rapidité = fenetre_jauge("points rapidité", "rapidité", pts_restant )
            perso = Personnage(nom, classe, pts_puissance, pts_resistance, pts_rapidité)      
            if perso.classe == "guerrier":
                perso.puissance = perso.puissance + 2
                perso.rapidité = perso.rapidité + 2
                perso.résistance = perso.résistance + 2
            if perso.classe == "mage":
                perso.puissance = perso.puissance + 6
            if perso.classe == "voleur":
                perso.rapidité = perso.rapidité +  6
            if perso.classe == "paladin":
                perso.puissance = perso.puissance +3
                perso.rapidité =  perso.rapidité + 3
            if perso.classe == "archer":
                perso.puissance = perso.puissance + 3
                perso.résistance = perso.résistance + 2
            if perso.classe == "berserker":
                perso.puissance = perso.puissance + 4
                perso.rapidité =perso.rapidité - 2
                perso.résistance = perso.résistance + 2
            joueur.append(perso)

    print(joueur)
    tableau_combat("titre","Commencer le jeu", joueur) 
    return joueur
    


#___________________________________________________________________________________________Jeu____________________________________________________________________________________________________

def partie(joueur1, joueur2):
    while joueur1.vie > 0 or joueur2.vie > 0:

        action1 = fenetre_texte("jeu", f"{joueur1.nom}, que voulez vous faire : ", "attaquer")
        print(action1)
        joueur1.attaquer(joueur2)
        action2 = fenetre_texte("jeu", f"{joueur2.nom}, que voulez vous faire : ", "attaquer")
        print(action2)
        joueur2.attaquer(joueur1)
        















explication()
création_joueurs()
partie(joueur[0], joueur[1])
