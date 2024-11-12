import time, random, os
os.system("clear")

print("hola soy un perrito. -Guau, Guau")

salud = 100
hambre = 0
sueno = 0

estado = True

while salud > 0:
    gSalud = ""
    gHambre = "" 
    gSueno = ""

    print("""
       _=,_             [A]  Acariciar
    o_/6 /#\            [C]  Alimentar
    \__ |##/            [D]  Dormir 
     ='|--\             
       /   #'-.
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/             
    """)

    # Representar gráficamente la salud
    for i in range(10):
        if i <= (salud // 10):
            gSalud += "#"
        else:
            gSalud += "·"
        if i >= (hambre // 10):
            gHambre += "#"
        else:
            gHambre += "·"
        if i >= (sueno // 10):
            gSueno += "#"
        else:
            gSueno += "·"
            
    print("Salud: " + gSalud + " [" + str(salud) + "]")
    print("hambre: " + gHambre + " [" + str(hambre) + "]")
    print("sueño: " + gSueno + " [" + str(sueno) + "]") 
    print("")   

    respuesta = input("Inserta tu respuesta: ") 
    if respuesta.upper() == "A" and salud <= 100:
        salud += random.randint(7, 15)
        if salud > 100:
            salud = 100
    if respuesta.upper() != "A":
        salud -= random.randint(2, 15) 
    if respuesta.upper() == "C" and hambre >= 0:
        hambre -= random.randint(10, 20)
        salud += random.randint(4, 6)
        if hambre < 0:
            hambre = 0
    if respuesta.upper() != "C":
        hambre += random.randint(5, 15)
    if respuesta.upper() == "P":
        salud -= random.randint(0, 80)
    if respuesta.upper() == "M":
        salud = 0
    if respuesta.upper() == "D" and sueno >= 65:
        os.system("clear")
        print("""
 z       
  z      
   z   _=,_             
    o_/- /#\            
    \__ |##/            
     ='|--\             
       /   #'-.
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/    
        """)
        sueno = 0
        salud += random.randint(5, 10)
        hambre += random.randint(15, 30)
        time.sleep(random.randint(2, 6))
    elif sueno < 65 and respuesta.upper() == "D":
        print("No tengo sueño todavía")
    if respuesta.upper() != "D":
        sueno += random.randint(10, 20)
 

    if hambre >= 70:
        salud -= 7
        if hambre >= 90:
            salud -= 6

    
    
    time.sleep(1)
    os.system("clear")

print("Tu perrito ha muerto >:(")
print("""
       _=,_             
    o_/x /#\            
    \__ |##/            
     ='|--\             
       /   #'-.
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/    
""")
 
