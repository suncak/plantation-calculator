import math
import calculations


area = float(input("Enter land area: "))
areaUnit = input("Enter area unit 'a' for acre, 'h' for hectors:")
espacement = float(input("Enter espacement:"))
espacementUnit = input("Enter espacement unit- 'm' for meter, 'f' for feet: ")

total_area = calculations.t_area(area, areaUnit)

area_in_sqm = total_area * 10000
print("Area in sqm :", area_in_sqm)
row_length = math.sqrt(area_in_sqm)

esp_in_met = 0
if espacementUnit == "f":
    esp_in_met = espacement * 0.30481
elif espacementUnit == "m":
    esp_in_met = espacement


seedlings_in_row = row_length / esp_in_met
total_seedlings = seedlings_in_row ** 2
print(total_seedlings)
print("Aproximate no of seedlings :", math.floor(total_seedlings))
