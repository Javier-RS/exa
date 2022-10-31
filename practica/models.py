from app import db 

class Empleado(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    cargo = db.Column(db.String(250))
    salario = db.Column(db.Integer)    

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Cargo: {self.cargo} ,'
                f'Salario: {self.salario}'
        
        )

class Bebida(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    precio = db.Column(db.Integer)    

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Precio: {self.precio}'
        
        )

class Comida(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    precio = db.Column(db.Integer)    

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Precio: {self.precio}'
        
        )

class Mesa(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    tipodemesa = db.Column(db.String(250))
    numeromesa = db.Column(db.Integer)   
    capacidad = db.Column(db.Integer)    

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Tipo : {self.tipodemesa} ,'
                f'Numero: {self.numeromesa},'
                f'Capacidad: {self.capacidad}'
        
        )

class Restaurante(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(250))  
    capacidad = db.Column(db.Integer)    
    gerente = db.Column(db.String(250))
    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Direccion: {self.direccion},'
                f'Capacidad: {self.capacidad},'
                f'Gerente: {self.gerente}'
        
        )
