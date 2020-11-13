# Algoritmos de ordenamiento

## Bubble sort
    # Algoritmo de ordenamiento Burbuja
    
    from random import randint
    
    def burbuja(lista):
        size = len(lista) 
        
        for i in range(size):
            for j in range(size - i -1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1]= lista[j + 1], lista[j]
        return lista
    
    
    if __name__ == "__main__":
        size_list= int(input("Tamaño de la lista: "))
        lista = [randint(1,500) for _ in range(size_list)]
        
        print("lista original:")
        print(lista)
        lista = burbuja(lista)
        print("Lista ordenada")
        print(lista)







