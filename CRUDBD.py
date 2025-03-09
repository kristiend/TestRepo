import os
import time
import mysql.connector
#crearemos la conexion a la base de datos
mybd=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='tienda'
)
#craremos un objeto para ejecutar comandos en la BD (llamado cursor)
mycursor=mybd.cursor()
#crearemos un menu que verá el usuario (nuestro pequeño front end)
while True:
   print('---MENU DEL SISTEMA---'
          '\n1. Insertar un producto'
          '\n2. Eliminar un producto'
          '\n3. Buscar un producto'
          '\n4. Actualizar un producto'
          '\n5. Mostrar la lista de productos'
          '\n6. Salir del sistema')
   opc = int(input('Elige una opcion:\n'))
   if(opc==1): #Create Creamos el producto
    clave = input("Ingrese la clave del producto : ")
    nombre = input("Ingrese el nombre del producto : ")
    precio = float(input("Ingrese el precio del producto : "))
    #Creamos la instruccion para insertar
    sql = "Insert into productos (clave, nombre, precio) values (%s,%s,%s)"
    #crearemos la tupla para insertar
    val=(clave,nombre,precio)
    #preparamos para insertar
    mycursor.execute(sql,val)
    #insertamos
    mybd.commit()
    #avisamos al usuario
    print('Producto agregado al sistema')
    time.sleep(2)
    os.system('cls')# si usas mac o linux pon clear entre comillas
   elif(opc==2):#Delete
     clave = input("Ingrese la clave del producto a eliminar : ")
     #Creamos la instruccion para eliminar
     sql = "delete from productos where clave = %s"
     #crearemos la tupla
     val=(clave,)
     #preparamos la instrucción para eliminar
     mycursor.execute(sql,val)
     #realizamos los cambios
     mybd.commit()
     #avisamos al usuario
     print(mycursor.rowcount,'Producto eliminados')
     time.sleep(2)
     os.system('cls')# si usas mac o linux pon clear entre comillas
   elif (opc==3):# Read (leer un registro de la tabla o buscar un producto)
     clave=input('Escribe la clave del producto a buscar: ')
     #Creamos la instruccion para consultar
     sql='SELECT * FROM productos WHERE clave=%s'
     #creamos la tupla
     val=(clave,)
     #preparamos la instrucción
     mycursor.execute(sql,val)
     #verificaremos si existe el producto
     myresult=mycursor.fetchall()
     if myresult:
       print('El producto está en el sistema')
     else:
       print('Producto agotado, no hay existencias')
     time.sleep(2)
     os.system('cls')
   elif opc==4:# Update (actualizar/modificar el producto)
    clave=input('Escribe la clave del producto a modificar: ')
    nombre=input('Escribe el nombre correcto del producto: ')
    precio=float(input('Escribe el precio correcto del producto: '))
    #crearemos la consulta de actualización
    sql='UPDATE productos SET nombre=%s, precio=%s WHERE clave=%s'
    #creamos la tupla con los nuevos datos
    val=(nombre,precio,clave)
    #preparamos para la ejecución
    mycursor.execute(sql,val)
    #se realiza la modificación
    mybd.commit()
    #avisamos al usuario
    print('El producto se ha modificado correctamente')
    time.sleep(2)
    os.system('cls')
   elif opc==5: #Read (Consulta general o listado de productos)
    #crearemos la consulta general a la tabla de productos
    mycursor.execute('SELECT * FROM productos')
    myresult=mycursor.fetchall()
    #mostraremos el contenido de la tabla
    print('Lista de productos:')
    #inicia el ciclo para recorrer la tabla
    for x in myresult:
        #imprimiremos cada fila o registro de la tabla
        print(x)
        time.sleep(3)
        os.system('cls')
   elif opc==6:#Salir del sistema
    respuesta=input('Estás seguro? (s/n) ')
    if respuesta.upper()=='S':
        print('Saliendo del sistema...')
        time.sleep(2)
        os.system('cls')
        break
    time.sleep(2)#en caso que la respuesta no sea S
    os.system('cls')
   else:
    print('Opción no válida, intenta de nuevo...')
    time.sleep(2)
    os.system('cls')
mybd.close()    



