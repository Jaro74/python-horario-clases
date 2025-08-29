# 🗓️ Proyecto de Gestión de Horarios con Tkinter y SQLite

## 📌 Descripción
Aplicación de escritorio desarrollada en **Python** que permite gestionar horarios de clases. Utiliza **Tkinter** para la interfaz gráfica y **SQLite** como sistema de almacenamiento de datos.

## ✨ Características
- Interfaz gráfica intuitiva con Tkinter.
- Base de datos SQLite para guardar los horarios.
- Funcionalidades CRUD: Crear, Leer, Actualizar y Eliminar registros.
- Búsqueda y filtrado por distintos criterios.
- Ordenación de datos por campos seleccionables.

## ⚙️ Instalación

### 1. Requisitos
- Python 3 instalado.
- Se recomienda crear un entorno virtual:
- bash
python -m venv env
# En Windows:
.\env\Scripts\activate
  
## 🗃️ Uso de la base de datos SQLite

El proyecto utiliza **SQLite** para almacenar los horarios de clases en una base de datos llamada `clase_horario.db`.

### 🔧 Funciones principales de la base de datos

| Función | Descripción |
|--------|-------------|
| `createDB()` | Crea la base de datos si no existe |
| `createTable()` | Crea la tabla `clase_horaria` si no existe |
| `insert_row(nombre, hora_inicio, hora_fin, dia, aula)` | Inserta un nuevo horario de clase |
| `read_row()` | Lee y devuelve todos los registros de la tabla |
| `read_rows()` | Muestra todos los registros de la tabla en consola |
| `insert_rows(lista_de_horarios)` | Inserta múltiples registros de clase |
| `read_ordered(campo)` | Obtiene registros ordenados por el campo especificado |
| `search(termino)` | Busca registros por nombre o aula |
| `modify_row(id, nombre, hora_inicio, hora_fin, dia, aula)` | Modifica un registro existente |
| `update_fields(campo, nuevo_valor, criterio, valor_criterio)` | Modifica registros que coincidan con el criterio |
| `delete_row(id_registro)` | Elimina un registro por su ID |
| `delete_row_2p(campo, valor)` | Elimina registros según un criterio |

---

## 🖥️ Interfaz gráfica con Tkinter

La interfaz gráfica permite al usuario:

- Agregar nuevos horarios.
- Visualizar la lista de horarios almacenados en la base de datos.
- Editar o eliminar horarios existentes.
- Realizar búsquedas filtradas por nombre o aula.

---

## 👤 Autor

Desarrollado por **Emilio Iniesta**.







