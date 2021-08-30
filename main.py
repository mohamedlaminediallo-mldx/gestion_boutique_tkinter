from tkinter import *
import sqlite3
from vente import *
from totaux import *

def inserer():
    print('hello tout le monde')




def recupere():
    try:

        nom_cli=champ_nom.get()
        nom_produit = champ_nom2.get()
        prix=int(champ_nom3.get())

        #connexion a la base de donnée
        con=sqlite3.connect('donne.db')
        #liaison dun curseur
        cur =con.cursor()
                #excution des commande sql
        cur.execute(''' CREATE TABLE IF NOT EXISTS client(nomclient text,nomproduit text,prix real) ''')
        cur.execute(" INSERT INTO client VALUES(?,?,?)  ",(nom_cli,nom_produit,prix))

                #commiter la base de donne
        con.commit()

        for i in cur.execute('select * from client'):
            print(i)
        
        
    except:
        print('le prix nest pas correct ')


fen = Tk()
fen.title('GESTION DE BOUTIQUE')
fen.geometry("900x600")
fen.minsize(width=1000,height=700)
fen.maxsize(width=1000,height=600)



zonemenu=Frame(fen,borderwidth=3,bg='gray')
zonemenu.grid(column=0,row=0)

menuinser=Menubutton(zonemenu,text='Acceuil',width=30,borderwidth=1,bg='gray',activebackground='blue',relief=RAISED)
menuinser.grid(row=0,column=0)

menuvente=Button(zonemenu,text='Vente',width=30,borderwidth=1,bg='gray',activebackground='blue',relief=RAISED,command=ventes)
menuvente.grid(row=0,column=1)

menutotaux=Button(zonemenu,text='Totaux',width=30,borderwidth=1,bg='gray',activebackground='blue',relief=RAISED,command=totaux)
menutotaux.grid(row=0,column=2)

menuaide=Button(zonemenu,text='Quitter',width=30,borderwidth=1,bg='gray',activebackground='blue',relief=RAISED,command=quit)
menuaide.grid(row=0,column=3)


sous_menu=Menu(menuinser,tearoff = 0)
sous_menu.add_command(label='recherche',activebackground='blue',command=inserer )
sous_menu.add_command(label='suppression',command='achat_produit',activebackground='blue')
menuinser.configure(menu=sous_menu)

nom =Label(fen,text='nom client')
nom.grid(row=1,column=0)

champ_nom=Entry(fen,width=30)
champ_nom.grid(row=2,column=0)

nom_produit =Label(fen,text='nom du produit')
nom_produit.grid(row=3,column=0)

champ_nom2=Entry(fen,width=30)
champ_nom2.grid(row=4,column=0)

prix =Label(fen,text='le prix du produit')
prix.grid(row=6,column=0)

champ_nom3=Entry(fen,width=30)
champ_nom3.grid(row=7,column=0)

ajoute=Button(fen,text='ajouter',bg='orange',command=recupere)
ajoute.grid(row=8,column=0)

photo=PhotoImage(file='Logo.png',width=800,height=800)
label =Label(fen,image=photo)
label.grid()







fen.mainloop()
quit()