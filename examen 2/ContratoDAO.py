from cursorDelPool import CursorDelPool
from Contrato import Contrato
from conexion import Conexion
from logger_base import log

class ContratoDAO:
    _SELECCIONAR = "SELECT * FROM contrato"
    _INSERT = "INSERT INTO contrato(id,nocontrato,costo,fechainic,fechafin) VALUES (%s,%s,%s,%s,%s)"
    _ACTUALIZAR ="UPDATE contrato SET nocontrato=%s, costo=%s, fechainic=%s, fechafin=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM contrato WHERE id=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:            
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato)
            return contratos
            
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.id, contrato.nocontrato, contrato.costo, contrato.fechainic, contrato.fechafin)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.nocontrato, contrato.costo, contrato.fechainic, contrato.fechafin, contrato.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
                                    
if __name__ == '__main__':

    #select
    contratos = ContratoDAO.seleccionar()
    for p in contratos:
        log.debug(p)

    #insertar
    contrato1 = Contrato(id=4,nocontrato=1238,costo=5000,fechainic="31/10/22",fechafin="02/11/22")
    contratosInsertadas = ContratoDAO.insertar(contrato1)
    log.debug(f"Contratos insertados {contratosInsertadas}")

    #actualizar
    contrato1 = Contrato(id=4,nocontrato=1212,costo=5500,fechainic="31/10/22",fechafin="02/11/22")
    contratosActualizadas = ContratoDAO.actualizar(contrato1)
    log.debug(f"Contratos actulizados {contratosActualizadas}")

    #eliminar
    contrato1 = Contrato(id=4)
    contratoEliminada = ContratoDAO.eliminar(contrato1)
    log.debug(f"Contrato eliminados {contratoEliminada}")