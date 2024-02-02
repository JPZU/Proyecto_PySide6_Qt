import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase,QSqlQuery



conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

# conexion = QSqlDatabase.addDatabase("QMYSQL")
# conexion.setDatabaseName(absPath("Contactos.db"))

# print(conexion.databaseName(),conexion.connectionName())
if not conexion.open():
    print("No se puede conectar a la base de datos", conexion.lastError().text())
    sys.exit(True)
else: 
    print("Conexion abierta", conexion.isOpen())



consulta = QSqlQuery()
# Borrar la tabla 
consulta.exec("DROP TABLE IF EXISTS contactos")
# Crear la tabla
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )""")

# print(conexion.tables())

nombre, empleo, email  = "Juan", "Instructor", "juan@gamil.com"

consulta.exec(f"""
    INSERT INTO contactos (nombre, empleo, email)
    VALUES ('{nombre}','{empleo}','{email}')
             """)

contactos = [("Andres 1","Astronomo 1","andres@astronomo1"),
             ("Andres 2","Astronomo 2","andres@astronomo2"),
             ("Andres 3","Astronomo 3","andres@astronomo3"),
             ("Andres 4","Astronomo 4","andres@astronomo4")]

consulta.prepare("INSERT INTO contactos (nombre, empleo, email) VALUES (?,?,?)")

for nombre, empleo, email in contactos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(email)
    consulta.exec()
    
consulta.exec("SELECT nombre, empleo, email FROM contactos")

# if consulta.first():
#     print(consulta.value("nombre"),
#           consulta.value("empleo"),
#           consulta.value("email"))

while consulta.next():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))    
    
conexion.close()
print("Conexion cerrada", not conexion.isOpen())