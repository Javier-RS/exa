class Contrato:
    def __init__(self, id=None, nocontrato=None, costo=None, fechainic=None, fechafin=None) -> None:
        self.id = id
        self.nocontrato = nocontrato
        self.costo = costo
        self.fechainic = fechainic
        self.fechafin = fechafin
        
    def __str__(self) -> str:
        return (f"{self.id} {self.nocontrato} {self.costo} {self.fechainic} {self.fechafin} ")
    @property
    def idContrato(self):
        return self.id
    
    def nocontrato(self):
        return self.nocontrato
    
    def costo(self):
        return self.costo
    
    def fechainic(self):
        return self.fechainic
    
    if __name__ == '__main__':
        pass