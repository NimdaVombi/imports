import os
from setup import *
import PySimpleGUI as sg
class gui:
	layout = [
    [sg.Text("Select an option:")],
    [sg.Button("Option 1"), sg.Button("Option 2")],
    [sg.Button("Option 3"), sg.Button("Option 4")],
    [sg.Button("Quit")]
	]

	window = sg.Window("imports", layout)

	while True:
		event, values = window.read()
		if event == "Option 1":
			print('hiiiii')
		if event in (sg.WIN_CLOSED, "Quit"):
			break


	window.close()
