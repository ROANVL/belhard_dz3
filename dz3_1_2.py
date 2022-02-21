#калькулятор гипотенузы и площади нескольких треугольников
class NonNumericError(Exception):
    pass
class InconsistentDataError(Exception):
    pass
class MinusValueError(Exception):
    pass

def split_array(str):
    return str.split(' ')

def compare_length(array):
    is_equal =  len(array) % 2 
    if is_equal == 1:
        raise InconsistentDataError
    return is_equal

def array_int(array):
    in_array = []
    for i in array:
        if i.lstrip('-').isnumeric() != True:
            raise NonNumericError
        a = int(i)
        in_array.append(a)
    return in_array

def minus(array):
    for i in array:
        if i <= 0:
            raise MinusValueError

try:
    cathets_a_string = input("Введите первые катеты: ")
    
    cathets_a_split = split_array(cathets_a_string)
   
    cathets_a_int = array_int(cathets_a_split)
    
    cathets_a = []
    cathets_b = []
    for i in cathets_a_int[0 : len(cathets_a_int) : 2]:
        cathets_a.append(i)
    for i in cathets_a_int[1 : len(cathets_a_int) : 2]:
        cathets_b.append(i)
    
    compare_length(cathets_a_int)
    minus(cathets_a_int)
       
    hypotenuse = []
    square_triangle = []

    range_len = len(cathets_a)

    for i in range(range_len):
        hypotenuse.append(round((int(cathets_a[i])**2 + int(cathets_b[i])**2)**0.5, 2))

    for i in range(range_len):
        square_triangle.append(round((int(cathets_a[i]) * int(cathets_b[i]))/2, 2))

    for i in range(range_len):
        print(f'Треугольник {i+1} с катетами {cathets_a[i]} и {cathets_b[i]} имеет площадь {square_triangle[i]} и гипотенузу {hypotenuse[i]}')
    
    print('Программа выполнена успешно!!!')

except NonNumericError:
    print("Вы ввели не число")
except InconsistentDataError:
    print("Массивы имеют разную длинну")
except MinusValueError:
    print("Вы ввели значение меньше нуля")










