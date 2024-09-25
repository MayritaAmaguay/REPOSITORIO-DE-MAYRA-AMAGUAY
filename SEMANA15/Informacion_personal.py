# Definimos el diccionario
persona = {
    "nombre": "Mayra",
    "edad": 29,
    "profesión": "Ingeniera"
}

# Modificamos y accedemos
persona["edad"] = 30
print(persona.get("ciudad", "No especificada"))

# Agregamos un nuevo campo
persona["nacionalidad"] = "Ecuatoriana"

# Eliminamos un campo
ciudad = persona.pop("ciudad", "No especificada")

# Iteramos sobre el diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
