import sqlite3



nom_cli='diallo'
nom_produit='banane'
prix=256


        


 
  #connexion a la base de donnée
con=sqlite3.connect('base.db')
        #liaison dun curseur
cur =con.cursor()
                #excution des commande sql
cur.execute(''' CREATE TABLE IF NOT EXISTS client(nomclient text,nomproduit text,prix real) ''')
cur.execute(" INSERT INTO client VALUES(?,?,?)  ",(nom_cli,nom_produit,prix))

                #commiter la base de donne
con.commit()

for i in cur.execute('select * from client'):
    print(i)