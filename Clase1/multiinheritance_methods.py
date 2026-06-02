# Ejemplo de método con el mismo nombre
class PadreA:
    def saludar(self):
        print("Hola desde PadreA")

class MadreA:
    def saludar(self):
        print("Hola desde MadreA")

class Hijo1(PadreA, MadreA):
    pass

print("\n\n---------------- Ejemplo 1 ----------------")
hijo1 = Hijo1()
hijo1.saludar()
print(Hijo1.__mro__)





# Método redefinido en la clase hija
class Hijo2(PadreA, MadreA):
    def saludar(self):
        print("Hola desde Hijo2")
print("\n\n---------------- Ejemplo 2 ----------------")
hijo2 = Hijo2()
hijo2.saludar()






# Llamar a saludar del padre
class PadreB:
    def saludar(self):
        print("Hola desde PadreB")
        super().saludar() # type: ignore

class MadreB:
    def saludar(self):
        print("Hola desde MadreB")

class Hijo3(PadreB, MadreB):
    def saludar(self):
        print("Hola desde Hijo3")
        super().saludar()
print("\n\n---------------- Ejemplo 3 ----------------")
hijo3 = Hijo3()
hijo3.saludar()