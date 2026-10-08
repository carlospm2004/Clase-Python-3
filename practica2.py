lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
edad_objetivo1 = 18
edad_objetivo2 = 65

for edad in lista_edades:
    if edad >= edad_objetivo1 and edad <= edad_objetivo2:
        print(edad)
    elif edad >= edad_objetivo1 and edad >= edad_objetivo2:
        break

    


