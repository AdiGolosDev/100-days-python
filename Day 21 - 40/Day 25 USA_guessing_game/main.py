import csv
import pandas
import os

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data)) # DataFrame
# print(type(data["temp"])) # Series

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].median())

# print(data.condition)

print(data[data.temp == 14]) # prints row where temp was highest

monday = data[data.day == "Monday"]
print((monday.temp * 1.8) + 32) # monday's temp in fahrenheit

data_dict = {
    "students": ["Klok", "Klokan", "Klokologan"],
    "scores": [80, 60, 20]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

if not os.path.exists("./new_data.csv"):
    new_data.to_csv("new_data.csv")

