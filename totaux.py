from tkinter import *
import sqlite3
from vente import *

def totaux():

    con=sqlite3.connect('donne.db')
    cur=con.cursor()
    total=0
    Contenu=cur.execute("SELECT prix FROM client")
    for i in Contenu:
      total=total+sum(i)
    
    
    
    
    print('vous aviez vendu',total,' FG')
    con.commit()

    fen_totaux=Tk()
    fen_totaux.title('total')
    fen_totaux.maxsize(width=390,height=290)
  
    cnv=Canvas(fen_totaux,bg='Indigo',)
    cnv.create_text(180,120,text="vous aviez vendu {} FG ".format(total))
    cnv.grid()


    


    fen_totaux.mainloop()
    quit()
