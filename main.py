
from funciones import (fac_elec,fac_diet,fac_gas,fac_res,fac_dig,cant_imp)# Se importa las funciones creadas y rehubicadas para la organizacion del codigo

bienvenida = ("""\n
  -----------------------------------------------------------
             BIENVENIDO A STREAMING COUNTER
              
 ¿Somos concientes del impacto que tenemos en el ambiente?
 ¿Sabias que nuestra actividad virtual tambien deja huella?
        ¿Te interesaria averiguar tu impacto? 
 -------------------------------------------------------------
            """)

menu = ("""\n
  ---------------------------------------------------
             SELECCIONE UNA OPCION
  1. Calcular su impacto ambiental cotidiano
  2. Calcular su impacto virtual
  3. Conocer informacion sobre Green Software
  4. Historial de huella
  5. Salir
  ---------------------------------------------------
        """)

def main():
    print(bienvenida)

    while True:#Da inicio al menu de manera indeterminada hasta que el usuario elija salir
        print(menu)
        opc_prin = input("Por favor, seleccione una opcion(1-5): ")

        if opc_prin == "1":
            print("\n--- Calcular su impacto ambiental cotidiano ---")#Se inicia la recoleccion de datos hacia el usuario.
                    
            res_elec = fac_elec(
                        input("""\n ¿Cuántas personas viven en tu hogar? \n 1. 1 o 2 personas \n 2. 3 o 4 personas \n 3. 5 o mas personas \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cómo describirías el consumo eléctrico general de tu hogar? \n 1. Bajo (pocos electrodomésticos, uso consciente) \n 2. Medio (heladera, TV, PC, uso regular) \n 3. Alto (aire acondicionado/ estufas uso frecuente, muchos dispositivos) \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cuántas horas al día usaste electrodomésticos de alto consumo como el aire acondicionado/estufa? \n 1. Ninguna hora\n 2. 1 a 4 horas \n 3. Más de 4 horas \n Seleccione una opcion(1-3): """))
            res_gas = fac_gas(
                        input("""\n ¿Cómo describirías tu uso del auto hoy? \n 1. No usé el auto / Usé transporte público \n 2. Uso esporádico (pocas cuadras, un par de veces) \n 3. Uso habitual (trabajo, recados, varias veces al día) \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cuál fue tu medio de transporte principal hoy?" \n 1. Caminando / Bicicleta: \n 2. Transporte público (bus/subte): (asumiendo trayectos urbanos normales) \n 3. Auto particular: (asumiendo un uso promedio diario)\n Seleccione una opcion(1-3): """))
            res_res = fac_res(
                        input("""\n ¿Cuánta basura generaste hoy en tu hogar? \n 1. Muy poca (casi nada, mucho reciclaje/compost) \n 2. Normal (bolsa pequeña, algo de reciclaje) \n 3. Mucha (bolsa grande, poco reciclaje) \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cómo manejas tus residuos habitualmente? \n 1. Reciclo y/o compost todo lo posible: \n 2. Reciclo algunos materiales, pero no todo: \n 3 No reciclo ni composto, todo va a la basura: \n Seleccione una opcion(1-3): """))
            res_diet = fac_diet(
                        input("""\n ¿Cómo describirías tu dieta de hoy? \n 1. Principalmente Vegetariana/Vegana: \n 2. Con algo de carne blanca/pescado/lácteos \n 3. Con carne roja (ej., un asado o bife): \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cuántas porciones de carne roja (vaca, cordero) comiste hoy? \n 1. Ninguna: \n 2. 1 porción (ej., bife, milanesa): \n 3. 2 o más porciones (ej., asado grande, dos comidas con carne): \n Seleccione una opcion(1-3): """))

            cant_imp(res_elec,res_gas,res_diet,res_res)

        elif opc_prin == "2":# Se separa el factor virtual para diferenciar el impacto
            print("\n --- Calcular su impacto virtual ---")
            res_dig = fac_dig(
                        input("""\n ¿Cómo gestionas tus datos digitales (fotos, documentos, emails)? \n 1.  Soy muy organizado/a: Elimino lo que no necesito, optimizo archivos y limpio mi email regularmente. \n 2.  Mantengo lo básico: Guardo lo que uso, pero no hago limpiezas muy frecuentes. \n 3.  Guardo todo sin revisar: Acumulo muchos archivos y emails viejos, sin optimizar o borrar. \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cómo describirías tu consumo de streaming de video y videollamadas hoy? \n 1.  Mínimo: Casi no vi videos ni hice videollamadas, o solo por períodos muy cortos. \n 2. Moderado: Vi algunas horas de streaming (TV/películas) o tuve 1-2 videollamadas de duración media. \n 3. Intensivo: Varias horas de streaming en alta calidad, muchas videollamadas o juegos en línea.\n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cuánto tiempo usaste hoy tu computadora (escritorio/laptop) o consola de videojuegos? \n 1. Poco tiempo (menos de 2 horas): Uso ligero, principalmente en celular o tablet. \n 2. Tiempo moderado (2 a 6 horas): Trabajo/estudio, ocio con PC o consola. \n 3. Mucho tiempo (más de 6 horas): Uso intensivo, juegos prolongados, trabajo remoto a tiempo completo.\n Seleccione una opcion(1-3): """),
                        input("""\n ¿Con qué frecuencia sueles reemplazar tus dispositivos electrónicos principales (teléfono, laptop, TV)? \n 1.  Muy raras veces: Uso mis dispositivos hasta que ya no funcionan o por más de 5 años. \n 2. Cada pocos años: Los reemplazo cada 3 a 5 años (ej. actualizo el teléfono regularmente) \n 3. Frecuentemente: Los reemplazo cada 1 a 2 años, siempre buscando lo último.\n Seleccione una opcion(1-3): """))
            
            print("""\nEl total de su impacto es """,res_dig, "kgCO2e/día")
        
        elif opc_prin == "3": #Llama desde la carpeta al archivo txt, para mostrar la informacion
            with open('informacion_basica.txt','r') as archivo:
                print(archivo.read())
        
        elif opc_prin == "4": #Muestra el historial generado por el usuario
            with open('Registro.txt','r') as archivo:
                print(archivo.read())

        elif opc_prin == "5":
            print("¡Gracias por usar la calculadora de huella ambiental! ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2, 3, 4 o 5")

if __name__ == "__main__":
    main()