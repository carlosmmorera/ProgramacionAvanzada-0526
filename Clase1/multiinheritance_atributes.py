# Atributos de clase con el mismo nombre
class PadreA:
    valor = "valor en PadreA"

class MadreA:
    valor = "valor en MadreA"

class Hijo1(PadreA, MadreA):
    pass

print("\n\n---------------- Ejemplo 1 ----------------")
hijo1 = Hijo1()
print(hijo1.valor)





# Atributo redefinido en la clase hija
class Hijo2(PadreA, MadreA):
    valor = "valor en Hijo2"

print("\n\n---------------- Ejemplo 2 ----------------")
hijo2 = Hijo2()
print(hijo2.valor)




# Atributos de instancia con el mismo nombre
class PadreB:
    def __init__(self):
        self.valor = "valor en PadreB"
        super().__init__()

class MadreB:
    def __init__(self):
        self.valor = "valor en MadreB"
        super().__init__()

class Hijo3(PadreB, MadreB):
    def __init__(self):
        super().__init__()

print("\n\n---------------- Ejemplo 3 ----------------")
hijo3 = Hijo3()
print(hijo3.valor)