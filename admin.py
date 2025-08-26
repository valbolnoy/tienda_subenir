
productos = [
    {"codigo": "P001", "nombre": "Artesanía Wayuu", "categoria": "artesanías", "precio": 35000},
    {"codigo": "P002", "nombre": "Camisa Colombia", "categoria": "ropa", "precio": 55000},
    {"codigo": "P003", "nombre": "Gorra Tricolor", "categoria": "accesorios", "precio": 25000},
    {"codigo": "P004", "nombre": "Imán Bogotá", "categoria": "imanes", "precio": 10000},
    {"codigo": "P005", "nombre": "Sombrero Vueltiao", "categoria": "artesanías", "precio": 80000}
]


productos = sorted(productos, key=lambda x: x["nombre"])

def buscar_producto(productos, nombre, inicio=0, fin=None):
    if fin is None:         
        fin = len(productos) - 1  
    if inicio > fin: 
        return None
    
    medio = (inicio + fin) // 2  
    actual = productos[medio]["nombre"]   

    if actual.lower().strip() == nombre.lower().strip(): 
        return productos[medio]     
    if nombre.lower().strip() < actual.lower().strip(): 
        return buscar_producto(productos, nombre, inicio, medio - 1)
    return buscar_producto(productos, nombre, medio + 1, fin)
    


def precio_total(productos, indice=0):
    if indice == len(productos):
        return 0
    return productos[indice]["precio"] + precio_total(productos, indice + 1)


def acumular(productos, i=0, acum=None):
    if acum is None:
        acum = {} 
    if i == len(productos):
        return acum
    
    cat = productos[i]["categoria"]
    precio = productos[i]["precio"]

    if cat not in acum:
        acum[cat] = {"suma": 0, "n": 0} 
    acum[cat]["suma"] += precio
    acum[cat]["n"] += 1
    
    return acumular(productos, i + 1, acum)


def promedio_por_categoria(productos, i=0, acum=None):
    if acum is None:
        acum = {}
    if i == len(productos):
        return calcular_promedios(list(acum.items()))

    prod = productos[i]
    cat = prod["categoria"]  
    precio = prod["precio"] 

   
    if cat not in acum:
        acum[cat] = {"suma": 0, "n": 0}

    acum[cat]["suma"] += precio
    acum[cat]["n"] += 1
    return promedio_por_categoria(productos, i + 1, acum)


def calcular_promedios(items, resultado=None):
    if resultado is None:
        resultado = {}

    if not items:
        return resultado
    cat, info = items[0]
    resultado[cat] = info["suma"] / info["n"]
    return calcular_promedios(items[1:], resultado)
    


def quicksort_precio(productos, ascendente=True):
    if len(productos) <= 1:
        return productos

    pivote = productos[0]

    def dividir(resto, menores=None, mayores=None):
        if menores is None: menores, mayores = [], []
        if not resto:  
            return menores, mayores
        cabeza, *cola = resto
        (menores if cabeza["precio"] <= pivote["precio"] else mayores).append(cabeza)
        return dividir(cola, menores, mayores)

    menores, mayores = dividir(productos[1:])
    ordenados = quicksort_precio(menores, ascendente) + [pivote] + quicksort_precio(mayores, ascendente)
    return ordenados if ascendente else ordenados[::-1]

def buscar_por_rango(productos, minimo, maximo, i=0):
    if i == len(productos):
        return [] 
    
    actual = productos[i]
    if minimo <= actual["precio"] <= maximo: 
        return [actual] + buscar_por_rango(productos, minimo, maximo, i + 1)
    return buscar_por_rango(productos, minimo, maximo, i + 1)

def recomendar_misma_categoria(productos, producto_base, i=0):
    if i == len(productos):
        return []
    
    actual = productos[i]
    if actual["categoria"] == producto_base["categoria"] and actual["codigo"] != producto_base["codigo"]:
        return [actual] + recomendar_misma_categoria(productos, producto_base, i + 1)
    
    return recomendar_misma_categoria(productos, producto_base, i + 1)

def menu():
    print("\n MENÚ DE LA TIENDA")
    print("1. Ver precio total")
    print("2. Ver promedio por categoría")
    print("3. Buscar producto por nombre")
    print("4. Buscar productos por rango de precios")
    print("5. Recomendar productos de la misma categoría")
    print("6. Salir")

    opcion = input(" Elige una opción: ")

    if opcion == "1":
        print(f"\n🪙 Precio total: {precio_total(productos)}")
        return menu()

    if opcion == "2":
        promedios = promedio_por_categoria(productos)
        print("\n Promedio por categoría:")
        for cat, valor in promedios.items():
            print(f"   {cat}: {round(valor,2)}")
        return menu()

    if opcion == "3":
        nombre = input(" Escribe el nombre del producto a buscar: ")
        resultado = buscar_producto(productos, nombre)
        if resultado:
            print(f" Encontrado: {resultado['nombre']} - ${resultado['precio']}")
        else:
            print(" Producto no encontrado.")
        return menu()

    if opcion == "4":
        minimo = int(input("🔽 Precio mínimo: "))
        maximo = int(input("🔼 Precio máximo: "))
        encontrados = buscar_por_rango(productos, minimo, maximo)
        if encontrados:
            print("\n Productos encontrados:")
            for p in encontrados:
                print(f"   {p['nombre']} - ${p['precio']}")
        else:
            print(" No hay productos en ese rango.")
        return menu()

    if opcion == "5":
        nombre = input(" Escribe el nombre del producto base: ")
        base = buscar_producto(productos, nombre)
        if base:
            recomendados = recomendar_misma_categoria(productos, base)
            if recomendados:
                print(f"\n Recomendaciones en categoría '{base['categoria']}':")
                for p in recomendados:
                    print(f"   {p['nombre']} - ${p['precio']}")
            else:
                print(" No hay recomendaciones en la misma categoría.")
        else:
            print(" Producto base no encontrado.")
        return menu()

    if opcion == "6":
        print("👋 Saliendo del programa...")
        return 

    print("⚠️ Opción no válida, intenta de nuevo.")
    return menu()  

menu()    



