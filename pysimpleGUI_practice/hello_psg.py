import PySimpleGUI as sg

layout = [[sg.Txt('Hello from PySimpleGUI')], [sg.Button('OK')]]

#creats the window

window = sg.Window('Demo', layout=layout)

#create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or presses the OK button

    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()
