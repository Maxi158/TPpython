import string
import datetime
fecha = datetime.date.today().strftime("%d/%m/%y")

#se importan las funciones necesarias para que las funciones puedan llevarse a cabo

def fac_elec(tam_hog,cons_dia,cons_alt):#Se define el valor de las varieables segun cada respuesta
    caracter = ""
    cont1 = 0
    if tam_hog:
        caracter += string.digits
        if tam_hog == "1":
            cont1 += 1
        elif tam_hog == "2":
            cont1 += 0.6
        elif tam_hog == "3":
            cont1 += 0.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
        
    if cons_dia:
        caracter += string.digits
        if cons_dia == "1":
            cont1 += 1.6
        elif cons_dia == "2":
            cont1 += 3.3
        elif cons_dia == "3":
            cont1 += 6.7
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if cons_alt:
        caracter += string.digits
        if cons_alt == "1":
            cont1 += 0
        elif cons_alt == "2":
            cont1 += 1.6
        elif cons_alt == "3":
            cont1 += 3.3
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    return cont1

def fac_gas(frec_uso,trans_pri): #Se repite las mismas funciones variando los valores de consumo
    caracter = ""
    cont2 = 0

    if frec_uso:
        caracter += string.digits
        if frec_uso == "1":
            cont2 += 0
        elif frec_uso == "2":
            cont2 += 0.5
        elif frec_uso == "3":
            cont2 += 2
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if trans_pri:
        caracter += string.digits
        if trans_pri == "1":
            cont2 += 0
        elif trans_pri == "2":
            cont2 += 0.2
        elif trans_pri == "3":
            cont2 += 1.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    return cont2
    
def fac_res(cant_res,hab_res):
    caracter = ""
    cont3 = 0
    if cant_res:
        caracter += string.digits
        if cant_res == "1":
            cont3 += 0.1
        elif cant_res == "2":
            cont3 += 0.5
        elif cant_res == "3":
            cont3 += 1.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if hab_res:
        caracter += string.digits
        if hab_res == "1":
            cont3 += 0.2
        elif hab_res == "2":
            cont3 += 0.7
        elif hab_res == "3":
            cont3 += 1.2
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    
    return cont3

def fac_diet(tip_diet,can_dia):
    caracter = ""
    cont4 = 0 
    if tip_diet:
        caracter += string.digits
        if tip_diet == "1":
            cont4 += 1
        elif tip_diet == "2":
            cont4 += 2.5
        elif tip_diet == "3":
            cont4 += 4.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
         
    if can_dia:
        caracter += string.digits
        if can_dia == "1":
            cont4 += 0
        elif can_dia == "2":
            cont4 += 2
        elif can_dia == "3":
            cont4 += 4.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    return cont4

def fac_dig(alm_ges,cons_stre,cons_dia,rem_dis):
    caracter = ""
    cont5 = 0
    if alm_ges:
        caracter += string.digits
        if alm_ges == "1":
            cont5 += 0.02
        elif alm_ges == "2":
            cont5 += 0.1
        elif alm_ges == "3":
            cont5 += 0.3
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
        
    if cons_stre:
        caracter += string.digits
        if cons_stre == "1":
            cont5 += 0.5
        elif cons_stre == "2":
            cont5 += 0.3
        elif cons_stre == "3":
            cont5 += 1
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    if cons_dia:
        caracter += string.digits
        if cons_dia == "1":
            cont5 += 0.1
        elif cons_dia == "2":
            cont5 += 0.4
        elif cons_dia == "3":
            cont5 += 0.8
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
    if rem_dis:
        caracter += string.digits
        if rem_dis == "1":
            cont5 += 0.05 
        elif rem_dis == "2":
            cont5 += 0.2
        elif rem_dis == "3":
            cont5 += 0.5
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    return cont5

def cant_imp(res_elec,res_gas,res_diet,res_res):#Suma todos los factores de la opcion 1, comparando y etiquetando segun los resultados
    imp_tot = (res_elec + res_gas + res_diet + res_res)
    print(f"""\n\n\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n Su impacto total es :{imp_tot}(kgCO2e/día)""")
    histo_huella(res_elec,res_gas,res_res,res_diet,imp_tot)#luego de obtener los resultados se guardan en el historial
    if imp_tot < 8:
        print ("""Su huella es Baja/Menor \n Felicitaciones a seguir asi!!""")
    elif imp_tot < 20:
        print ("Su huella es Media/Promedio")
    elif imp_tot > 20:
        print ("Su huella es Muy Alta")
    else:
        print("Error")
    return imp_tot
    
def histo_huella(res_elec,res_gas,res_res,res_diet,imp_tot):# Genera una lista que detalla y anota en un archivo externo los valores, el total y la fecha.
    registro = open("Registro.txt","a")
    registro.write(f"""\n\n
    -----------------------------------------------------------------
    Se registro en la fecha de {fecha}
    Huella de carbono asociada a los factores electronicos {res_elec}
    Huella de carbono asociada a los factores de gas {res_gas}
    Huella de carbono asociada a los factores de residuos {res_res}
    Huella de carbono asociada a los factores de dieta {res_diet}

    El impacto total del dia {fecha} es de {imp_tot}
    -----------------------------------------------------------------
            """)
    registro.close()

