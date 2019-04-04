import sqlite3


def introducirCategoria():

    nombreCategoria = [raw_input("introduce el nombre de la categoria: ")]

    x=0
    while x==0:

        if nombreCategoria.__contains__("Facil") or nombreCategoria.__contains__("Intermedio") or nombreCategoria.__contains__("Avanzado"):
            miCursor.execute("INSERT INTO CATEGORIAS(NOMBRE) VALUES (?)",(nombreCategoria))
            conexion.commit()
            x=1
        else:
            print("nombre de categoria incorrecto")
            nombreCategoria = [raw_input("introduce el nombre de la categoria: ")]


def introducirCurso():

    nombreCurso=raw_input("Escribe el nombre del curso: ")
    categoria=raw_input("escribe la categoria del curso: ")

    x=0
    while x==0:
        if categoria=="Facil":
            categoria=1
            x=1
        elif categoria=="Intermedio":
            categoria=2
            x=1
        elif categoria=="Avanzado":
            categoria=3
            x=1
        else:
            print("categoria erronea")
            categoria = raw_input("escribe la categoria del curso: ")



    miCursor.execute("INSERT INTO CURSOS(NOMBRE, CATEGORIA_ID) VALUES (?,?)", (nombreCurso, categoria))
    conexion.commit()



def listaCursos():
    categoria=['Intermedio']



    consulta = miCursor.execute("SELECT CURSOS.NOMBRE, CATEGORIAS.NOMBRE FROM CURSOS, CATEGORIAS WHERE "
                                "(CURSOS.CATEGORIA_ID=CATEGORIAS.ID AND CATEGORIAS.NOMBRE = ? )", (categoria))

    lista=list(consulta)


    print lista






conexion=sqlite3.connect("bbdd_antoniocs88")

miCursor=conexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS CATEGORIAS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(100) UNIQUE NOT NULL)")
miCursor.execute("CREATE TABLE IF NOT EXISTS CURSOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(100) UNIQUE NOT NULL, CATEGORIA_ID INTEGER NOT NULL, FOREIGN KEY(CATEGORIA_ID) REFERENCES CATEGORIA(ID))")


listaCursos()
#introducirCurso()

#introducirCategoria()














conexion.close()