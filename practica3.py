intentos = 0
while intentos <= 5:
    numero = input("Introduce un número")
    try:
        numero_int = int(numero)
        print("Número válido")
        break
    except:
        intentos = intentos + 1
        print("Número inválido, prueba otra vez")
