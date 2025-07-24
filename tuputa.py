
temperatura = float(input("ingrese temperatura:"))
clase = str(input("Es Farenheit(F) o es Celcius(C)?:"))

if clase == "C" or "c":
    print("En Farenheit son ",(temperatura * 1.8 )+32) 
elif clase == "F" or "f":
    print("En Celsius son",(temperatura-32)/1.8)
else:
    print("Escala incorrecta")
