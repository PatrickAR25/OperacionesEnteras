class numeroEntero:
    def MCD (self,a,b):
        x = abs(a)
        y = abs(b)

        while y !=0:
            remainder = x % y
            x = y
            y = remainder
        return x

numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo Numero: "))

operacion = numeroEntero()
print(f"MCD de {numero1}, {numero2} es {operacion.MCD(numero1,numero2)}")