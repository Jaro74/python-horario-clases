Proyecto de Gestión de Horarios con Tkinter y SQLite

Descripción:
Este proyecto es una aplicación de escritorio desarrollada en Python que permite gestionar horarios de clases utilizando la biblioteca Tkinter para la interfaz gráfica y SQLite como base de datos para almacenar la información.

Características principales:
- Interfaz gráfica con Tkinter para la gestión de horarios.
- Base de datos SQLite para el almacenamiento de horarios de clases.
- Operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los registros de clases.
- Búsqueda y filtrado de registros mediante distintos criterios.
- Ordenación de datos por diferentes campos.

Instalación y ejecución:
1. Requisitos previos:
   Asegúrate de tener instalado Python 3 en tu sistema. Además, es recomendable crear un entorno virtual:
   
   python -m venv env
   En Windows: .\env\Scripts\activate

2. Instalación de dependencias:
   Ejecuta el siguiente comando para instalar las bibliotecas necesarias:
   
   pip install tk sqlite3

3. Ejecución de la aplicación:
   Para ejecutar el programa, usa el siguiente comando:
   
   python formulario_general.py

Uso de la base de datos SQLite:
El proyecto usa SQLite para almacenar los horarios de clases en una base de datos llamada "clase_horario.db".

Funciones principales de la base de datos:
- createDB(): Crea la base de datos si no existe.
- createTable(): Crea la tabla clase_horaria si no existe.
- insert_row(nombre, hora_inicio, hora_fin, dia, aula): Inserta un nuevo horario de clase.
- read_row(): Lee y devuelve todos los registros de la tabla.
- read_rows(): Muestra todos los registros de la tabla en consola.
- insert_rows(lista_de_horarios): Inserta múltiples registros de clase.
- read_ordered(campo): Obtiene registros ordenados por el campo especificado.
- search(termino): Busca registros por nombre o aula.
- modify_row(id, nombre, hora_inicio, hora_fin, dia, aula): Modifica un registro existente.
- update_fields(campo, nuevo_valor, criterio, valor_criterio): Modifica registros que coincidan con el criterio.
- delete_row(id_registro): Elimina un registro por su ID.
- delete_row_2p(campo, valor): Elimina registros según un criterio.

Interfaz gráfica con Tkinter:
La interfaz gráfica permite al usuario:
- Agregar nuevos horarios.
- Visualizar la lista de horarios almacenados en la base de datos.
- Editar o eliminar horarios existentes.
- Realizar búsquedas filtradas por nombre o aula.

Autor:
Desarrollado por Emilio Iniesta.
