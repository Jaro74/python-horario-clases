import sqlite3 as sql #importo modulo sqlite con alias 
import unicodedata #importo para manejar datos Unicode, al final no lo implemento,
# Crear base de datos
def createDB():
    """Función para crear la base de datos"""
    conn = sql.connect("clase_horario.db")
    # con commit se guardan los cambios
    conn.commit()
    # cerrar la conexión
    conn.close()

def createTable():
    """Función para crear la tabal en la base de datos"""
    conn = sql.connect("clase_horario.db")
    #cursor es un objeto que permite ejecutar instrucciones SQL
    cursor = conn.cursor()
    # Crear tabla
    cursor.execute("""CREATE TABLE IF NOT EXISTS clase_horaria (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nombre TEXT NOT NULL, hora_inicio TEXT NOT NULL, hora_fin TEXT NOT NULL, 
                   dia TEXT NOT NULL, aula TEXT NOT NULL)""")
    conn.commit()
    conn.close()

def insert_row(nombre, hora_inicio, hora_fin, dia, aula):
    """Función para insertar un nuevo registro en la tabla clase_horaria."""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    # Insertar datos
    cursor.execute("""
        INSERT INTO clase_horaria (nombre, hora_inicio, hora_fin, dia, aula) 
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, hora_inicio, hora_fin, dia, aula))
    conn.commit()
    conn.close()

def read_row():
    """Funcion para consulta y leer datos enn tkinter"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    
    try:
        # Realizar la consulta para obtener los datos
        cursor.execute("SELECT id, nombre, hora_inicio, hora_fin, dia, aula FROM clase_horaria")
        rows = cursor.fetchall()
    except sql.Error as e:
        print(f"Error al leer los datos: {e}")
        rows = []  # En caso de error, devolver una lista vacía
    finally:
        conn.close()
        return rows
    
    
def read_rows():
    """Funcion para consulta y leer datos es para terminal"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    # Leer datos
    instruccion = "SELECT * FROM clase_horaria"
    cursor.execute(instruccion)
    # fetchall() obtiene todos los registros
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    print(rows)

def insert_rows(clase_horaria_list):
    """Función para insertar un nuevo registro en la tabla clase_horaria. Para terminal que se puedan meter mas datos de una vez"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    #Insertar datos executemany() para insertar varias filas se pasa como parametro la instruccion y la lista de tuplas
    #para cada fila se inserta una tupla ? es un placeholder
    cursor.executemany("""
        INSERT INTO clase_horaria (nombre, hora_inicio, hora_fin, dia, aula) 
        VALUES (?, ?, ?, ?, ?)  
    """, (clase_horaria_list))
    conn.commit()
    conn.close()

def read_ordered (field):    
    """Función para leer registros ordenados por un campo especifico en orden desc para terminal"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    # Leer datos
    instruccion = "SELECT * FROM clase_horaria ORDER BY ? DESC"
    cursor.execute(instruccion, (field,))
    
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    print(rows)

def search(parameter, field):
    """Función de búsqueda en la base datos en terminal y prueba para ver si con el mismo nombre con fiel diferente no daba error"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM clase_horaria WHERE {parameter} LIKE ?" # parametro es para buscar por campo y field es para buscar por valor LIKE es para buscar por coincidencia
    cursor.execute(instruccion, (f"%{field}%",))
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    print(rows)

#Es una función para quitar acentos en las búsquedas pero no me queda claro como implementarla
def eliminar_acentos(texto):
    """Elimina los acentos de una cadena de texto."""
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def search(termino):
    """Busca registros en la base de datos donde el nombre o aula contenga el término."""
    # termino = eliminar_acentos(termino).lower  para implementar la función y quitar mayusculas, no funciona o no encuentro la manera de implementarlo
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id, nombre, hora_inicio, hora_fin, dia, aula 
            FROM clase_horaria 
            WHERE nombre LIKE ?  OR aula LIKE ? 
        """, ('%' + termino + '%', '%' + termino + '%'))

        resultados = cursor.fetchall()
    except sql.Error as e:
        print(f"Error al buscar datos: {e}")
        resultados = []
    finally:
        conn.close()
        return resultados    

def modify_row( id,nombre, hora_inicio, hora_fin, dia, aula):
    """Función para modificar un registro existente en la tabla clase_horaria"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    #Actualizar los datos del registro con id especifico
    cursor.execute("""
        UPDATE clase_horaria 
        SET nombre = ?, hora_inicio = ?, hora_fin = ?, dia = ?, aula = ? 
        WHERE id = ?
    """, (nombre, hora_inicio, hora_fin, dia, aula, id))

    conn.commit()
    conn.close()    

def update_fields(parameter, field, parameter2, field2):
    """Función para actualizar"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE clase_horaria SET {parameter} = ? WHERE {parameter2} LIKE ?"
    cursor.execute(instruccion, (field, f"%{field2}%"))
    conn.commit()
    conn.close()
    
def delete_row_2p(parameter, field):
    """Función para borrar, para terminarl no para tkinter"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM clase_horaria WHERE {parameter} = ?"
    cursor.execute(instruccion, (field,))
    conn.commit()
    conn.close()

def delete_row (id_registro):
    """Función para borrar"""
    conn = sql.connect("clase_horario.db")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clase_horaria WHERE id = ?", (id_registro))
        conn.commit()
        print(f"Registro con ID {id_registro} eliminado.")
    except sql.Error as e:
        print(f"Error al eliminar el registro: {e}") 
    finally:
        conn.close()      

    
"""Comento todo ya que eran las pruebas para ver si funcionaba"""
# if __name__ == "__main__":
#     # createDB()
#     # createTable()
#     # insert_row("Matemáticas", "08:00", "09:00", "Lunes", "Aula 101")
#     read_rows()
#     #clase_horaria_list = [("Matemáticas", "08:00", "09:00", "Lunes", "Aula 101"), ("Física", "09:00", "10:00", "Lunes", "Aula 102"), ("Química", "10:00", "11:00", "Lunes", "Aula 103")]
#     #insert_rows(clase_horaria_list)
#     #read_ordered("nombre")
#     #search("nombre", "Matemáticas")
#     # update_fields("nombre", "Física", "nombre", "Matemáticas")
#     #delete_row("nombre", "Física")
