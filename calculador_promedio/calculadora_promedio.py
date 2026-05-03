

"""
PROMEDIO UNIVERSITARIO v1.0
Calcula promedio 4 notas + calificación
Hecho por: [Steven]
"""

print("\n----------------------------PROMEDIO UNIVERSITARIO------------------------------\n")

print("\nRESGISTRAR NOTAS ........ ⌨️\n")


notas = []
suma = 0

while True:
    try:
        nota1 = float(input(f"Ingrese la 1️⃣   nota:"))
        notas.append(nota1)

        nota2 = float(input(f"Ingrese la 2️⃣   nota:"))
        notas.append(nota2)

        nota3 = float(input(f"Ingrese la 3️⃣   nota:"))
        notas.append(nota3)

        nota4 = float(input(f"Ingrese la 4️⃣   nota:"))
        notas.append(nota4)

        total = sum(notas)
        promedio = total / len(notas)

        if promedio <= 10:
           print("\n------RESULTADO FINAL 👀 ------\n")
           print(f"Desaprobaste, tu promedio es de {promedio} 😓 😢 ")
           print("\n-----------------------------------\n")


        elif 11 < promedio < 16:
            print("\n------RESULTADO FINAL 👀 ------\n")
            print(f"Felicicidades aprobaste, tienes un promedio de {promedio} 😃👏")
            print("\n----------------------------------\n")


        else: 
           print("\n------RESULTADO FINAL 👀 ------\n")
           print(f"Felicidades eres 🫵 🤖 una maquina, tienes un promedio alto de, {promedio} 🦾💯")

           print("\n----------------------------------\n")
        
        salir = input("¿Desea continuar calculando tus notas 📝 ? (o 'salir'):").lower().strip()

        if salir == 'salir':
            print("Gracias por usar la calculadora, nos vemos pronto 👋  ....")
            print("\n-----------------------------------------\n")
            break
        
    
    except:
       print("❌ Error, solo numeros")

