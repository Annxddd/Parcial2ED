import random
import time

# Clase Producto
class Producto:
    contador_id = 1

    def __init__(self, nombre, precio, categoria, stock, calificacion):
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacionPromedio = calificacion

    def __str__(self):
        return (
            f"ID: {self.id:02d} | "
            f"Nombre: {self.nombre:25} | "
            f"Precio: ${self.precio:7.2f} | "
            f"Categoría: {self.categoria:12} | "
            f"Stock: {self.stock:3d} | "
            f"Calificación: {self.calificacionPromedio:.1f}"
        )

# Datos base
nombres_base = ["Smartphone", "Laptop", "Camisa", "Libro", "Silla", "Audífonos", "Lámpara", "Tablet", "Reloj", "Zapatillas"]
categorias = ["Electrónica", "Ropa", "Libros", "Hogar"]

# Generador de nombre aleatorio
def generar_nombre():
    modelo = random.randint(100, 999)
    return random.choice(nombres_base) + f" Modelo {modelo}"

# Generar productos
productos = []
for _ in range(50):
    nombre = generar_nombre()
    precio = round(random.uniform(5.00, 2000.00), 2)
    categoria = random.choice(categorias)
    stock = random.randint(0, 100)
    calificacion = round(random.uniform(1.0, 5.0), 1)
    producto = Producto(nombre, precio, categoria, stock, calificacion)
    productos.append(producto)

# MERGE SORT
def merge_sort(arr, key_func, reverse=False):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_func, reverse)
    right = merge_sort(arr[mid:], key_func, reverse)
    return merge(left, right, key_func, reverse)

def merge(left, right, key_func, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if reverse:
            condition = key_func(left[i]) > key_func(right[j])
        else:
            condition = key_func(left[i]) < key_func(right[j])
        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# INSERTION SORT
def insertion_sort(arr, key_func, reverse=False):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and (
            key_func(arr[j]) > key_func(key_item) if not reverse else key_func(arr[j]) < key_func(key_item)
        ):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# Búsqueda binaria
def busqueda_binaria(lista, id_buscado):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].id == id_buscado:
            return lista[medio]
        elif lista[medio].id < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# Imprimir productos
def imprimir_productos(lista):
    print("\n" + "=" * 110)
    print("CATÁLOGO DE PRODUCTOS ORDENADOS")
    print("=" * 110)
    for producto in lista:
        print(producto)
    print("=" * 110)

# Menú principal
def menu():
    productos_ordenados = productos.copy()
    productos_por_id = []
    while True:
        print("\n🔧 MENÚ PRINCIPAL:")
        print("1. Ordenar productos")
        print("2. Buscar productos por ID (requiere orden por ID)")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print("\nCriterios de ordenamiento:")
            print("1. Precio (Ascendente)")
            print("2. Calificación Promedio (Descendente)")
            criterio = input("Selecciona criterio (1 o 2): ")

            print("\nAlgoritmos disponibles:")
            print("A. Merge Sort")
            print("B. Insertion Sort")
            algoritmo = input("Selecciona algoritmo (A o B): ").strip().upper()

            # Configurar clave y orden
            if criterio == "1":
                key_func = lambda p: p.precio
                reverse = False
            elif criterio == "2":
                key_func = lambda p: p.calificacionPromedio
                reverse = True
            else:
                print("❌ Criterio inválido.")
                continue

            if algoritmo == "A":
                productos_ordenados = merge_sort(productos.copy(), key_func, reverse)
            elif algoritmo == "B":
                productos_ordenados = insertion_sort(productos.copy(), key_func, reverse)
            else:
                print("❌ Algoritmo inválido.")
                continue

            imprimir_productos(productos_ordenados)

        elif opcion == "2":
            if not productos_por_id:
                print("\n🔍 Ordenando productos por ID (requerido para búsqueda binaria)...")
                productos_por_id = merge_sort(productos.copy(), key_func=lambda p: p.id)
            print("\n🔎 Ingrese IDs de producto para buscar. Escriba 'salir' para volver al menú.\n")
            while True:
                entrada = input("Ingrese un ID (o 'salir'): ")
                if entrada.strip().lower() == "salir":
                    break
                if not entrada.isdigit():
                    print("❌ Entrada inválida. Ingrese solo números.")
                    continue
                id_buscar = int(entrada)
                resultado = busqueda_binaria(productos_por_id, id_buscar)
                if resultado:
                    print(f"✅ Producto encontrado:\n{resultado}")
                else:
                    print("❌ Producto no encontrado.")


# Ejecutar menú
menu()