class Contrato_Persona:
    def __init__(self, idpersona=None, idcontrato=None) -> None:
        self.idp = idpersona
        self.idc = idcontrato
        
        
    def __str__(self) -> str:
        return (f"{self.idp} {self.idc} ")
    @property
    def idPersona(self):
        return self.idp
    
    def idContrato(self):
        return self.idc
    
    if __name__ == '__main__':
        pass