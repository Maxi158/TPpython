import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Error interno: No hay tipos de caracteres seleccionados."

    contrasena_lista = []
    if incluir_minusculas:
        contrasena_lista.append(random.choice(string.ascii_lowercase))
    if incluir_mayusculas:
        contrasena_lista.append(random.choice(string.ascii_uppercase))
    if incluir_numeros:
        contrasena_lista.append(random.choice(string.digits))
    if incluir_simbolos:
        contrasena_lista.append(random.choice(string.punctuation))

    for _ in range(longitud - len(contrasena_lista)):
        contrasena_lista.append(random.choice(caracteres))

    random.shuffle(contrasena_lista)
    return ''.join(contrasena_lista)

# --- INICIO DE CORRECCIONES DE INDENTACIÓN Y ESTRUCTURA ---

# La función mostrar_menu() debe estar al mismo nivel que generar_contrasena()
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Generar Contraseña")
    print("2. Ver Instrucciones")
    print("3. Salir")
    print("----------------------")

# La función mostrar_instrucciones() DEBE ESTAR SEPARADA y al mismo nivel que mostrar_menu()
def mostrar_instrucciones():
    print("\n--- INSTRUCCIONES ---")
    print("Esta aplicación te permite generar contraseñas seguras.")
    print("Podrás elegir la longitud de la contraseña y qué tipos de caracteres incluir:")
    print("- Letras minúsculas")
    print("- Letras mayúsculas")
    print("- Números")
    print("- Símbolos")
    print("¡Utiliza contraseñas fuertes para proteger tu información!")
    print("----------------------")

# La función main() DEBE ESTAR SEPARADA y al mismo nivel que las otras funciones
def main():
    print("¡Bienvenido al Generador de Contraseñas!") # Cambié el mensaje de "crea tu contraseña" a este

    # Todo el bucle 'while True' y su contenido debe estar indentado dentro de main()
    while True:
        mostrar_menu() # Llama a la función para mostrar las opciones del menú
        opcion = input("Por favor, selecciona una opción (1-3): ")

        if opcion == '1':
            print("\n--- Generar Nueva Contraseña ---")

            while True:
                try:
                    longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
                    if longitud <= 0:
                        print("La longitud debe ser un número positivo.")
                        continue

                    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
                    incluir_mayusculas = input("Incluir letras mayúsculas? (s/n): ").lower() == 's'
                    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
                    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

                    min_longitud_requerida = 0
                    if incluir_minusculas: min_longitud_requerida += 1
                    if incluir_mayusculas: min_longitud_requerida += 1
                    if incluir_numeros: min_longitud_requerida += 1
                    if incluir_simbolos: min_longitud_requerida += 1

                    if min_longitud_requerida == 0:
                        print("Error: Debes seleccionar al menos un tipo de caracter (minúsculas, mayúsculas, números o símbolos).")
                        continue

                    if longitud < min_longitud_requerida:
                        print(f"La longitud mínima para los tipos de caracteres seleccionados es {min_longitud_requerida}.")
                        print("Por favor, aumente la longitud o cambie sus selecciones.")
                        continue

                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para la longitud.")

            contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
            print(f"\nContraseña generada: {contrasena_generada}")

        elif opcion == '2':
            # Ahora sí, podemos llamar a mostrar_instrucciones porque está definida correctamente
            mostrar_instrucciones()

        elif opcion == '3':
            print("¡Gracias por usar el Generador de Contraseñas! ¡Adiós!") # Volví al mensaje original
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Esto DEBE ESTAR al final del archivo y al mismo nivel que las definiciones de funciones (sin indentación)
if __name__ == "__main__":
    main()

