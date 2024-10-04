# Escritura en un archivo de texto
# Abre (o crea) el archivo my_notes.txt en modo escritura ("w")
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales
    file.write("Esta es mi primera nota personal.\n")
    file.write("Hoy aprendí cómo manipular archivos en Python.\n")
    file.write("El uso de 'with' asegura que el archivo se cierre automáticamente.\n")

# Lectura de un archivo de texto
# Abre el archivo my_notes.txt en modo lectura ("r")
with open('my_notes.txt', 'r') as file:
    # Lee y muestra cada línea del archivo
    for line in file:
        print(line.strip())  # strip() para eliminar saltos de línea adicionales

# El archivo se cierra automáticamente al salir de los bloques 'with'
