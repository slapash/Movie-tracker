import sqlite3

connect = sqlite3.connect('films.db')

curseur = connect.cursor()

def ajouterFilm(titreFilm):
    with connect:
        curseur.execute("INSERT INTO films VALUES (:titre)", {'titre': titreFilm})
    
    
def supprimerFilm(titreFilm):
    with connect:
        curseur.execute("DELETE from films WHERE titre = :titre", {'titre' : titreFilm})    

def modifFilm(ancien, nouveau):
    with connect:
        curseur.execute("UPDATE films Set titre = :nouveau WHERE titre = :ancien ", {'nouveau': nouveau, 'ancien': ancien})
        


curseur.execute("SELECT * FROM films;")
print(curseur.fetchall())
