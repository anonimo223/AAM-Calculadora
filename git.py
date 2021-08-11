class trabajo:

    def __init__ (self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def funcion_sumar(self):
        return self.numero1 + self.numero2

    def funcion_restar(self):
        return self.numero1 - self.numero2

    def funcion_multiplicar(self):
        return self.numero1 * self.numero2

    def funcion_dividir(self):
        return self.numero1 / self.numero2

trabajo_objeto = trabajo(int(input("Ingrese el numero 1: ")), int(input("Ingrese el numero 2: ")))
print(f"El resultado de la suma es: {trabajo_objeto.funcion_sumar()}")
print(f"El resultado de la resta es: {trabajo_objeto.funcion_restar()}")
#hola
print(f"El resultado de la multiplicacion es: {trabajo_objeto.funcion_multiplicar()}")
print(f"El resultado su division es: {trabajo_objeto.funcion_dividir()}")
