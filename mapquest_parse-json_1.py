import urllib.parse 
import requests
import time

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "3jRCqQMGQs5aOqetZQyS10oSqOZRlCVo"

while True:
    hora_actual = time.strftime("%H:%M:%S")
    print("Bienvenido! La hora actuales:", hora_actual)
    orig = input("Ubicación Inicial: ")
    if orig == "salida" or orig == "e":
        break
    dest = input("Destino: ")
    if dest == "salida" or dest == "e":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado del API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direccion Desde " + (orig) + " to " + (dest))
        print("Duracion del Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")