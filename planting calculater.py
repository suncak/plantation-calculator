import PySimpleGUI as Sg
import calculations

area_input = Sg.Input(size=(25,15), key="Area")
hectare_button = Sg.Button("Hectare", size=(7,1))
acre_button = Sg.Button("Acre", size=(7,1))
esp_input = Sg.Input(size=(25,15), key="Espacement")
esp_meter_button = Sg.Button("Meter", size=(7,1))
esp_feet_button = Sg.Button("Feet", size=(7,1))
calculate_button = Sg.Button("Calculate", size=(10,1))
out_put = Sg.Text(size=(30, 1), key="-OUTPUT-")
exit_button = Sg.Button("Exit")
clear_button = Sg.Button("Clear")

layout = [
    [area_input, hectare_button, acre_button],
    [esp_input, esp_meter_button, esp_feet_button],
    [calculate_button, clear_button, out_put], [exit_button]]


window = Sg.Window("Plantation Calculator", layout, size=(400,175))


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

        raw_esp = float(values["Espacement"])
        if event == "Meter":
            esp = raw_esp
        elif event == "Feet":
            esp = raw_esp * 0.3048

        if event == "Calculate":
            result = calculations.planting_calculation(total_area, esp)
            window["-OUTPUT-"].update(f"maximum seedlings: {result}", font=(16),text_color="yellow")

        if event == "Clear":
            for key in values:
                window[key]('')
                window["-OUTPUT-"](" ")

    except ValueError:
        # deceiting the value error
        window["-OUTPUT-"].update(value=" ", text_color="red")

    except ZeroDivisionError:
        window["-OUTPUT-"].update(value="Enter non-zero value", text_color="dark blue")

window.close()
