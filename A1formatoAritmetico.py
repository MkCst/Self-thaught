import re
# Segunda solucion usando expresiones regulares
def formato_aritmetico(problemas, display=False):
    if len(problemas) > 5:
        return "Error: Too many problems."

    # Definicion de lineas
    primera = ""
    segunda = ""
    separador = ""
    respuesta = ""
    cadena = ""
    for problema in problemas:
        # Condicion: Es un numero
        if(re.search("[^\s0-9.+-]", problema)):
            # Condicion: Pertimir solo suma y resta
            if(re.search("[/]", problema) or re.search("[*]", problema)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        # Operadores
        primer_num = problema.split(" ")[0]
        operador = problema.split(" ")[1]
        segundo_num = problema.split(" ")[2]
        # Condicion: Numeros menores a 5 digitos
        if(len(primer_num) >= 5 or len(segundo_num) >= 5):
            return "Error: Numbers cannot be more than four digits."

        res = ""
        if(operador == "+"):
            res = str(int(primer_num) + int(segundo_num))
        elif(operador == "-"):
            res = str(int(primer_num) - int(segundo_num))

        length = max(len(primer_num), len(segundo_num)) + 2
        arg_prmro = str(primer_num).rjust(length)
        arg_sgndo = operador + str(segundo_num).rjust(length - 1)
        resultado = str(res).rjust(length)
        line = ""
        for _ in range(length):
            line += "-"

        # Construccion con sus determinadas lineas
        # Fin del arreglo ?
        if problema != problemas[-1]:  # es el ultimo elemento
            primera += arg_prmro + "    "
            segunda += arg_sgndo + "    "
            separador += line + "    "
            respuesta += resultado + "    "
        else:
            primera += arg_prmro
            segunda += arg_sgndo
            separador += line
            respuesta += resultado

    if display:
        cadena = primera + "\n" + segunda + "\n" + separador + "\n" + respuesta
    else:
        cadena = primera + "\n" + segunda + "\n" + separador
    return cadena


problemas = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
var = formato_aritmetico(problemas, True)
print(problemas)
print(var)
