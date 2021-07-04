# Primera solucion
def formato_aritmetico(problemas, display=False):
    lst = []
    max_length = []
    required_length = []

    # Construccion lista de operaciones
    for i in range(len(problemas)):
        lst.append(problemas[i].split(" "))
    #print(lst)

    # Condiciones
    if len(lst) > 5:
        """Mas problemas de los permitidos"""
        return "Error: Too many problems."

    for i in range(len(lst)):
        if (len(lst[i]) != 3):
            return "Error: Expression must only contain 2 operands and 1 operator."
        if lst[i][1] != '+' and lst[i][1] != '-':
            return "Error: Operator must be '+' or '-'."

        try:  # Conversion de numeros a enteros
            lst[i][0] = int(lst[i][0])
            lst[i][2] = int(lst[i][2])
        except:
            return "Error: Numbers must only contain digits"

        # Longitud maxima de la maxima expresion
        max_length.append(
            max(len(str(lst[i][0])), len(str(lst[i][2])))
        )
        required_length.append(int(max_length[i]) + 2)

        if lst[i][0] > 9999 or lst[i][2] > 9999:
            return "Error: Numbers cannot be more than four digits."

        arranged_problems = ""

    # Primera linea
    for i in range(len(lst)):
        space_required = required_length[i] - len(str(lst[i][0]))
        for _ in range(space_required):
            arranged_problems += " "
        arranged_problems += str(lst[i][0]) + "  "
    arranged_problems = arranged_problems.rstrip()
    arranged_problems += "\n"

    #print(arranged_problems)
    # Segunda linea
    for i in range(len())
    

    
problemas = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formato_aritmetico(problemas)
