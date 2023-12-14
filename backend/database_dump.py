import sqlite3
from random import choice, randint

# Create a connection to the SQLite database
# Note: You'll need to replace 'my_database.db' with the path to your database file
conn = sqlite3.connect('/Users/lucas/facultad/Grupo-I/backend/database/final_program1.db')

# Create a cursor object
c = conn.cursor()

# Insert 50 entries into the 'alumno' table and 'alumnos_planificaciones' table
for _ in range(1, 200):
    # Generate random data for 'altura' and 'peso'
    altura = randint(150, 200)
    peso = randint(50, 100)

    # Insert a new entry into the 'alumno' table
    c.execute("INSERT INTO alumno (id_usuario, estado, altura, peso, planilla_medica) VALUES (?, ?, ?, ?, ?)",
              (randint(1, 100), 'active', altura, peso, 'medica'))

    # Get the ID of the last inserted row
    id_alumno = c.lastrowid

    # Insert a new entry into the 'alumnos_planificaciones' table
    c.execute("INSERT INTO alumnos_planificaciones (id_alumno, id_planificacion) VALUES (?, ?)",
              (id_alumno, randint(1, 100)))

# Insert 50 entries into the 'clase' table
for _ in range(1, 200):
    # Generate random data for 'tipo', 'descripcion', and 'imagen'
    tipo = f"tipo_{randint(1, 100)}"
    descripcion = f"descripcion_{randint(1, 100)}"
    imagen = f"assets/clases/clase_{randint(1, 10)}.jpg"

    # Insert a new entry into the 'clase' table
    c.execute("INSERT INTO clase (tipo, descripcion, imagen) VALUES (?, ?, ?)",
              (tipo, descripcion, imagen))

for _ in range(1, 200):
    # Generate random data for 'horas_semanales', 'nivel', and 'objetivo'
    horas_semanales = randint(1, 10)
    nivel = f"nivel_{randint(1, 100)}"
    objetivo = f"objetivo_{randint(1, 100)}"

    # Insert a new entry into the 'planificacion' table
    c.execute("INSERT INTO planificacion (id_clase, horas_semanales, nivel, objetivo) VALUES (?, ?, ?, ?)",
              (randint(1, 100), horas_semanales, nivel, objetivo))

for _ in range(1, 200):
    # Generate random data for 'certificacion', 'fecha_inicio_actividad', 'sueldo', and 'estado'
    certificacion = f"certificacion_{randint(1, 100)}"
    fecha_inicio_actividad = f"2022-01-{randint(1, 28)}"
    sueldo = randint(1000, 5000)
    estado = 'active'

    aprobacion_pendiente = choice([True, False])
    # Insert a new entry into the 'profesor' table
    c.execute(
        "INSERT INTO profesor (id_usuario, certificacion, fecha_inicio_actividad, sueldo, estado, aprobacion_pendiente) VALUES (?, ?, ?, ?, ?, ?)",
        (randint(1, 100), certificacion, fecha_inicio_actividad, sueldo, estado, aprobacion_pendiente))

    # Get the ID of the last inserted row
    id_profesor = c.lastrowid

    # Insert a new entry into the 'profesores_clases' table
    c.execute("INSERT INTO profesores_clases (id_clase, id_profesor) VALUES (?, ?)",
              (randint(1, 100), id_profesor))

# Define some lists for random selection
roles = ['Alumno', 'Profesor', 'Admin']
sexos = ['Hombre', 'Mujer']

# Insert 50 entries into the 'usuario' table
for i in range(1, 200):
    # Generate random data for 'nombre', 'apellido', 'direccion', 'edad', 'telefono', 'dni', 'rol', 'sexo', 'email', and 'contrasena'
    nombre = f"nombre_{randint(1, 100)}"
    apellido = f"apellido_{randint(1, 100)}"
    direccion = f"direccion_{randint(1, 100)}"
    edad = randint(18, 65)
    telefono = randint(100000000, 999999999)
    dni = randint(10000000, 99999999)
    rol = choice(roles)
    sexo = choice(sexos)
    email = f"emails_{i}@example.com"
    contrasena = f"contrasena_{randint(1, 100)}"

    # Insert a new entry into the 'usuario' table
    c.execute(
        "INSERT INTO usuario (nombre, apellido, direccion, edad, telefono, dni, rol, sexo, email, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (nombre, apellido, direccion, edad, telefono, dni, rol, sexo, email, contrasena))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
