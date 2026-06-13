class Padre:
    def __init__(self, x) -> None:
        self.atributo = x

    def saludar(self):
        print("Hola desde Padre")

    @staticmethod
    def saludo_estatico(): #Name mangling
        print("Hola estáticamente")

Padre.saludo_estatico()

class Hijo(Padre):
    def __init__(self) -> None:
        Padre.__init__(self, 3)
        print(self.atributo)

hijo = Hijo()

import requests
import asyncio
# Singleton en Python
class Singleton:
    _instancia = None
    _lock = None

    def __init__(self, x) -> None:
        self.atributo = x

    @classmethod
    async def create(cls):
        if cls._lock is None:
            cls._lock = asyncio.Lock()

        if cls._instancia is None:
            async with cls._lock:
                if cls._instancia is None:
                    cls._instancia = cls(3)

        return cls._instancia
    
async def get_class() -> Singleton:
    return await Singleton.create()

#Métodos de singleton síncronos
# Usando decoradores

#Alternativa 1
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass(BaseClass):
    pass

# Alternativa 2

def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w,
                                    class_).__new__(class_,
                                                    *args,
                                                    **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class MyClass(BaseClass):
    pass



# Usando herencia múltiple

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(Singleton, BaseClass):
    pass

# Usando el atributo metaclase

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(BaseClass, metaclass=Singleton):
    pass
