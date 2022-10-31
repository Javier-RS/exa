import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_examen')   

cursor=conexion.cursor()
sql='UPDATE contrato SET nocontrato=%s, costo=%s, fechainic=%s, fechafin=%s WHERE id=%s'

id=input('Ingrese el id a editar ')
nocontrato=input('Ingrese el numero de contrato ')
costo=input('Ingrese el costo ')
fechainic=input('Ingrese la fecha inicial ')
fechafin=input('Ingrese la fecha fin ')

datos=(nocontrato,costo,fechainic,fechafin,id)
cursor.execute(sql,datos)
conexion.commit()
registro_actualizado=cursor.rowcount

print(f'registro actualizado {registro_actualizado}')

cursor.close()
conexion.close()