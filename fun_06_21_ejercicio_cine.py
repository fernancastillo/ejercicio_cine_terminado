import os, time, msvcrt, csv
ventas=[]
letras=["A","B","C","D", "E"]
asientos=[[a for a in range(1,11)] for x in range (5)]

def opc_1():
    print("\t\tASIENTOS DISPONIBLES\n")
    print(" -"+"-"*47+"- ")
    for x in range(len(asientos)):
        print("|\t",letras[x],asientos[x],"\t  |")
    print(" -"+"-"*47+"- ")

def opc_2():
    print("\tCOMPRAR ENTRADAS\n")
    print("La entrada tiene un valor de $4000 (con descuento para personas menores de 18 y mayores de 65 años)")
    while True:
        asiento_letra=input("Ingrese la letra del asiento (A, B, C, D o E): ")
        for x in letras:
            if x==asiento_letra.upper():
                break
        if x==asiento_letra.upper():
            numero_x=letras.index(asiento_letra.upper())
            break
        else:
            print("Error, debe ingresar una letra correcta!")  
            time.sleep(2)
    while True:  
        try:   
            asiento_numero=int(input("Ingrese el número del asiento: "))
            if asiento_numero in asientos[0]:
                numero_y=asiento_numero-1
                break
            else:
                print("Error! Debe ingresar un número del 1 al 10!")
        except:
            print("Error! Debe ingresar un número entero!")
    if asientos[numero_x][numero_y]=="X":
        print("Error! asiento ocupado!")
        time.sleep(2)
    else:
        nombre=validacion_nombre()
        edad=validacion_edad()
        telefono=validacion_telefono()
        valor_entrada=4000
        if edad<18:
            monto_total=round(valor_entrada-valor_entrada*0.2)
        elif edad>65:
            monto_total=round(valor_entrada-valor_entrada*0.15)
        else:
            monto_total=valor_entrada
        venta={
            "nombre":nombre,
            "edad":edad,
            "telefono":telefono,
            "asiento":str(letras[numero_x])+str(asientos[0][numero_y]),
            "valor":monto_total
        }
        asientos[numero_x][numero_y]="X"
        ventas.append(venta)
        os.system("cls")
        print("Venta realizada con éxito!")
        print(f"Valor de entrada: $ {monto_total}.")
        
def opc_3():
    print("\tMOSTRAR VENTAS REALIZADAS:\n")
    for v in ventas:
        print(f"Nombre: {v['nombre']} - Edad: {v['edad']}- Teléfono: {v['telefono']}- Asiento: {v['asiento']} - Valor entrada: $ {v['valor']}\n")

def opc_4():
    print("\tGENERAR ARCHIVO CSV DE VENTAS:\n")
    if len(ventas)==0:
        print("Aún no se ha realizado ninguna venta. Presione '2' en el menú para comenzar.")
    else:
        nombre_archivo=input("Ingrese el nombre del archivo: ")
        with open(f"{nombre_archivo}.csv","w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["nombre","edad","telefono","asiento","valor"])
            escritor.writeheader()
            escritor.writerows(ventas)
        print("Archivo creado con éxito.")

def opc_5():
    print("Hasta la próxima!")
    exit()

def validacion_menu(lista_menu):
    while True:
        try:
            opc=int(input("Ingrese un número del menú: "))
            if opc in lista_menu:
                os.system("cls")
                return opc
            else:
                print("Error! Debe ingresar un número del menú!")
                time.sleep(2)
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)

def validacion_nombre():
    while True:
        nombre=input("Ingrese el nombre del comprador: ")
        if len(nombre)<3:
            print("Error! Debe ingresar al menos 3 caracteres!")
            time.sleep(2)
        else:
            return nombre
        
def validacion_edad():
    while True:
        try:
            edad=int(input("Ingrese la edad del comprador: "))
            if edad<=0:
                print("Error! Debe ingresar un número mayor a 0!")
            else:
                return edad
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)

def validacion_telefono():
    while True:
        try:
            telefono=int(input("Ingrese el teléfono del comprador (+56): "))
            if len(str(telefono))==9 and str(telefono)[0]=='9':
                return telefono
            else:
                print("Error! El número debe comenzar con 9 y tener 9 dígitos!")
                time.sleep(2)
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)
