from fun_06_21_ejercicio_cine import *
os.system("cls")
while True:
    print("\tMENÚ CINE\n")
    print("1. Mostrar asientos disponibles")
    print("2. Comprar entrada")
    print("3. Mostrar ventas realizadas")
    print("4. Generar archivo CSV de ventas")
    print("5. Salir")
    opc=validacion_menu([1,2,3,4,5])
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    elif opc==4:
        opc_4()
    else:
        opc_5()
    print(">Presione una tecla para continuar<")
    msvcrt.getch()
    os.system("cls")