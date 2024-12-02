def numeros_repetidos(numeros: list[int]):
    a = set()

    for num in numeros:
        if num not in a:
            a.add(num)
        else:
            return True
        
    
    return False


print(numeros_repetidos([1,2,3,4,5,6,7]))
        

