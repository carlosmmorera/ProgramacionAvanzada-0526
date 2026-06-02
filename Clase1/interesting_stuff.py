# Tipado débil
x: int = 0
print(x)
x = "Hola" # type: ignore
print(x)

# Fallos de "compilación"

numero = 0
print(numero)
#numero.strip()


class Ejemplo:
    def __init__(self, c = None):
        self.a = 1
        self.b = "Hola"
        self.c = [] if c is None else c

    def __eq__(self, value: Ejemplo) -> bool:
        return self.a == value.a

    def __repr__(self) -> str:
        return f"a = {self.a}"

ej1 = Ejemplo()
ej1.c.append(5)
ej2 = Ejemplo()
print(ej1.c)
print(ej2.c)

print(id(ej2))

muestra = print
muestra(25)