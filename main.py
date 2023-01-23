from PySimpleGUI import PySimpleGUI as sg
from dbManagement import ajouterFilm
import sqlite3

connect = sqlite3.connect('films.db')
curseur = connect.cursor()

aRegarder = []
vus = []

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
        ajouterFilm(layout[0][0].get())
        
    if event == "-supprimer-":
        curseur.execute("SELECT * FROM films")
        vus = list(curseur.fetchall())
        window['-films_vus-'].update(vus)
        print(curseur.fetchall())

    

connect.commit()
connect.close()
window.close()