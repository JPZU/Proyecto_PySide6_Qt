import json
from helpers import absPath

datos = []

datos.append({
    "nombre": "Juan",
    "empleo": "Instructor",
    "email": "juan@gmail.com"
})


contactos = [("Andres 1","Astronomo 1","andres@astronomo1"),
             ("Andres 2","Astronomo 2","andres@astronomo2"),
             ("Andres 3","Astronomo 3","andres@astronomo3"),
             ("Andres 4","Astronomo 4","andres@astronomo4")]

for nombre, empleo, email in contactos:
    datos.append({
        "nombre": nombre,
        "empleo": empleo,
        "email": email
    })
    
# print(datos)


# Guardar registros en json
with open(absPath("contactos.json"), "w") as fichero:
    datos = json.dump(datos, fichero) 
    
# datos = None

with open(absPath("contactos.json")) as fichero:
    datos = json.load(fichero)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])