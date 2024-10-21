import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.sunat.gob.pe/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Parsear el HTML
soup = BeautifulSoup(response.content, "html.parser")

# Buscar el elemento con id "date"
fecha_element = soup.find("date", id="date")

# Obtener el texto del elemento (la fecha)
fecha = fecha_element.text.strip()

from selenium import webdriver
from bs4 import BeautifulSoup

# Configurar el driver de Selenium
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Ejecutar en modo headless
options.add_argument('no-sandbox')  # Desactivar sandbox
options.add_argument('disable-dev-shm-usage')  # Desactivar uso de memoria compartida

# Crear el driver
driver = webdriver.Chrome(options=options)

# Navegar a la página
driver.get("https://www.sunat.gob.pe/")

# Obtener el HTML actualizado
html = driver.page_source

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Buscar el elemento con id "date"
fecha_element = soup.find("date", id="date")

# Obtener el texto del elemento (la fecha)
fecha = fecha_element.text.strip()

# Cerrar el driver
driver.quit()

# Buscar el elemento con id "sell-rate"
venta_element = soup.find("strong", id="sell-rate")

# Obtener el texto del elemento (la venta)
venta = venta_element.text.strip()

import csv
from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Crear un diccionario con los datos
datos = {
    "Fecha": fecha_actual,
    "Venta": venta,
}

# Abrir el archivo CSV en modo append (añadir)
with open("datos.csv", "a", newline="") as csvfile:
    # Crear un escritor de CSV
    writer = csv.writer(csvfile)

    # Escribir el encabezado si el archivo está vacío
    if csvfile.tell() == 0:
        writer.writerow(["Fecha", "Venta", "Compra"])

    # Escribir los datos
    writer.writerow([datos["Fecha"], datos["Venta"]])

# Cerrar el driver
driver.quit()