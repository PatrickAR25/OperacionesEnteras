from NumeroEntero import NumeroEntero

if __name__ == '__main__':
    numero1=int(input("Primer Numero: "))
    numero2=int(input("Segundo Numero: "))

    operacion = NumeroEntero()
    print(f"MCD de {5} {10} es {operacion.MCD(numero1,numero2)}")