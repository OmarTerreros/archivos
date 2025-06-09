nombre= input("Escribe tu nombre:")

nombre1=nombre.istitle()
print (nombre1)

if nombre1== True:
    print("Tu Nombre esta bien")
elif nombre1 == False:
    print("Tu nombre esta mal")
    nombre2=nombre.title()
    print(f"Tu nombre es asi:{nombre2}")
    
