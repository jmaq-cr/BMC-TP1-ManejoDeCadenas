#Tecnológico de Costa Rica, Sede Cartago
#Escuela de Ingeniería en Computación
#Introducción a la Biología Molecular Computacional
#Tarea Programada #1
#Estudiantes
#   Jose Manuel Aguilar Quesada
#   Crisia Piedra Chavez
#Primer Semestre, 2017

from random import *

def menuPrincipal():
    salir = False
    cadena = ""
    opcion = ""
    while salir != True:
        print("\n\nTarea Programada #1\nElija una de las siguientes opciones:")
        print("1. Generador de números aleatorios\n2. Verificar ADN\n3. Verificar ARN\n4. Largo de una cadena\n5. Obtener elemento i-ésimo\n6. Verificar subsecuencias y supersecuencias")
        print("7. Verificar substrings y superstring\n8. Intervalo de una cadena\n9. Concatenar cadenas\n10. Prefijo\n11. Sufijo\n12. Verificar prefijo\n13. Verificar sufijo\n14. Complemento\n15. Complemento Inverso\n16. Verificar palíndromo")
        print("17. Generar secuencia de ADN\n18. Traducir ADN a ARN\n19. Traductor Genético\n20. Salir")
        opcion = str(input("Ingrese una opción >>"))
        if opcion == "1": #Generador de números
            cant = 0
            tipo = ""
            try:
                cant = int(input("Cuántos números desea generar? "))
                tipo = str(input("Seleccione el tipo de distribución:\n1. Normal\n2. Lineal\n3. Poisson\n>>"))
                if tipo == "1":
                    media = int(input("Media: "))
                    desv = int(input("Desviación: "))
                    print(generadorNormal(cant,media,desv))
                elif tipo == "2":
                    a = int(input("Límite menor: "))
                    b = int(input("Límite mayor: "))
                    print(generadorLineal(cant,a,b))
                elif tipo == "3":
                    a = int(input("Ocurrencias: "))
                    b = int(input("Esperanza: "))
                    print(generadorPoisson(cant,a,b))
                else:
                    print("La opción no es válida")
            except:
                print("La cantidad no es correcta")
        elif opcion == "2": #Verificar ADN
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(verificador_adn(hilera))
        elif opcion == "3": #Verificar ARN
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(verificador_arn(hilera))
        elif opcion == "4": #Largo hilera
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(largo_hilera(hilera))
        elif opcion == "5": #Elemento i-esimo
            print("Cargue su hilera:")
            hilera = cargarHilera()
            pos = 0
            try:
                pos = int(input("Ingrese la posición >>"))
                print(obtener_elemento(hilera,pos))
            except:
                print("La posición no es válida")
        elif opcion == "6": #Subsecuencia
            print("Cargue su hilera pequeña: >>")
            hilerap = cargarHilera()
            print("Cargue su hilera grande: >>")
            hilerag = cargarHilera()
            if esSubsecuencia(hilerap,hilerag) == True:
                print("Las hileras son subsecuencia y supersecuencia una de la otra")
            else:
                print("Las hilera NO son subsecuencia ni supersecuencia")
                
        elif opcion == "7": #substring
            print("Cargue su hilera pequeña: >>")
            hilerap = cargarHilera()
            print("Cargue su hilera grande: >>")
            hilerag = cargarHilera()
            if esSubstring(hilerap,hilerag) == True:
                print("Las hileras son substring y superstring una de la otra")
            else:
                print("Las hilera NO son substring ni superstring")
        elif opcion == "8": #intervalo
            print("Cargue su hilera:")
            hilera = cargarHilera()
            try:
                posi = int(input("Ingrese la posición i (inicial) >>"))
                posj = int(input("Ingrese la posición j (final) >>"))
                print(intervalo(posi,posj,hilera))
            except:
                print("Las posiciones no son válidas")
        elif opcion == "9": #Concatenación
            print("Cargue su hilera1:")
            hilera1 = cargarHilera()
            print("Cargue su hilera2:")
            hilera2 = cargarHilera()
            print(concatenacion(hilera1,hilera2))
        elif opcion == "10": #Prefijo
            print("Cargue su hilera1:")
            hilera = cargarHilera()
            posi = int(input("Ingrese la posición >>"))
            print (operacionPrefijo(hilera,posi))
        elif opcion == "11": #Sufijo
            hilera = cargarHilera()
            posi = int(input("Ingrese la posición >>"))
            print (operacionSufijo(hilera,posi))
        elif opcion == "12": #Verificar prefijo
            print("Cargue la Subhilera:")
            hilera1 = cargarHilera()
            print("Cargue su hilera:")
            hilera2 = cargarHilera()
            print (verificarP_prefijoS(hilera1,hilera2))
        elif opcion == "13": #Verificar sufijo
            print("Cargue la Subhilera:")
            hilera1 = cargarHilera()
            print("Cargue su hilera:")
            hilera2 = cargarHilera()
            print (verificarS_SufijoT(hilera1,hilera2))
        elif opcion == "14": #Complemento
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print (calcular_Complemento_ADN(hilera))
        elif opcion == "15": #Complemento inverso
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(calcular_Complemento_Invertido_ADN(hilera))
        elif opcion == "16": #palindromo
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(verificarPalindromo(hilera))
        elif opcion == "17": #Generador de secuencias
            try:
                tamano = int(input("Ingrese el tamaño de la hilera >>"))
                print(generadorAdn(tamano))
            except:
                print("El tamaño no es válido")
        elif opcion == "18": #Traductor ADN a ARN
            print("Cargue su hilera:")
            hilera = cargarHilera()
            print(traductorAdnArn(hilera))
        elif opcion == "19": #Traductor ADN a aminoacidos
            print("Cargue su hilera:")
            hilera = cargarHilera()
            opc = str(input("Elija el formato del aminoácido:\n1. Letra\n2. Abreviatura\n3. Nombre\n>>"))
            if opc == "1" or opc == "2" or opc == "3":
                print(adnAminoacidos(hilera,int(opc)))
            else:
                print("La opción elejida no es válida")
        elif opcion == "20":
            print("Saliendo...")
            break
        else:
            print("La opción no es válida")

#Del punto 4.a

def generadorNormal(cant,media, desv):
    res = []
    for i in range(cant):
        res.append(normalvariate(media,desv))
    return res

def generadorLineal(cant,a,b):
    res = []
    for i in range(cant):
        res.append(uniform(a,b))
    return res

def generadorPoisson(cant,a,b):
    res = []
    for i in range(cant):
        res.append(weibullvariate(a,b))
    return res


def cargarHilera():
    texto = ""
    tipo = str(input("1. Texto\n2. Archivo\n>>"))
    if tipo == "1":
        texto = str(input("Ingrese su cadena:\n>>"))
        return texto
    elif tipo == "2":
        direc = str(input("Ingrese la dirección de su archivo:\n>>"))
        try:
            file = open(direc,"r")
            texto = file.read()
            return texto
        except:
            print("Dirección no encontrada")
    else:
        print ("Opción no válida")
        return texto



def verificador_adn(cadena):
    for i in cadena:
        if i!="A" and i!="a" and i!="C" and i!="c" and i!="T" and i!="t" and i!="G" and i!="g":
            return False
    return True

def verificador_arn(cadena):
    for i in cadena:
        if i!="A" and i!="a" and i!="C" and i!="c" and i!="U" and i!="u" and i!="G" and i!="g":
            return False
    return True

def largo_hilera(cadena):
    return len(cadena)

##recordar que en clase se dijo que para las cadena de ADN y ARN se empieza
##a contar desde 1 no desde 0 como se hace normalmente en programación
def obtener_elemento(cadena,posicion):
    if posicion < 1 or posicion >= len(cadena):
        print("Fuera de rango")
        return ""
    else:
        return cadena[posicion-1]

def esSubsecuencia(cadenaMenor,cadenaMayor):
    pos = 0
    for i in cadenaMayor:
        if i == cadenaMenor[pos]:
            if pos < len(cadenaMenor)-1:
                pos = pos + 1
            else:
                return True
    return False

def esSubstring(cadenaMenor,cadenaMayor):
    return(cadenaMenor in cadenaMayor)

##recordar que en clase se dijo que para las cadena de ADN y ARN se empieza
##a contar desde 1 no desde 0 como se hace normalmente en programación
def intervalo(indicei,indicej,cadena):
    respuesta = ""
    indicei = indicei - 1
    indicej = indicej - 1
    if indicei < 0 or indicej < 0 or indicei >= len(cadena) or indicej >= len(cadena):
        print("fuera de rango")
        return ""
    if indicei >= indicej:
        return respuesta
    else:
        while indicei <= indicej:
            respuesta += cadena[indicei]
            indicei = indicei + 1
        return respuesta
def concatenacion(cadena1, cadena2):
    cadenaResultante= cadena1+cadena2
    return cadenaResultante
def operacionPrefijo(s,k):
    if k > len (s):
        print ("Debe ingresar un valor k menor o igual a ", len(s))
        return ""
    elif k <=0:
        print ("Debe ingresar un valor k mayor a 0 ")
        return ""
    else:
        s= s[:(k)]
        return s
def operacionSufijo(s,k):
    if k > len (s):
        print ("Debe ingresar un valor k menor o igual a ", len(s))
        return ""
    elif k <=0:
        print ("Debe ingresar un valor k mayor a 0 ")
        return ""
    else:
        s= s[-(k):]
        return s

def verificarPalindromo(hilera):
    hileraInversa= hilera[::-1]
    if hileraInversa == hilera:
        return True
    else:
        return False
    
def verificarP_prefijoS(subcadena,cadena):
    if len(subcadena)>len(cadena):
        return False
    else:
        i=0
        while i < (len(subcadena)):
            if subcadena[i] != cadena[i]:
                return False
            i=i+1
        return True

def verificarS_SufijoT(subcadena,cadena):
    if len(subcadena)>len(cadena):
        return False
    else:
        i=0
        while i < (len(subcadena)):
            if subcadena[(len(subcadena)-1)-i] != cadena[(len(cadena)-1)-i]:
                return False
            i=i+1
        return True

def calcular_Complemento_ADN(hilera):
    hileraComplemento=""
    if len(hilera)==0:
        return hileraComplemento 
    elif verificador_adn(hilera)== True:
        for x in range (len(hilera)):
            if hilera[x] == "A" or hilera[x] == "a":
                hileraComplemento=hileraComplemento+"T"
            elif hilera[x] == "G" or hilera[x] == "g":
                hileraComplemento=hileraComplemento+"C"
            else:
                hileraComplemento= hileraComplemento+hilera[x]
        return hileraComplemento

def calcular_Complemento_Invertido_ADN(hilera):
    hileraComplemento=""
    if len(hilera)==0:
        return hileraComplemento
    elif verificador_adn(hilera)== True:
        for x in range (len(hilera)):
            if hilera[x] == "A" or hilera[x] == "a":
                hileraComplemento=hileraComplemento+"T"
            elif hilera[x] == "G" or hilera[x] == "g":
                hileraComplemento=hileraComplemento+"C"
            elif hilera[x] == "C" or hilera[x] == "c":
                hileraComplemento=hileraComplemento+"G"
            elif hilera[x] == "T" or hilera[x] == "t":
                hileraComplemento=hileraComplemento+"A"               
        hileraComplemento= hileraComplemento[::-1]     
    return hileraComplemento                 


#Del punto 4.b        
    
def generadorAdn(tamanoCadena):
    opciones = ["A","C","T","G"]
    resultado = ""
    for i in range(tamanoCadena):
        resultado += opciones[randint(0,3)]
    return resultado
    
#Del punto 4.c
def traductorAdnArn(cadenaAdn):
    resultado = ""
    for i in cadenaAdn:
        if i == "T":
            resultado += "U"
        else:
            resultado += i
    return resultado

#Del punto 4.d
def adnAminoacidos(cadena,tipo):
    matriz = [["UUU","F","Phe","Phenylalanine"],["UUC","F","Phe","Phenylalanine"],["UUA","L","Leu","Leucine"],["UUG","L","Leu","Leucine"],["CUU","L","Leu","Leucine"],["CUC","L","Leu","Leucine"],["CUA","L","Leu","Leucine"],["CUG","L","Leu","Leucine"],["AUU","I","Ile","Isoleucine"],["AUC","I","Ile","Isoleucine"],["AUA","I","Ile","Isoleucine"],["AUG","M","Met","Methionine"],["GUU","V","Val","Valine"],["GUC","V","Val","Valine"],["GUA","V","Val","Valine"],["GUG","V","Val","Valine"],["UCU","S","Ser","Serine"],["UCC","S","Ser","Serine"],["UCA","S","Ser","Serine"],["UCG","S","Ser","Serine"],["CCU","P","Pro","Proline"],["CCC","P","Pro","Proline"],["CCA","P","Pro","Proline"],["CCG","P","Pro","Proline"],["ACU","T","Thr","Threonine"],["ACC","T","Thr","Threonine"],["ACA","T","Thr","Threonine"],["ACG","T","Thr","Threonine"],["GCU","A","Ala","Alanine"],["GCC","A","Ala","Alanine"],["GCA","A","Ala","Alanine"],["GCG","A","Ala","Alanine"],["UAU","Y","Tyr","Tyrosine"],["UAC","Y","Tyr","Tyrosine"],["CAU","H","His","Histidine"],["CAC","H","His","Histidine"],["CAA","Q","Gln","Glutamine"],["CAG","Q","Gln","Glutamine"],["AAU","N","Asn","Asparagine"],["AAC","N","Asn","Asparagine"],["AAA","L","Lys","Lysine"],["AAG","L","Lys","Lysine"],["GAU","D","Asp","Aspartic acid"],["GAC","D","Asp","Aspartic acid"],["GAA","E","Glu","Glutamic acid"],["GAG","E","Glu","Glutamic acid"],["UGU","C","Cys","Cysteine"],["UGC","C","Cys","Cysteine"],["CGU","R","Arg","Arginine"],["CGC","R","Arg","Arginine"],["CGA","R","Arg","Arginine"],["CGG","R","Arg","Arginine"],["AGU","S","Ser","Serine"],["AGC","S","Ser","Serine"],["AGA","R","Arg","Arginine"],["AGG","R","Arg","Arginine"],["GGU","G","Gly","Glycine"],["GGC","G","Gly","Glycine"],["GGA","G","Gly","Glycine"],["GGG","G","Gly","Glycine"],["UAA","Stop","Stop","Stop"],["UAG","Stop","Stop","Stop"],["UGA","Stop","Stop","Stop"]]
    i = 0
    listaSplit = []
    cont = 1
    temp = ""
    while i < len(cadena):
        if cont <= 3:
            temp += cadena[i]
            cont += 1
            i += 1
        else:
            cont = 1
            listaSplit.append(temp)
            temp = ""
    listaSplit.append(temp)
    listaConv = []
    for tripleta in listaSplit:
        for datos in matriz:
            if datos[0] == tripleta:
                listaConv.append(datos[tipo])
    return listaConv

menuPrincipal()
        
