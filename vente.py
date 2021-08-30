from tkinter import *
import sqlite3
from totaux import totaux





def ventes():
    con=sqlite3.connect('donne.db')
    cur=con.cursor()
    stocke=[]

    
    cur.execute(''' CREATE TABLE IF NOT EXISTS client(nomclient text,nomproduit text,prix real) ''')
   
    Contenu=cur.execute("SELECT * FROM client")
    con.commit()
   

    for i in Contenu:
       
        stocke.append(i)
        
        

    
    
    
    
    

    fen_vent=Tk()
    fen_vent['bg']='Magenta'
    fen_vent.title('voici les produits vendus')
    label_client=Label(fen_vent,text='VOICI LES RESULTATS DE VOS VENTES',justify='center')
    label_client.grid(row=2,column=0)
    contenus =Text(fen_vent,width=100,height=90)
    contenus.insert(INSERT,stocke)
    contenus.grid()
    bouton_total=Button(fen_vent,text='total',command=totaux)
    bouton_total.grid(row=0,column=2,ipadx=100,sticky=S)
   
    fen_vent.mainloop()
    quit()
    





