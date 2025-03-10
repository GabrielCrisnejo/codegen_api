import requests
import xml.etree.ElementTree as ET
import csv

# Define la URL y los parámetros
url = 'https://web-api.tp.entsoe.eu/api'
params = {
    'securityToken': 'c37e73a4-14d0-4ca1-b2ab-596591429743',  # Reemplaza con tu API Key
    'documentType': 'A44',
    'in_Domain': '10YAT-APG------L',
    'out_Domain': '10YAT-APG------L',
    'periodStart': '202407280000',
    'periodEnd': '202407282345',
}

# Realiza la solicitud GET
response = requests.get(url, params=params)

# Verifica si la respuesta es correcta
if response.status_code == 200:
    # Guarda el XML en un archivo
    with open('respuesta.xml', 'w', encoding='utf-8') as xml_file:
        xml_file.write(response.text)
    print("XML guardado en 'respuesta.xml'")

    # Analiza el XML
    root = ET.fromstring(response.text)

    # Extrae los precios
    namespaces = {'ns': 'urn:iec62325.351:tc57wg16:451-3:publicationdocument:7:3'}
    prices = []
    
    for point in root.findall(".//ns:Point", namespaces):
        position = point.find("ns:position", namespaces).text
        price = point.find("ns:price.amount", namespaces).text
        prices.append((int(position), float(price)))

    # Ordenamos por posición
    prices.sort()
    
    # Guardar en un archivo CSV
    with open('datos_filtrados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Posición", "Precio (EUR/MWh)", "País"])
        for pos, price in prices:
            writer.writerow([pos, price, "Austria"])  # '10YAT-APG------L' corresponde a Austria
    
    print("Datos guardados en 'datos_filtrados.csv'")
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
