from cursorDelPool import CursorDelPool
from Contrato_Persona import Contrato_Persona
from conexion import Conexion
from logger_base import log

class ContratoPersonaDAO:
    _SELECCIONAR = "SELECT * FROM contrato_persona"
    _INSERT = "INSERT INTO contrato_persona(idpersona,idcontrato) VALUES (%s,%s)"

    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:            
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato_Persona(r[0],r[1])
                contratos.append(contrato)
            return contratos
            
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.idp, contrato.idc)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
                                    
if __name__ == '__main__':

    #select
    """contratos = ContratoPersonaDAO.seleccionar()
    for p in contratos:
        log.debug(p)"""

    #insertar
    contrato1 = Contrato_Persona(idcontrato=4,idpersona=1)
    contratosInsertadas = ContratoPersonaDAO.insertar(contrato1)
    log.debug(f"Contratos personas insertados {contratosInsertadas}")
