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