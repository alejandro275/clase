productos = []

while True:
    print("\n--- Menú ---")
    print("1. Registrar Producto")
    print("2. Consultar Datos de Producto")
    print("3. Listar Productos")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        while True:
            codigo = input("Ingrese código de producto (ej. P001): ")
            if len(codigo) != 4 or codigo[0].upper() != 'P':
                print("El código debe tener 4 caracteres y comenzar con 'P'. Intente nuevamente.")
                continue
            existe = False
            for prod in productos:
                if prod['codigo'] == codigo:
                    existe = True
                    break
            if existe:
                print("¡Este código de producto ya existe! Intenta con otro.")
                continue

            nombre = input("Ingrese el nombre del producto: ")
            if nombre == "":
                print("El nombre no puede estar vacío. Intente nuevamente.")
                continue

            try:
                precio = int(input("Ingrese el precio (mayor o igual a $1000): "))
                if precio < 1000:
                    print("El precio debe ser mayor o igual a $1000.")
                    continue
            except:
                print("Precio inválido, debe ser un número entero.")
                continue

            try:
                stock = int(input("Ingrese el stock (entre 1 y 99): "))
                if stock <= 0 or stock >= 100:
                    print("El stock debe ser mayor que 0 y menor que 100.")
                    continue
            except:
                print("Stock inválido, debe ser un número entero.")
                continue

            productos.append({'codigo': codigo, 'nombre': nombre, 'precio': precio, 'stock': stock})
            print("Producto registrado correctamente.")
            break

    elif opcion == '2':
        codigo = input("Ingrese el código del producto a buscar: ")
        encontrado = False
        for prod in productos:
            if prod['codigo'] == codigo:
                print("Producto encontrado:")
                print("Código:", prod['codigo'])
                print("Nombre:", prod['nombre'])
                print("Precio: $", prod['precio'])
                print("Stock:", prod['stock'])
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == '3':
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Listado de productos:")
            for prod in productos:
                print("Código:", prod['codigo'], "| Nombre:", prod['nombre'], "| Precio: $", prod['precio'], "| Stock:", prod['stock'])

    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

