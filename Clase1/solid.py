# Single Responsability

# Mala práctica
class Factura:
    def calculaTotal(self) -> int:
        return 10
    
    def guardaEnBBDD(self) -> None:
        #Guardado en BBDD
        print("Guardado")

    def muestraFacutra(self) -> None:
        print("Total: 10")

# Solución
class CalculadoraFactura:
    def calculaTotal(self) -> int:
        return 10

class RepositorioFactura:    
    def guardaEnBBDD(self) -> None:
        #Guardado en BBDD
        print("Guardado")

class RepresentacionFactura:
    def muestraFacutra(self) -> None:
        print("Total: 10")

# Open/Closed (abiertas a extensión pero cerradas a modificación)
# Mala práctica
class CalculadoraDescuentos:
    def calcula(self, tipo_cliente: str, precio: float) -> float:
        if tipo_cliente == "normal":
            return precio * 0.95
        elif tipo_cliente == "VIP":
            return precio * 0.8
        elif tipo_cliente == "empleado":
            return precio * 0.7
        return precio
    
# Solución
from abc import ABC, abstractmethod
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio: float) -> float:
        pass

class DescuentoNormal(Descuento):
    def aplicar(self, precio: float) -> float:
        return precio * 0.95
    
class DescuentoVIP(Descuento):
    def aplicar(self, precio: float) -> float:
        return precio * 0.8
    
class DescuentoEmpleado(Descuento):
    def aplicar(self, precio: float) -> float:
        return precio * 0.7
    
class CalculadoraDescuento:
    def calcular(self, descuento: Descuento, precio: float) -> float:
        return descuento.aplicar(precio)