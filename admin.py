#Búsqueda de un producto por nombre
productos = [
    {"codigo": "P001", "nombre": "Artesanía Wayuu", "categoria": "artesanías", "precio": 35000},
    {"codigo": "P002", "nombre": "Camisa Colombia", "categoria": "ropa", "precio": 55000},
    {"codigo": "P003", "nombre": "Gorra Tricolor", "categoria": "accesorios", "precio": 25000},
    {"codigo": "P004", "nombre": "Imán Bogotá", "categoria": "imanes", "precio": 10000},
    {"codigo": "P005", "nombre": "Sombrero Vueltiao", "categoria": "artesanías", "precio": 80000}
]

productos = sorted(productos, key=lambda x: x["nombre"])
    #extrae el campo nombre y ordena por ese campo
    
# Búsqueda binaria recursiva
def buscar_producto(productos, nombre, inicio=0, fin=None):
    if fin is None:
        fin = len(productos) - 1
    
    # Caso base: no encontrado
    if inicio > fin:
        return None
    
    medio = (inicio + fin) // 2
    actual = productos[medio]["nombre"]
    
    if actual == nombre:  
        return productos[medio]
    elif nombre < actual: 
        return buscar_producto(productos, nombre, inicio, medio - 1)
    else:  
        return buscar_producto(productos, nombre, medio + 1, fin)


# --- PRUEBA ---
buscado = "Imán Bogotá"
resultado = buscar_producto(productos, buscado)

if resultado:
    print("Producto encontrado:")
    for k, v in resultado.items():
        print(f"{k}: {v}")
else:
    print("El producto no existe en el inventario.")


#2. Cálculo precio total de todos los productos


def precio_total(productos, indice=0):
    # Caso base: si ya pasamos el último índice, el total es 0
    if indice == len(productos):
        return 0
    # Caso recursivo: sumar el precio actual + el resto
    return productos[indice]["precio"] + precio_total(productos, indice + 1)


# --- PRUEBA ---
total = precio_total(productos)
print(f"💰 El precio total de todos los productos es: {total}")

# 3 Precio promedio por categoría usando recursión ---

def acumular(productos, i=0, acum=None):
    if acum is None: acum = {}
    if i == len(productos): return acum
    cat, precio = productos[i]["categoria"], productos[i]["precio"]
    if cat not in acum: acum[cat] = {"suma": 0, "n": 0}
    acum[cat]["suma"] += precio; acum[cat]["n"] += 1
    return acumular(productos, i+1, acum)

def promedio_por_categoria(productos):
    datos = acumular(productos)
    return {c: datos[c]["suma"]/datos[c]["n"] for c in datos}

# --- PRUEBA ---
print(promedio_por_categoria(productos))
