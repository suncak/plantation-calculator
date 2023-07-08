import PySimpleGUI as Sg
from PySimpleGUI import Print

import calculations

area_input = Sg.Input(key='-Area-', size=(25, 15), enable_events=True)
hectare_button = Sg.Button("Hectare", size=(7, 1))
acre_button = Sg.Button("Acre", size=(7, 1))
esp_input = Sg.Input(key='-Espacement-', size=(25, 15))
esp_meter_button = Sg.Button("Meter", size=(7, 1))
esp_feet_button = Sg.Button("Feet", size=(7, 1))
calculate_button = Sg.Button("Calculate", size=(10, 1), button_color="dark green")
out_put = Sg.Text(size=(30, 1), key="-OUTPUT-")
exit_button = Sg.Button("Exit")
clear_button = Sg.Button("Clear", size=(9, 1))

layout = [
    [area_input, hectare_button, acre_button],
    [esp_input, esp_meter_button, esp_feet_button],
    [calculate_button, clear_button, out_put], [exit_button]]

window = Sg.Window("Plantation Calculator", layout, size=(425, 175))

while True:
    event, values = window.read()
    if event == "Exit":
        break
    if event == Sg.WINDOW_CLOSED:
        break
    if event == 'Acre':
        if values['-Area-'] == '':
            Sg.popup('Enter area')

    if event == 'Hectare':
        if values['-Area-'] == '':
            Sg.popup('Enter area')

    if event == "Meter":
        if values['-Espacement-'] == '':
            Sg.popup('Enter Espacement')

    if event == "Feet":
        if values['-Espacement-'] == '':
            Sg.popup('Enter Espacement')

    if event == "Calculate":
        if values['-Area-'] == '' or values['-Espacement-'] == '':
                    Sg.popup('Enter Area, Espacement first')
    try:
        raw_area = float(values['-Area-'])
        if event == "Hectare":
            total_area = raw_area

        if event == "Acre":
            total_area = float(calculations.t_area(raw_area))

        raw_esp = float(values['-Espacement-'])
        if event == "Meter":
            esp = raw_esp
        elif event == "Feet":
            esp = raw_esp * 0.3048

        try:
            if event == "Calculate":
                result = calculations.planting_calculation(total_area, esp)
                window["-OUTPUT-"].update(f"maximum seedlings: {result}", font=28, text_color="yellow")
        except NameError:
            Sg.popup("click area and espacement buttons")
            out_put.update('')
        if event == "Clear":
            # clearing field values after calculation
            area_input.update('')
            esp_input.update('')
            out_put.update('')
            Sg.popup('All cleared')
            # alternate way
            # for key in values:
            # window[key]('')
            # window["-OUTPUT-"](" ")

    except ValueError:
        # deceiving the value error
        window["-OUTPUT-"].update(value=" ", text_color="red")

    except ZeroDivisionError:
        window["-OUTPUT-"].update(value="Enter non-zero value", text_color="dark blue")
        Sg.popup("Enter non-zero values")
window.close()
