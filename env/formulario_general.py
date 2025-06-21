
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controlador import  search,read_row, insert_row , modify_row, delete_row

class FormularioGeneral():
    def formulario(self):
        try:
            def guardar_datos(): #me estaba dando error UnboundLocalError , HAY QUE PONER EL CODIGO ANTES PARA QUE FUNCIONE
                nombre = text_box_nombre.get().strip()
                hora_inicio = text_box_hora_inicio.get().strip()
                hora_fin = text_box_hora_fin.get().strip()
                dia = text_box_dia.get().strip()
                aula = text_box_aula.get().strip()
                 # Validación de campos vacíos
                if not all([nombre, hora_inicio, hora_fin, dia, aula]):
                    messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
                    return
                try:
                    # Insertar datos en la base de datos
                    insert_row(nombre, hora_inicio, hora_fin, dia, aula)
                    messagebox.showinfo("Éxito", "Datos guardados correctamente")
                    limpiar_campos()
                    actualizar_treeview()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar en la base de datos: {e}")

            def buscar_datos():
                """Busca registros en la base de datos y los muestra en el Treeview."""
                termino = text_box_buscar.get().strip()

                if not termino:
                    messagebox.showwarning("Advertencia", "Ingrese un término de búsqueda")
                    return

                try:
                    resultados = search(termino)  # Llamar a la función de búsqueda en la BD
                    actualizar_treeview1(resultados)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo realizar la búsqueda: {e}")
              
            def eliminar_dato():
                """ Modifica un elemento en la base de datos """
                id = text_box_id.get().strip ()
                nombre = text_box_nombre.get().strip()
                hora_inicio = text_box_hora_inicio.get().strip()
                hora_fin = text_box_hora_fin.get().strip()
                dia = text_box_dia.get().strip()
                aula = text_box_aula.get().strip()

                if not all([ nombre, hora_inicio, hora_fin, dia, aula]):
                    messagebox.showwarning("Advertencia", "No tienes marcado ningún elemento")
                    return

                try:
                    delete_row(id) # Llamar a la función de base de datos
                    messagebox.showinfo("Éxito", "Datos modificados correctamente")
                    limpiar_campos()
                    actualizar_treeview()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo modificar: {e}")     

            def limpiar_campos():
                """Limpiar los campos"""
                text_box_id.config(state="normal")
                text_box_id.delete(0, tk.END)
                text_box_id.config(state="readonly") 
                text_box_nombre.delete(0, tk.END)
                text_box_hora_inicio.delete(0, tk.END)
                text_box_hora_fin.delete(0, tk.END)
                text_box_dia.delete(0, tk.END)
                text_box_aula.delete(0, tk.END)

            def actualizar_treeview():
                """Limpia los datos y actualiza no es necesario un parámetro"""
                for item in tree.get_children():
                    tree.delete(item)
                
                try:
                    datos = read_row()  # Obtener los datos de la base de datos
                    if not datos:
                        messagebox.showwarning("Advertencia", "No hay datos para mostrar")
                    for row in datos:
                        tree.insert("", tk.END, values=row)  # Insertar filas en el Treeview
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo actualizar la vista: {e}")

            def actualizar_treeview1(datos):
                """Limpia y actualiza el Treeview con los datos proporcionados."""
                for item in tree.get_children():
                    tree.delete(item)

                for row in datos:
                    tree.insert("", tk.END, values=row)

                   

            def selecciona_elemento():
                """Función para seleccionar y mostrar los datos de un elemento en los campos correspondientes"""
                select_item = tree.selection()
                #Verificar se se ha seleccionado el objeto
                if not select_item: #el error es que en vez de poner select_item puse la función y por eso daba error
                    messagebox.showwarning("Advertencia", "Seleccione un elemento")
                    return
                item = tree.item(select_item [0],"values") #DA ERROR MIRAR MAÑANA  indexError: tuple index out of range
                if not item:  # Verificar que el elemento tiene datos
                    messagebox.showwarning("Advertencia", "El elemento seleccionado no tiene datos.")
                    return
                
                
                
                text_box_id.config(state="normal")  # Habilitar ID para edición temporalmente
                text_box_id.delete(0, tk.END)
                text_box_id.insert(0, item[0])
                text_box_id.config(state="readonly")  # Bloquear nuevamente el ID

                text_box_nombre.delete(0, tk.END)
                text_box_nombre.insert(0, item[1])

                text_box_hora_inicio.delete(0, tk.END)
                text_box_hora_inicio.insert(0, item[2])

                text_box_hora_fin.delete(0, tk.END)
                text_box_hora_fin.insert(0, item[3])

                text_box_dia.delete(0, tk.END)
                text_box_dia.insert(0, item[4])

                text_box_aula.delete(0, tk.END)
                text_box_aula.insert(0, item[5])

            def modificar_datos():
                """ Modifica un elemento en la base de datos """
                id = text_box_id.get().strip ()
                nombre = text_box_nombre.get().strip()
                hora_inicio = text_box_hora_inicio.get().strip()
                hora_fin = text_box_hora_fin.get().strip()
                dia = text_box_dia.get().strip()
                aula = text_box_aula.get().strip()

                if not all([ nombre, hora_inicio, hora_fin, dia, aula]):
                    messagebox.showwarning("Advertencia", "No tienes seleccionado un elemento")
                    return

                try:
                    modify_row(id,nombre, hora_inicio, hora_fin, dia, aula) # Llamar a la función de base de datos
                    messagebox.showinfo("Éxito", "Datos modificados correctamente")
                    limpiar_campos()
                    actualizar_treeview()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo modificar: {e}")    

            base = tk.Tk()
            ancho_ventana= 1280
            alto_ventana = 740
            # base.geometry ("1280x720")
            #obtener ancho de la pantalla
            ancho_pantalla = base.winfo_screenwidth()
            alto_pantalla = base.winfo_screenheight()
            #calcular la posición del punto de inicio para centrar la ventana 
            posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
            posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)
            base.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")  #para que funcione geometry no tiene que haber espacios en blanco
            base.title("Formulario general")

            # Crear un frame para el formulario
            group_box = tk.LabelFrame(base, text="ACCIONES",padx=5, pady=5)  #creamos un panel que llevará otros contenedor de controles
            group_box.grid(row=0, column=1, padx=10, pady=10) #grid posicionamiento 

            label_id = tk.Label (group_box,text="Id:", width=13,font=("arial",13)).grid(row=0,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_id = tk.Entry(group_box, state="readonly") #creo el segundo control con Entry indico el panel y el estado
            text_box_id.grid (row=0,column=1)

            label_nombre = tk.Label (group_box,text="Nombre:", width=13,font=("arial",13)).grid(row=1,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_nombre = tk.Entry(group_box) #creo el segundo control con Entry indico el panel y el estado
            text_box_nombre.focus() #para que el cursor se posicione en el control
            text_box_nombre.grid (row=1,column=1)
            
            label_hora_inicio = tk.Label (group_box,text="Hora Inicio:", width=13,font=("arial",13)).grid(row=2,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_hora_inicio = tk.Entry(group_box) #creo el segundo control con Entry indico el panel y el estado
            text_box_hora_inicio.grid (row=2,column=1)

            label_hora_fin = tk.Label (group_box,text="Hora fin:", width=13,font=("arial",13)).grid(row=3,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_hora_fin = tk.Entry(group_box) #creo el segundo control con Entry indico el panel y el estado
            text_box_hora_fin.grid (row=3,column=1)

            label_dia = tk.Label (group_box,text="Día:", width=13,font=("arial",13)).grid(row=4,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_dia = tk.Entry(group_box) #creo el segundo control con Entry indico el panel y el estado
            text_box_dia.grid (row=4,column=1)

            label_aula = tk.Label (group_box,text="Aula:", width=13,font=("arial",13)).grid(row=5,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_aula = tk.Entry(group_box) #creo el segundo control con Entry indico el panel y el estado
            text_box_aula.grid (row=5,column=1)

            group_box1 = tk.LabelFrame(base, text="ACCIONES",padx=5, pady=5)  #creamos un panel que llevará otros contenedor de controles
            group_box1.grid(row=5, column=1, padx=10, pady=10, columnspan=3) #grid posicionamiento 


            tk.Button (group_box1, text="Guardar", width=20,fg="white", bg="green", command=guardar_datos).grid(row=1, column=0)
            tk.Button (group_box1, text="Modificar", width=20, fg="white", bg="green", command=modificar_datos).grid(row=2, column=0)
            tk.Button (group_box1, text="Selecionar", width=20, fg="white", bg="green", command=selecciona_elemento).grid(row=3, column=0)
            tk.Button (group_box1, text="Eliminar", width=20, fg="white", bg="green", command= eliminar_dato).grid(row=4, column=0)
            tk.Button (group_box1, text="Borrar", width=20,fg="white", bg="green", command=limpiar_campos).grid(row=5, column=0)  

            
            #crear un treeview configurar columnas lo creamos y donde lo vamos a poner
            group_box2 = tk.LabelFrame(base, text="ACCIONES",padx=5, pady=5)  #creamos un panel que llevará otros contenedor de controles
            group_box2.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10, width=950, height=400) # Esquina superior derecha


            tree = ttk.Treeview(group_box2, columns=("Id", "nombre","hora_inicio", "hora_fin", "dia","aula"),
                                show="headings", height=5)  #creamos el treeview
            
            # Configurar las columnas del treeview
            for col in tree['columns']:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", minwidth=0, width=150, stretch=tk.NO) #configuramos las columnas
                            # Insertar los datos obtenidos de la base de datos en el treeview
            read_rows1 = read_row()
            for row in read_rows1:
                tree.insert("", tk.END, values=row)
            
            tree.pack(padx=10, pady=10, fill= "both", expand=True) #empaquetamos el treeview

            # Crear Scrollbar vertical 
            scroll_y = ttk.Scrollbar(group_box2, orient="vertical", command=tree.xview) 
            tree.configure(xscrollcommand=scroll_y.set)
            # Empacar el Treeview y el Scrollbar 
            tree.pack(side="left", fill="both", expand=True) 
            scroll_y.pack(side="right", fill="x")


            tree.pack()  #para que se pueda cerrar
            
            group_box3 = tk.LabelFrame(base, text="ACCIONES",padx=5, pady=5)  #creamos un panel que llevará otros contenedor de controles
            group_box3.place(relx=1.0, rely=0.7, anchor="ne",x=-10, y=10, width=950, height=100) #grid posicionamiento 
            label_buscar = tk.Label (group_box3,text="Buscar por nombre o aula:", width=25,font=("arial",13)).grid(row=0,column=0) #creo el primer control con Label indico el panel el texto largura tipo de letra 
            text_box_buscar = tk.Entry(group_box3) #creo el segundo control con Entry indico el panel y el estado
            text_box_buscar.grid(row=0,column=1, ipadx=270, padx=5, pady=5)
            tk.Button(group_box3, text="Buscar",width=20,fg="white", bg="green", command=buscar_datos).grid(row=1,column=0)
            tk.Button(group_box3, text="Volver",width=20,fg="white", bg="green", command=actualizar_treeview).grid(row=1,column=1)
            

            base.mainloop() #para que se pueda cerrar

       
        except ValueError as e:
            messagebox.showerror('Error', e)    


if __name__ == "__main__":
    formulario = FormularioGeneral()
    formulario.formulario ()          