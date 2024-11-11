import os

# Definir un directorio de trabajo inicial (esto depende de tu estructura de carpetas)
os.chdir('module/root_folder')

# Bucle infinito para recibir y procesar comandos continuamente
while True:
    print("\nInput the command: ")
    command = input().strip()

    if command.isnumeric():
        print("Invalid command")

    if command == "pwd":
        # Imprime la ruta absoluta del directorio actual
        abs_path = os.getcwd()
        print(abs_path)

    elif command.startswith("cd"):
        #Si el comando es cd "ruta", intenta cambiar al directorio especificado
        path = command[3:].strip()

        if os.path.isdir(path):
            #cambiar al directorio relativo especifico
            os.chdir(path)
            print(f"Changed directory to: {os.getcwd()}")


    elif command == "cd ..":
        #Si el comando es cd .. retrocede un nivel
        os.chdir("..")
        print(f"Changed directory to: {os.getcwd()}")
        # Si el comando es "cd", intenta cambiar al directorio especificado






