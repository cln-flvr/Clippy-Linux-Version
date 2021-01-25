#Clippy-Mac
import PySimpleGUI as sg
import os.path
import pyperclip
import clipboard


# First the window layout in 2 columns
sg.theme('SystemDefault')
file_list_column = [
    [
        sg.Text("File:", key='-TEXT-'),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
file_viewer = [
    [sg.Text("Choose file:")],
    [sg.Text(size=(45, 40), key="-TOUT-")],
    [sg.Text(key="-FILE-")],
  
    
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(file_viewer),
    ]
]

window = sg.Window("Clipysh", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
       
        print("Hello: "+folder)
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
           
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".py", ".txt"))
        ]
        window["-FILE LIST-"].update(fnames)
        
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0])
            print("Hello Filename: "+filename)
            fileread = open(filename)
            filename = fileread.read()
            pyperclip.copy(filename)
            window["-TOUT-"].update(filename)
            window["-FILE-"].update(filename=filename)
            pyperclip.copy(filename)

        except:
            pass
            
fileread.close()
window.close()


