import psycopg2 

conexion=psycopg2.connect(user='postgres',
                        password='admin',
                        host='localhost',
                        port='5432',
                        database='db_examen')   

cursor=conexion.cursor()

sql='INSERT INTO contrato(id, nocontrato, costo,fechainic,fechafin) VALUES(%s,%s,%s,%s,%s)'

id=input('ingrese id ')
nocontrato=input('ingrese numero de contrato ')
costo=input('Ingrese costo ')
fechainic=input('Ingrese fecha de inicio ')
fechafin=input('Ingrese fecha fin ')

datos=(id, nocontrato, costo, fechainic, fechafin)
cursor.execute(sql,datos)
conexion.commit()
registros=cursor.rowcount

print(f'registro insertado {registros}')
cursor.close()
conexion.close()