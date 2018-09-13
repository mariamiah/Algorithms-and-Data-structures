lista = [7, 5, 6, 'a', 't', 'y', 5, 6, 64, 'h', 'u', 'o', 'p', 4, 5, 7, 19, 't']


def list_sort(lista):
    if type(lista) == int:
        return "Invalid Input"
    if type(lista) == str:
        return "Invalid Input"
    evens = [i for i in lista if type(i) == int and i%2 == 0]
    evens.sort()
    odds = [i for i in lista if type(i) == int and i%2 == 1]
    odds.sort()
    chars = [i for i in lista if type(i) == str]
    chars.sort() 
    return {'evens': evens, 'odds': odds, 'chars': chars}
            
print(list_sort(lista))


