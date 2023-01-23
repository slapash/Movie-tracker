import sqlite3

connect = sqlite3.connect('films.db')

curseur = connect.cursor()

def ajouterFilm(titreFilm):
    with connect:
        curseur.execute("INSERT INTO films VALUES (:titre)", {'titre': titreFilm})
    
    



curseur.execute("SELECT * FROM films")
print(curseur.fetchall())
