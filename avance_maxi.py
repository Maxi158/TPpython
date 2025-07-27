import string


bienvenida = ("""
                        Bienvenido a nombre
        ¿Somos concientes del impacto que tenemos en el ambiente?
        ¿Sabias que nuestra actividad virtual tambien deja huella?
                ¿Te interesaria averiguar tu impacto? 
            """)

menu = ("""
                    Seleccione una opcion
        1. Calcular su impacto ambiental cotidiano
        2. Calcular su impacto virtual
        3. Conocer informacion sobre Green Software
        4. Salir
        """)
    
def fac_elec(tam_hog,cons_dia,cons_alt):
    caracter = ""
    cont1 = 0
    if tam_hog:
        caracter += string.digits
        if tam_hog == "1":
            cont1 += 1.2
        elif tam_hog == "2":
            cont1 += 0.8
        elif tam_hog == "3":
            cont1 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
        
    if cons_dia:
        caracter += string.digits
        if cons_dia == "1":
             cont1 += 1.2
        elif cons_dia == "2":
             cont1 += 0.8
        elif cons_dia == "3":
             cont1 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if cons_alt:
        caracter += string.digits
        if cons_alt == "1":
            cont1 += 1.2
        elif cons_alt == "2":
            cont1 += 0.8
        elif cons_alt == "3":
            cont1 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    return cont1

def fac_gas(km_rec,frec_uso,trans_pri):
    caracter = ""
    cont2 = 0
    if km_rec:
        caracter += string.digits
        if km_rec == "1":
            cont2 += 1.2
        elif km_rec == "2":
            cont2 += 0.8
        elif km_rec == "3":
            cont2 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if frec_uso:
        caracter += string.digits
        if frec_uso == "1":
            cont2 += 1.2
        elif frec_uso == "2":
            cont2 += 0.8
        elif frec_uso == "3":
            cont2 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if trans_pri:
        caracter += string.digits
        if trans_pri == "1":
            cont2 += 1.2
        elif trans_pri == "2":
            cont2 += 0.8
        elif trans_pri == "3":
            cont2 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    return cont2
    
def fac_res(cant_res,hab_res):
    caracter = ""
    cont3 = 0
    if cant_res:
        caracter += string.digits
        if cant_res == "1":
            cont3 += 1.2
        elif cant_res == "2":
            cont3 += 0.8
        elif cant_res == "3":
            cont3 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if hab_res:
        caracter += string.digits
        if hab_res == "1":
            cont3 += 1.2
        elif hab_res == "2":
            cont3 += 0.8
        elif hab_res == "3":
            cont3 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    
    return cont3

def fac_diet(tip_diet,can_dia):
    caracter = ""
    cont4 = 0 
    if tip_diet:
        caracter += string.digits
        if tip_diet == "1":
            cont4 += 1.2
        elif tip_diet == "2":
            cont4 += 0.8
        elif tip_diet == "3":
            cont4 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
         
    if can_dia:
        caracter += string.digits
        if can_dia == "1":
            cont4 += 1.2
        elif can_dia == "2":
            cont4 += 0.8
        elif can_dia == "3":
            cont4 += 0.6
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    return cont4

def cant_imp(res_elec,res_gas,res_diet,res_res):
    imp_tot = (res_elec + res_gas + res_diet + res_res)
    print(f"\n Su impacto total es :{imp_tot}")
    if imp_tot < 20:
        print ("Su huella es menor")
    elif imp_tot < 40:
        print ("Su huella es promedio")
    elif imp_tot < 60:
        print ("Su huella es muy alta")
    else:
        print("error")
    return imp_tot

def main():
    print(bienvenida)

    while True:
        print(menu)
        opc_prin = input("Por favor, seleccione una opcion(1-4): ")

        if opc_prin == "1":
            print("\n--- Calcular su impacto ambiental cotidiano ---")
                    
            res_elec = fac_elec(
                        input("""\n ¿Cuántas personas viven en tu hogar? \n 1. 1 o 2 personas \n 2. 3 o 4 personas \n 3. 5 o mas personas \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cómo describirías el consumo eléctrico general de tu hogar? \n 1. Bajo (pocos electrodomésticos, uso consciente) \n 2. Medio (heladera, TV, PC, uso regular) \n 3. Alto (aire acondicionado/ estufas uso frecuente, muchos dispositivos) \n Seleccione una opcion(1-3): """),
                        input("""\n ¿Cuántas horas al día usaste electrodomésticos de alto consumo como el aire acondicionado/estufa? \n 1. Ninguna hora\n 2. 1 a 4 horas \n 3. Más de 4 horas \n Seleccione una opcion(1-3): """))
            res_gas = fac_gas(
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """),
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """),
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """))
            res_res = fac_res(
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """),
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """))
            res_diet = fac_diet(
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """),
                        input("""\n op1\n op2 \n op3\n Seleccione una opcion(1-3): """)) 

            cant_imp(res_elec,res_gas,res_diet,res_res)

        elif opc_prin == "4":
            print("¡Gracias por usar la calculadora de huella ambiental! ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2, 3 o 4")

if __name__ == "__main__":
    main()