# Generador email
print("Bienvenido al sistema de generacion de email de ciudad gotica")
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
dominio_email = "@ciudadgotica.com"

print(f'''\tTu nuevo email generado por el sistema es:\n\t{nombre.lower()}.{apellido.lower()}{dominio_email}
\t*** Felicidades ***''')