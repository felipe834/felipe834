from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Caminho relativo ou absoluto para o geckodriver
gecko_path = "geckodriver"  # ou use o caminho absoluto, ex: "/home/seuusuario/PycharmProjects/tkinter/geckodriver"

# Opções (opcional, mas recomendado evitar abertura do terminal)
options = Options()
options.headless = False  # Se quiser sem interface gráfica, use True

# Criando o driver com o caminho customizado
service = FirefoxService(executable_path=gecko_path)
driver = webdriver.Firefox(service=service, options=options)

# Testando
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
