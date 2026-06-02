# MRO = Method Resolution Order

# Ejemplo sin constructor clase heredada
class PadreA:
    def __init__(self):
        print("Constructor de PadreA")

class MadreA:
    def __init__(self):
        print("Constructor de MadreA")

class Hijo1(PadreA, MadreA):
    pass

print("\n\n---------------- Ejemplo 1 ----------------")
hijo1 = Hijo1()

print(Hijo1.__mro__)






# Ejemplo con constructor la clase heredada
class Hijo2(PadreA, MadreA):
    def __init__(self):
        print("Constructor Hijo2")

print("\n\n---------------- Ejemplo 2 ----------------")
hijo2 = Hijo2()





# Ejemplo con llamada a los constructores (rompe MRO, desaconsejado para diamante)
class Hijo3(PadreA, MadreA):
    def __init__(self):
        PadreA.__init__(self)
        MadreA.__init__(self)
        print("Constructor Hijo3")

print("\n\n---------------- Ejemplo 3 ----------------")
hijo3 = Hijo3()





# Ejemplo con llamada a los constructores con super
class PadreB:
    def __init__(self):
        print("Constructor de PadreB")
        super().__init__()
        print("Construído PadreB")

class MadreB:
    def __init__(self):
        print("Constructor de MadreB")
        super().__init__()
        print("Construído MadreB")

class Hijo4(PadreB, MadreB):
    def __init__(self):
        print("Constructor de Hijo4")
        super().__init__()
        print("Construído Hijo4")

print("\n\n---------------- Ejemplo 4 ----------------")
print(Hijo4.__mro__)
hijo4 = Hijo4()





# Ejemplo de constructores con argumentos (usar **kwargs como buena práctica)
class PadreC:
    def __init__(self, e, **kwargs):
        print(f"PadreC recibe {e}")
        super().__init__(**kwargs)

class MadreC:
    def __init__(self, f, **kwargs):
        print(f"MadreC recibe {f}")
        super().__init__(**kwargs)

class Hijo5(PadreC, MadreC):
    def __init__(self, e, f, g):
        print(f"Hijo5 recibe {g}")
        super().__init__(e = e, f = f)

print("\n\n---------------- Ejemplo 5 ----------------")
hijo5 = Hijo5(1, 2, 3)





#Ejemplo del diamante
class Abuelo:
    def __init__(self):
        print("Abuelo")

class PadreD(Abuelo):
    def __init__(self):
        print("Constructor de PadreD")
        super().__init__()

class MadreD(Abuelo):
    def __init__(self):
        print("Constructor de MadreD")
        super().__init__()

class Hijo6(PadreD, MadreD):
    def __init__(self):
        print("Constructor de Hijo6")
        super().__init__()

print("\n\n---------------- Ejemplo 6 ----------------")
print(Hijo6.__mro__)
hijo6 = Hijo6()