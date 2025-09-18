class Queue:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, self.__list))

    def enqueue(self, e):
        self.__list.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def first(self):
        if self.is_empty():
            return None
        return self.__list[0]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)


class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, reversed(self.__list)))

    def push(self, e):
        self.__list.append(e)
        return True

    def pop(self):
        if self.is_empty():
            return None
        return self.__list.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.__list[-1]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)


#-----------------------------
class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad 
        self.visitantes = Stack()  

    def agregar_visitante(self, visitante):
        self.visitantes.push(visitante)  

    def procesar_turno(self):
        procesados = []
        for _ in range(self.capacidad):
            if not self.visitantes.is_empty():
                procesados.append(self.visitantes.pop())
        return procesados  

    def __str__(self):
        return f"{self.nombre}: {self.visitantes}" 


class ParqueDiversiones:
    def __init__(self):
        self.atracciones = Queue() 
        self.atracciones.enqueue(Atraccion("Montaña Rusa", 3))
        self.atracciones.enqueue(Atraccion("Carros Chocones", 2))  
        self.atracciones.enqueue(Atraccion("Rueda de la Fortuna", 2))
        self.atracciones.enqueue(Atraccion("Casa del Terror", 2))

    def agregar_visitante(self, visitante):
        primera = self.atracciones.first()  
        if primera:
            primera.agregar_visitante(visitante) 

    def ejecutar_turno(self):
        print("\n--- Ejecutando Turno ---")
        procesados_siguiente = [] 
        nueva_cola = Queue()  

        while not self.atracciones.is_empty():
            atraccion = self.atracciones.dequeue()   

            for v in procesados_siguiente:
                atraccion.agregar_visitante(v)
            procesados_siguiente = []  
            procesados = atraccion.procesar_turno() 
            procesados_siguiente = procesados

            print(f"{atraccion.nombre} -> Procesados: {procesados}, "
                  f"En espera: {atraccion.visitantes}")

            nueva_cola.enqueue(atraccion) 

        self.atracciones = nueva_cola

    def ejecutar_todo(self):
        turno = 1 
        while self.hay_visitantes():
            print(f"\n=== TURNO {turno} ===") 
            self.ejecutar_turno() 
            turno += 1 
        print("\n Todos los visitantes han salido del parque.")

    def estado(self):
        print("\n--- Estado del Sistema ---")
        temporal = Queue() 

        while not self.atracciones.is_empty():
            atraccion_actual = self.atracciones.dequeue() 
            print(atraccion_actual)
            temporal.enqueue( atraccion_actual)

      
        self.atracciones = temporal   

    def hay_visitantes(self, temp=None):
     if temp is None:
        temp = Queue()

     if self.atracciones.is_empty():
        self.atracciones = temp  
        return False

    
     atraccion_actual = self.atracciones.dequeue()  
     temp.enqueue(atraccion_actual)

     if not atraccion_actual.visitantes.is_empty(): 
        while not self.atracciones.is_empty():
            temp.enqueue(self.atracciones.dequeue())
        self.atracciones = temp 
        return True

    
     return self.hay_visitantes(temp)  


    def agregar_atraccion(self, nombre, capacidad):
        """Agrega una nueva atracción al final de la cola"""
        print(f"\n Atracción '{nombre}' agregada con capacidad {capacidad}.")

    def eliminar_atraccion(self, nombre):
        """Elimina una atracción y pasa sus visitantes a la siguiente"""
        nueva_cola = Queue()
        encontrada = False 

        while not self.atracciones.is_empty():
            atraccion = self.atracciones.dequeue()
            if atraccion.nombre == nombre:
                encontrada = True
              
                if not self.atracciones.is_empty(): 
                    siguiente = self.atracciones.first() 
                    while not atraccion.visitantes.is_empty():
                        siguiente.agregar_visitante(atraccion.visitantes.pop())
                print(f"\n⚠️ Atracción '{nombre}' eliminada.")
            else:
                nueva_cola.enqueue(atraccion)

        self.atracciones = nueva_cola 
        if not encontrada:
            print(f"\n No se encontró la atracción '{nombre}'.")


#--------------------------------------------------------------------------------------------------------------------------------------

def menu():
    parque = ParqueDiversiones()

    while True:
        print("\n===== MENÚ PARQUE DE DIVERSIONES =====")
        print("1. Agregar visitante")
        print("2. Ejecutar un turno")
        print("3. Ejecutar todos los turnos")
        print("4. Consultar estado del sistema")
        print("5. Agregar atracción")
        print("6. Eliminar atracción")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            visitante = input("Nombre del visitante (ej: A1, N1): ")
            parque.agregar_visitante(visitante)
            print(f"Visitante {visitante} agregado.")

        elif opcion == "2":
            parque.ejecutar_turno()

        elif opcion == "3":
            parque.ejecutar_todo()

        elif opcion == "4":
            parque.estado()

        elif opcion == "5":
            nombre = input("Nombre de la nueva atracción: ")
            capacidad = int(input("Capacidad de la atracción por turno: "))
            parque.agregar_atraccion(nombre, capacidad)

        elif opcion == "6":
            nombre = input("Nombre de la atracción a eliminar: ")
            parque.eliminar_atraccion(nombre)

        elif opcion == "0":
            print(" Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()






