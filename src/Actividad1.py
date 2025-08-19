
def par_impar(): 
    print("Funcion para culcular si un numero ingresado es par o impar")
    while True:
        try:
            numero_a_calcular = int(input("ingresar un numero entero:"))
            break
        
    except Exception as err:
        print ("Ingresa un numero valido")
        print(err)
    
    par_impar = numero_a_calcular %2

    if par_impar == 0:
        print("numero par")
    else:
        print("numro impar")


