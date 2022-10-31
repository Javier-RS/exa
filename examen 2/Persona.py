class Persona:
    def __init__(self, id=None, nombre=None, edad=None, correo=None) -> None:
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        
    def __str__(self) -> str:
        return (f"{self.id} {self.nombre} {self.edad} {self.correo} ")
    @property
    def idPersona(self):
        return self.id
    
    def nombre(self):
        return self.nombre
    
    def edad(self):
        return self.edad
    
    def correo(self):
        return self.correo
    
    if __name__ == '__main__':
        pass