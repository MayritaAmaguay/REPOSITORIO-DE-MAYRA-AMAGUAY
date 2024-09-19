def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo monto total
    monto1 = 200  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    print(f"El descuento en una compra de {monto1} es: {descuento1}")  # Salida: 20.0

    # Segunda llamada: monto total y porcentaje de descuento
    monto2 = 150  # Monto total de la compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    print(f"El descuento en una compra de {monto2} con un descuento del {porcentaje_descuento2}% es: {descuento2}")  # Salida: 22.5
