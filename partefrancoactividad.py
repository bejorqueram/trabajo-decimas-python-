#SISTEMA DE GESTION DE RESERVAS

reservas = []

#FUNCIONES DE VALIDACION

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: no puede estar vacio.")
        
def validar_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Error: debe ser un numero mayor que cero.")
        except ValueError:
            print("Error: ingrese un numero valido.")
            
def validar_float_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            print("Error: debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese un valor valido.")
            
#FUNCIONES DE CALCULO

def calcular_total(noches, valor_noche):
    return noches * valor_noche

def calcular_categoria(total):
    if total <  200000:
        return "economica"
    elif total <= 500000:
        return "estandar"
    else:
        return "premiun"
    
#FUNCION DE BUSQUEDA

def buscar_posicion(codigo):
    for i in range(len(reservas)):
        if reservas[i]["codigo"] == codigo:
            return i
    return -1

#REGISTRAR RESERVA

def registrar_reserva():
    codigo = validar_texto("Codigo de reserva:")
    
    if buscar_posicion(codigo) != -1:
        print("ya existe una reserva con ese codigo.")
        return
    
    nombre = validar_texto("Nombre del huesped:")
    noches = validar_entero_positivo("Cantidad de noches:")
    valor_noche = validar_float_positivo("Valor por noche:")
    
    total = calcular_total(noches, valor_noche)
    categoria = calcular_categoria(total)
    
    reserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor_noche":  valor_noche,
        "total": total,
        "categoria": categoria    
    }                                            
 
    reservas.append(reserva)
    
    print("Reserva registrada correctamente.")
    
#BUSCAR RESERVAS

def buscar_reserva():
    codigo = validar_texto("Ingrese codigo de reserva:")
    
    posicion = buscar_posicion(codigo)
    
    if posicion == -1:
        print("Reserva no encontrada.")
    else:
        print("\nPosicion:", posicion)
        
        for clave, valor in reservas[posicion].items():
            print(clave, ":", valor) 
            
#ACTUALIZAR RESERVA

def actualizar_reserva():
    codigo = validar_texto("Ingrese codigo de reserva:")
    
    posicion = buscar_posicion(codigo)
    
    if posicion == -1:
        print("Reserva no encontrada.")
        return
    
    nombre = validar_texto("Nuevo nombre: ")
    noches = validar_entero_positivo("Nueva cantidad de noches: ")
    valor_noche = validar_float_positivo("Nuevo valor por noche: ")
    
    total = calcular_total(noches, valor_noche)
    categoria = calcular_categoria(total)
    
    reservas[posicion]["nombre"] = nombre
    reservas[posicion]["noches"] = noches
    reservas[posicion]["valor_noche"] = valor_noche
    reservas[posicion]["total"] = total
    reservas[posicion]["categoria"] = categoria
    
    print("Reserva actualizada correctamente.")
    
    
#ELIMINAR RESERVA

def eliminar_reserva():
    codigo = validar_texto("Ingrese codigo de reserva:")
    
    posicion = buscar_posicion(codigo)
    
    if posicion == -1:
        print("Reserva no encontrada.")
    else:
        reservas.pop(posicion)
        print("Reserva eliminada correctamente.")
        
        
#MOSTRAR RESERVAS

def mostrar_reservas():
    if len(reservas) == 0:
        print("No existen reservas registradas.")
        return
    
    print("\nLISTADO DE RESERVAS:")
    
    for reserva in reservas:
        print("-" * 40)
        for clave, valor in reserva.items():
            print(clave, ":", valor)
            
#ESTADISTICAS

def mostrar_estadisticas():
    if len(reservas) == 0:
        print("No existen reservas registradas.")
        return
    
    cantidad = len(reservas)
    
    ingresos_totales = 0
    
    for reserva in reservas:
        ingresos_totales += reserva["total"]
        
    mayor = reservas[0]
    
    for reserva in reservas:
        if reserva["total"] > mayor["total"]:
            mayor = reserva
            
    promedio = ingresos_totales / cantidad
    
    print("\nESTADISTICAS")
    print("Cantidad total de resrvas:", cantidad)
    print("Ingresos totales:", ingresos_totales)
    print("Promedio ingresos:", promedio)
    
    print("\nReserva de mayor valor:")
    for clave, valor in mayor.items():
        print(clave, ":", valor)
        
        
#MENU PRINCIPAL

def menu():
    while True:
        
        print("\n====HOTEL====")
        print("1. Registrar reserva")
        print("2. Buscar reserva")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("5. Mostrar reservas")
        print("6. Mostrar estadisticas")
        print("7. Salir")
        
        opcion = input("Seleccione una opcion:")
        
        if opcion == "1":
            registrar_reserva()
            
        elif opcion == "2":
            buscar_reserva()
            
        elif opcion ==  "3":
            actualizar_reserva()
            
        elif opcion == "4":
            eliminar_reserva()
            
        elif opcion == "5":
            mostrar_reservas()
            
        elif opcion == "6":
            mostrar_estadisticas()
            
        elif opcion == "7":
            print("Gracias por utilizar el sistema.")
            break
        
        else:
            print("Opcion invalida.")
            
            
menu()                                     
