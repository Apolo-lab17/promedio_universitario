

"""
PROMEDIO UNIVERSITARIO v2.0 SIGUIENDO EL CALCULO DE LA UNIVERSIDAD CESAR VALLEJO
Calcula suma total 4 notas + Promedio
Hecho por: [Steven]
"""

print("\n==========================PROMEDIO UNIVERSITARIO===================================\n")

print("\nRESGISTRAR NOTAS ........ ⌨️\n")


notas = []
nota_multi = []

while True:
    try:
        nota1 = float(input(f"Ingrese la 1️⃣   nota:"))
        notas.append(nota1)

        porcentaje1 = float(input("Ingrese el % que vale la nota:"))
        nota_multi.append(nota1 * porcentaje1)


        nota2 = float(input(f"Ingrese la 2️⃣   nota:"))
        notas.append(nota2)

        porcentaje2 = float(input("Ingrese el porcentaje que vale la nota:"))
        nota_multi.append(nota2 * porcentaje2)


        nota3 = float(input(f"Ingrese la 3️⃣   nota:"))
        notas.append(nota3)

        porcentaje3 = float(input("Ingrese el porcentaje que vale la nota:"))
        nota_multi.append(nota3 * porcentaje3)


        nota4 = float(input(f"Ingrese la 4️⃣   nota:"))
        notas.append(nota4)

        porcentaje4 = float(input("Ingrese el porcentaje que vale la nota:"))
        nota_multi.append(nota4 * porcentaje4)

        total = sum(nota_multi)
        print(f"Total ponderado {total}")

        porcentaje_unidad = float(input("Ingrese el % que vale la unidad:"))
        nota_final = total * porcentaje_unidad
        print(f" 🎓  PROMEDIO FINAL:{nota_final}")


        print("\n=================RESULTADO 👀 ===================\n")


        if nota_final <=3:
           print(f"Tiene un promedio bajo,{nota_final}, ¡A mejorar!  😓 😢 ")
        elif 5 <= nota_final <= 6:
            print(f"Buen promedio, {nota_final}, ¡Felicidades! 😃👏")
        else: 
            print(f"Felicidades eres 🫵 🤖 una maquina, tienes un promedio alto de, {nota_final} 🦾💯")

        print("\n==========================================================================\n")
        
        print("Presione Enter si desea continuar....")
        salir = input("¿Desea calcular otra unidad 📝 ? (Enter=Si 'salir'=No):").lower().strip()
        

        if salir == 'salir':
            print("¡Gracias por usar PROMEDIO UCV v2.0! 👋  ....")
            break
        
    
    except(ValueError, KeyboardInterrupt):
       print("❌ !Error¡ Solo numeros validos")
       continue

