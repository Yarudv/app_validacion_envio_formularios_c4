import random
import time
print("Bienvenido a nuestra app")
inicio = int(input("Opcion 1 para registrarse / Opcion 2 para enviar formularios: "))
if inicio == 1:
    crear = str(input("¿Deseas registrarte en nuestra app? (s/n): "))
    if crear == 's':
        nombre = []
        nombre.append(str(input("Ingrese su nombre de usuario: ")))   
        print(nombre[0])
        contraseña = []
        contraseña.append(str(input("Ingrese su contraseña entre 8-10 digitos entre numeros, caracteres especiales, letras minusculas y mayúsculas:")))
        print(contraseña[0])
        print(len(contraseña[0]))
        digitos = int(len(contraseña[0]))
        if digitos < 8 or digitos > 10:
            while True:
                del[contraseña[0]]
                contraseña.append(str(input("Su contraseña no cumple con 8-10 digitos entre numeros, caracteres especiales, letras minusculas y mayúsculas. Vuelva a ingresar: ")))
                digitos = len(contraseña[0])
                if digitos >= 8 and digitos <= 10:
                    print("Contraseña guardada satisfactoriamente...")
                    break
        else:
            print("Contraseña guardada satisfactoriamente...")
    else:
        print("Gracias por visitarnos...")
else:
    formularios = ["Hábitos alimenticios", "Experiencia laboral", "Actividades recreativas", "Atletismo", "Natacion", "Deportes general"]
    usuarios = []
    usuarios.append(str(input("Ingrese nombre de usuario 1: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 2: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 3: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 4: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 5: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 6: ")))
    usuarios.append(str(input("Ingrese nombre de usuario 7: ")))
    def formu_aleatorio (formularios):
        return random.choice(formularios)
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    i = 0
    j = 0
    k = 0
    lista_a = []
    lista_b =[]
    lista_c = []
    lista_d = []
    lista_e = []
    lista_f = []
    lista_g = []
    for a in range(5):
        var1= str(formu_aleatorio(formularios))
        print("Enviando formulario", var1, "al usuario", usuarios[0],"...")
        lista_a.append(var1)
        time.sleep(3)
        print("El formulario",var1,"ha sido enviado satisfactoriamente")
    for b in range(5):
        var2= str(formu_aleatorio(formularios))
        print("Enviando formulario", var2, "al usuario", usuarios[1],"...")
        lista_b.append(var2)
        time.sleep(3)
        print("El formulario",var2,"ha sido enviado satisfactoriamente")
    for c in range(5):
        var3= str(formu_aleatorio(formularios))
        print("Enviando formulario", var3, "al usuario", usuarios[2],"...")
        lista_c.append(var3)
        time.sleep(3)
        print("El formulario",var3,"ha sido enviado satisfactoriamente")
    for d in range(5):
        var4= str(formu_aleatorio(formularios))
        print("Enviando formulario", var4, "al usuario", usuarios[3],"...")
        lista_d.append(var4)
        time.sleep(3)
        print("El formulario",var4,"ha sido enviado satisfactoriamente")
    for e in range(5):
        var5= str(formu_aleatorio(formularios))
        print("Enviando formulario", var5, "al usuario", usuarios[4],"...")
        lista_e.append(var5)
        time.sleep(3)
        print("El formulario",var5,"ha sido enviado satisfactoriamente")
    for f in range(5):
        var6= str(formu_aleatorio(formularios))
        print("Enviando formulario", var6, "al usuario", usuarios[5],"...")
        lista_f.append(var6)
        time.sleep(3)
        print("El formulario",var6,"ha sido enviado satisfactoriamente")
    for g in range(5):
        var7= str(formu_aleatorio(formularios))
        print("Enviando formulario", var7, "al usuario", usuarios[6],"...")
        lista_g.append(var7)
        time.sleep(3)
        print("El formulario",var7,"ha sido enviado satisfactoriamente")
    lista_total = [lista_a, lista_b, lista_c, lista_d, lista_e, lista_f, lista_g] 
    for i in range(len(lista_total)):
        print("Para el usuario", usuarios[i], "los formularios enviados son: ", lista_total[i])
       
            



