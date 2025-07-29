import random   # Trae herramientas para elegir cosas al azar, como números o palabras.


# Creamos una clase llamada Producto, que es como una receta para fabricar productos.
class Producto:
    contador_id = 1  # Empezamos con el número 1 para asignar una ID única a cada producto.

    # Esto se activa cada vez que creamos un producto nuevo.
    def __init__(self, nombre, precio, categoria, stock, calificacion):
        self.id = Producto.contador_id  # Le damos una ID única al producto.
        Producto.contador_id += 1       # Subimos el contador para el próximo producto.
        self.nombre = nombre            # Guardamos el nombre del producto.
        self.precio = precio            # Guardamos el precio del producto.
        self.categoria = categoria      # Guardamos la categoría (como "ropa", "electrónica", etc.).
        self.stock = stock              # Guardamos cuántos productos hay en existencia.
        self.calificacionPromedio = calificacion  # Guardamos la calificación (del 1 al 5).

    # Esto dice cómo mostrar el producto si lo imprimimos.
    def __str__(self):
        return (
            f"ID: {self.id:02d} | "
            f"Nombre: {self.nombre:25} | "
            f"Precio: ${self.precio:7.2f} | "
            f"Categoría: {self.categoria:12} | "
            f"Stock: {self.stock:3d} | "
            f"Calificación: {self.calificacionPromedio:.1f}"
        )

'''
Este método define cómo se imprime un objeto Producto cuando haces print(producto).
Usa formato para alinear y mostrar ordenadamente:
:02d → ID con al menos 2 dígitos.
:25 → nombre del producto con un espacio reservado de 25 caracteres.
:7.2f → precio con 2 decimales, alineado.
:12 → categoría con espacio reservado de 12 caracteres.
:3d → stock como entero con 3 espacios.
:.1f → calificación con 1 decimal.
'''

# Lista de nombres para los productos base.
nombres_base = ["Smartphone", "Laptop", "Camisa", "Libro", "Silla", "Audífonos", "Lámpara", "Tablet", "Reloj", "Zapatillas"]

# Lista de categorías donde puede estar un producto.
categorias = ["Electrónica", "Ropa", "Libros", "Hogar"]

# Función para crear nombres aleatorios combinando base y un número.
def generar_nombre():
    modelo = random.randint(100, 999)  # Número aleatorio entre 100 y 999.
    return random.choice(nombres_base) + f" Modelo {modelo}"  # Une un nombre con ese número.

# Creamos una lista vacía para guardar todos los productos.
productos = []

# Vamos a crear 50 productos aleatorios.
for _ in range(50):
    nombre = generar_nombre()  # Genera un nombre como "Laptop Modelo 123".
    precio = round(random.uniform(5.00, 2000.00), 2)  # Precio al azar entre $5 y $2000.
    categoria = random.choice(categorias)  # Elige una categoría aleatoria.
    stock = random.randint(0, 100)  # Cantidad aleatoria en stock (de 0 a 100).
    calificacion = round(random.uniform(1.0, 5.0), 1)  # Calificación al azar (1.0 a 5.0).
    producto = Producto(nombre, precio, categoria, stock, calificacion)  # Crea el producto.
    productos.append(producto)  # Lo agrega a la lista.

# ==== ALGORITMO MERGE SORT ====
# Es un método para ordenar los productos (por precio, por calificación, etc.).
def merge_sort(arr, key_func, reverse=False):
    if len(arr) <= 1:
        return arr  # Si la lista es muy pequeña, ya está ordenada.
    mid = len(arr) // 2  # Dividimos la lista en dos mitades.
    left = merge_sort(arr[:mid], key_func, reverse)  # Ordenamos la primera mitad.
    right = merge_sort(arr[mid:], key_func, reverse)  # Ordenamos la segunda mitad.
    return merge(left, right, key_func, reverse)  # Unimos ambas mitades ya ordenadas.

# Parte que junta dos mitades de lista en orden correcto.
def merge(left, right, key_func, reverse):
    result = []  # Lista vacía donde guardamos el orden final.
    i = j = 0
    while i < len(left) and j < len(right):
        if reverse:
            condition = key_func(left[i]) > key_func(right[j])
        else:
            condition = key_func(left[i]) < key_func(right[j])
'''
Compara los elementos usando key_func, que es una función que indica qué atributo usar para ordenar 
(precio, calificación, etc.). Si reverse=True, el orden es descendente y Si reverse=False, el orden 
es ascendente.
'''
#Agrega al result el elemento menor (o mayor si es descendente). Avanza el índice correspondiente (i o j).
        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])   # Agrega lo que queda de la izquierda.
    result.extend(right[j:])  # Agrega lo que queda de la derecha.
    return result #Devuelve la lista fusionada y ordenada.

# ==== ALGORITMO INSERTION SORT ====
# Otro método para ordenar, más lento pero más fácil de entender.
def insertion_sort(arr, key_func, reverse=False):
    for i in range(1, len(arr)):
        key_item = arr[i]  # Guardamos el producto actual.
        j = i - 1

'''
Se crea un bucle repetitivo For, donde comienza desde el segundo elemento 
(índice 1). key_item es el producto actual que se va a insertar en su posición 
correcta. j es el índice del elemento anterior.
'''
        
        while j >= 0 and (
            key_func(arr[j]) > key_func(key_item) if not reverse else key_func(arr[j]) < key_func(key_item)
        ):
            arr[j + 1] = arr[j]  # Movemos el producto anterior hacia adelante.
            j -= 1
        arr[j + 1] = key_item  # Ponemos el producto en su lugar correcto.
    return arr #Devuelve el arreglo ordenado en el mismo lugar (ordenamiento in-place).

'''En este bucle while se compara el key_item con los elementos anteriores. Si el elemento anterior es mayor 
(o menor si reverse=True), lo desplaza a la derecha.
'''

# ==== BÚSQUEDA BINARIA POR ID ====
# Sirve para buscar un producto rápidamente si la lista está ordenada por ID.
def busqueda_binaria(lista, id_buscado):
    izquierda, derecha = 0, len(lista) - 1

'''
Define los límites de búsqueda: izquierda: inicio del arreglo (índice 0) y derecha: fin del arreglo (último índice).
Esto es necesario porque la búsqueda binaria trabaja acotando un rango dentro de la lista.
'''
    # Bucle que se ejecuta mientras haya elementos por revisar
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Buscamos el centro de la lista.
        # Si el ID del producto en la posición medio es igual al id_buscado, se encontró el producto y se retorna.
        if lista[medio].id == id_buscado:
            return lista[medio]  # Lo encontramos.
            
        #Si el ID en el medio es menor que el buscado, significa que el producto está en la mitad derecha, 
        #así que se mueve el límite izquierdo hacia medio + 1.
        elif lista[medio].id < id_buscado:
            izquierda = medio + 1

        # Si el ID en el medio es mayor, se busca en la mitad izquierda, moviendo el límite derecho a medio - 1.
        else:
            derecha = medio - 1
    return None  # Si no lo encuentra, regresa nada.

# ==== IMPRIMIR PRODUCTOS ====
# Imprime un encabezado decorativo antes de mostrar los productos.
def imprimir_productos(lista):
    print("\n" + "=" * 110)
    print("CATÁLOGO DE PRODUCTOS ORDENADOS")
    print("=" * 110)
    for producto in lista:
        print(producto)  
    print("=" * 110)

'''
Recorre toda la lista y muestra cada producto. El método __str__ definido en la clase Producto se encarga 
de dar formato a cada impresión.
'''

# ==== MENÚ PRINCIPAL ====
# Aquí es donde el usuario elige qué quiere hacer.
def menu():
    productos_ordenados = productos.copy()  # Hacemos una copia de la lista de productos.
    productos_por_id = []  # Lista vacía para ordenar por ID solo si se necesita.

    while True:
        print("\n MENÚ PRINCIPAL:")
        print("1. Ordenar productos")
        print("2. Buscar productos por ID (requiere orden por ID)")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")  # El usuario elige qué hacer.

        if opcion == "1":
            # Elige cómo se van a ordenar
            print("\nCriterios de ordenamiento:")
            print("1. Precio (Ascendente)")
            print("2. Calificación Promedio (Descendente)")
            criterio = input("Selecciona criterio (1 o 2): ")

            print("\nAlgoritmos disponibles:")
            print("A. Merge Sort")
            print("B. Insertion Sort")
            algoritmo = input("Selecciona algoritmo (A o B): ").strip().upper()

            # Dependiendo de la opción, definimos cómo comparar los productos
            if criterio == "1":
                key_func = lambda p: p.precio  # Usamos el precio.
                reverse = False  # Orden de menor a mayor.
            elif criterio == "2":
                key_func = lambda p: p.calificacionPromedio  # Usamos la calificación.
                reverse = True  # Orden de mayor a menor.
            else:
                print(" Criterio inválido.")
                continue  # Vuelve al menú.

            # Elegimos el algoritmo correcto.
            if algoritmo == "A":
                productos_ordenados = merge_sort(productos.copy(), key_func, reverse)
            elif algoritmo == "B":
                productos_ordenados = insertion_sort(productos.copy(), key_func, reverse)
            else:
                print(" Algoritmo inválido.")
                continue

            imprimir_productos(productos_ordenados)  # Mostramos los productos ordenados.

        elif opcion == "2":
            if not productos_por_id:
                print("\n Ordenando productos por ID (requerido para búsqueda binaria)...")
                productos_por_id = merge_sort(productos.copy(), key_func=lambda p: p.id)

            print("\n Ingrese IDs de producto para buscar. Escriba 'salir' para volver al menú.\n")
            while True:
                entrada = input("Ingrese un ID (o 'salir'): ")
                if entrada.strip().lower() == "salir":
                    break
                if not entrada.isdigit():
                    print(" Entrada inválida. Ingrese solo números.")
                    continue
                id_buscar = int(entrada)
                resultado = busqueda_binaria(productos_por_id, id_buscar)
                if resultado:
                    print(f" Producto encontrado:\n{resultado}")
                else:
                    print(" Producto no encontrado.")

# Al final, activamos el menú para que el programa funcione.
menu()
