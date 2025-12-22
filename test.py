import requests

respuesta = requests.get("https://www.programacionfacil.org/", timeout=5)

contenido = respuesta.content.decode("utf-8")

print(contenido)
print(respuesta)

45:27 ni