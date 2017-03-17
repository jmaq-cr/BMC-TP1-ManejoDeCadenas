#Tecnológico de Costa Rica, Sede Cartago
#Escuela de Ingeniería en Computación
#Introducción a la Biología Molecular Computacional
#Tarea Programada #1
#Estudiantes
#   Jose Manuel Aguilar Quesada
#   Crisia Piedra Chavez
#Primer Semestre, 2017

from random import randint

#Del punto 4.a
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
    if posicion < 1 or posición >= len(cadena):
        print("Fuera de rango")
        return ""
    else:
        return cadena[posicion-1]

def esSubsecuencia(cadenaMayor,cadenaMenor):
    pos = 0
    for i in cadenaMayor:
        if i == cadenaMenor[pos]:
            if pos < len(cadenaMenor)-1:
                pos = pos + 1
            else:
                return True
    return False

def esSupersecuencia(cadenaMayor,cadenaMenor):
    pos = 0
    for i in cadenaMayor:
        if i == cadenaMenor[pos]:
            if pos < len(cadenaMenor)-1:
                pos = pos + 1
            else:
                return True
    return False

def esSubstring(cadenaMayor,cadenaMenor):
    return(cadenaMenor in cadenaMayor)

def esSuperstring(cadenaMayor,cadenaMenor):
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
        
