from os import system
class Nodo:
    def __init__(self, num):
        self.num = num
        self.izq = None
        self.der = None

    def insertar(self, num):
        if num <= self.num:
            print(f"{num} <= {self.num}")
            if self.izq is None:
                self.izq = Nodo(num)
            else:
                self.izq.insertar(num)
        else:
            print(f"{num} > {self.num}")
            if self.der is None:
                self.der = Nodo(num)
            else:
                self.der.insertar(num)

    def buscar(self, num):
        if num == self.num:
            return True
        elif num < self.num:
            if self.izq is None:
                return False
            return self.izq.buscar(num)
        else:
            if self.der is None:
                return False
            return self.der.buscar(num)


ar_bi = Nodo(60)
numeros = [70, 30, 20, 53, 90, 80, 96, 35, 40, 40, 50, 33]
for numero in numeros:
    ar_bi.insertar(numero)
system("cls")


ar_bi.insertar(33)
a= ar_bi.buscar(33)
if a is True:
    print(f"El número {33} esta arbol")
else:
    print(f"El número {33} no esta arbol")
