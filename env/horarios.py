"""Es un código sencillo para ejecutar lo pedido"""
# Definir los días de la semana y las horas
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
horas = ["08:00-09:00", "09:00-10:00", "10:00-11:00"]

# Crear un diccionario vacío para almacenar el horario
horario = {dia: {} for dia in dias_semana}

# Solicitar al usuario que ingrese las materias para cada día y hora
for dia in dias_semana:
    print(f"Introduce las materias para {dia}:")
    for hora in horas:
        materia = input(f"  {hora}: ")
        horario[dia][hora] = materia

# Imprimir el horario
for dia, clases in horario.items():
    print(f"{dia}:")
    for hora, materia in clases.items():
        print(f"  {hora}: {materia}")

        