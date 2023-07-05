import PySimpleGUI as Sg
import calculations

area_input = Sg.Input(key="Area")
hectare_button = Sg.Button("Hectare")
acre_button = Sg.Button("Acre")
esp_input = Sg.Input(key="Espacement")
esp_meter_button = Sg.Button("Meter")
esp_feet_button = Sg.Button("Feet")
calculate_button = Sg.Button("Calculate")
out_put = Sg.Text(size=(10, 1), key="-OUTPUT-")
exit_button = Sg.Button("Exit")
clear_button = Sg.Button("Clear")

layout = [
    [area_input, hectare_button, acre_button],
    [esp_input, esp_meter_button, esp_feet_button],
    [calculate_button, clear_button, out_put], [exit_button]]


window = Sg.Window("Plantation Calculator", layout)


while True:
    event, values = window.read()
    if event == "Exit":
        break
    if event == Sg.WINDOW_CLOSED:
        break

    try:
        raw_area = float(values["Area"])
        if event == "Hectare":
            total_area = raw_area
        elif event == "Acre":
            total_area = float(calculations.t_area(raw_area))
            print(total_area)

        raw_esp = float(values["Espacement"])
        if event == "Meter":
            esp = raw_esp
        elif event == "Feet":
            esp = raw_esp * 0.3048
            print(esp)

        if event == "Calculate":
            result = calculations.planting_calculation(total_area, esp)
            window["-OUTPUT-"].update(result, text_color="white")

        if event == "Clear":
            for key in values:
                window[key]('')

    except ValueError:
        window["-OUTPUT-"].update(value="Invalid input", text_color="red")

window.close()
