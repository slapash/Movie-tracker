from PySimpleGUI import PySimpleGUI as sg
from dbManagement import ajouterFilm
import sqlite3

def rafraichir():
    curseur.execute("SELECT * FROM films")
    vus = list(curseur.fetchall())
    window['-films_vus-'].update(values = vus)


connect = sqlite3.connect('films.db')
curseur = connect.cursor()
#affiche la liste de la bdd
curseur.execute("SELECT * FROM films")
vus = list(curseur.fetchall())
#ferme le curseur pour ne pas poser de probleme pendant le programme
curseur.close()
############################
curseur = connect.cursor()



layout = [[sg.Input(default_text="Pulp Fiction", border_width= None, enable_events= True, key="-titre-")],
             [sg.Listbox(values = vus, enable_events= True, size=(40, 10), key="-films_vus-")],
             [sg.Button(button_text= "ajouter", enable_events= True, key ='-ajouter-'),
             sg.Button(button_text= "modifier", enable_events= True, key = '-modifier-'),
             sg.Button(button_text= "supprimer", enable_events= True, key = '-supprimer-')]]





window = sg.Window(title="Movie Tracker", layout= layout, icon = 'something.ico', resizable= True)



while True:
    
    event, values = window.read()
    
   

    if event == sg.WIN_CLOSED:
        break
    if event == "-ajouter-":
        nouveauTitre = layout[0][0].get()
        ajouterFilm(nouveauTitre)
        rafraichir()

        
    if event == "-supprimer-":
        
        print(curseur.fetchall())

    

connect.commit()
connect.close()
window.close()