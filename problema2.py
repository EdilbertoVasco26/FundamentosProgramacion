# ---------------------------------------------------------
# FUNCIÓN:
# Calcula el precio final de un producto aplicando
# un descuento del 15% si cumple las condiciones.
# ---------------------------------------------------------

def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):

    descuento = 0.15

    # Verificar condiciones para aplicar descuento
    if categoria == categoria_objetivo and precio_base > umbral:

        precio_final = precio_base - (precio_base * descuento)

    else:

        precio_final = precio_base

    return precio_final


# ---------------------------------------------------------
# MATRIZ DEL MENÚ
# Formato:
# [Nombre del Producto, Categoría, Precio Base]
# ---------------------------------------------------------

menu = [

    ["Hamburguesa Especial", "Plato Fuerte", 25000],
    ["Pizza Hawaiana", "Plato Fuerte", 30000],
    ["Gaseosa Personal", "Bebida", 5000],
    ["Helado de Vainilla", "Postre", 12000],
    ["Pasta Alfredo", "Plato Fuerte", 22000],
    ["Jugo Natural", "Bebida", 8000]

]


# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PROMOCIÓN
# ---------------------------------------------------------

categoria_objetivo = "Plato Fuerte"
umbral = 20000


# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------

print("===================================================")
print("        MENÚ DEL RESTAURANTE - PROMOCIONES")
print("===================================================")

print("\nCategoría con descuento:", categoria_objetivo)
print("Descuento aplicado: 15%")
print("Precio mínimo para descuento: $", umbral)

print("\n===================================================")
print("LISTADO DE PRODUCTOS")
print("===================================================")


# ---------------------------------------------------------
# RECORRER MATRIZ Y MOSTRAR RESULTADOS
# ---------------------------------------------------------

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamar función
    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    # Mostrar información
    print("\n-------------------------------------------")
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)

    # Verificar si tuvo descuento
    if precio_base != precio_final:

        print("Promoción aplicada: SÍ")
        print("Precio Final con Descuento: $", round(precio_final, 2))

    else:

        print("Promoción aplicada: NO")
        print("Precio Final: $", precio_final)

print("\n===================================================")
print("   PROCESO FINALIZADO CORRECTAMENTE")
print("===================================================")