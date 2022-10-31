import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_examen')   

cursor=conexion.cursor()
sql='DELETE FROM contrato WHERE id=%s'

id=input('Ingrese el id ')

cursor.execute(sql,id)
conexion.commit()
registro_eliminado=cursor.rowcount

print(f'registro eliminado {registro_eliminado}')

cursor.close()
conexion.close()