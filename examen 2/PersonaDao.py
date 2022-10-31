from cursorDelPool import CursorDelPool
from Persona import Persona
from conexion import Conexion
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona"
    _INSERT = "INSERT INTO persona(id,nombre,edad,correo) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR ="UPDATE persona SET nombre=%s, edad=%s, correo=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:            
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
            
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id, persona.nombre, persona.edad, persona.correo)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad, persona.correo, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
                                    
if __name__ == '__main__':

    #select
    personas = PersonaDAO.seleccionar()
    for p in personas:
        log.debug(p)

    #insertar
    persona1 = Persona(id=5,nombre = "Pancho", edad = 20, correo ="pancho@gmail.com")
    personasInsertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas {personasInsertadas}")

    #actualizar
    persona1 = Persona(id=4,nombre = "Lili", edad = 20, correo ="Lili@gmail.com")
    personasActualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actulizadas {personasActualizadas}")

    #eliminar
    persona1 = Persona(id=5)
    personaEliminada = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas {personaEliminada}")

