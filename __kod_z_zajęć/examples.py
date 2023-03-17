# przykłady wykorzystania wybranych funkcji wbudowanych
import math

# filter
# odfiltrowanie elementów zbioru iterowalnego spełniającego
# dany warunek
print('*' * 5, 'filter', '*' * 5)
lista = list(range(1, 11))
print(list(filter(lambda x: x > 5, lista)))

def is_one_digit_number(num: int):
    return len(str(num)) < 2

print(list(filter(is_one_digit_number, lista)))

# sorted - sortowanie obiektu iterowalnego
print('*' * 5, 'sorted', '*' * 5)
print(sorted(lista))
print(sorted(lista, key=lambda x: x % 2 == 0))

# map - wykonanie funkcji na elementach obiektu iterowalnego
print('*' * 5, 'map', '*' * 5)
# z użyciem funkcji anonnimowej
power = map(lambda x: math.pow(x, 2), lista)
# z użyciem istniejącej funkcji
lancuch = map(str, lista)
print(list(power))
print(list(lancuch))

# bin, int, oct, hex
# jest to klasa pozwalająca na zapis liczby całkowitej w formie binarnej
print('*' * 5, 'bin, int, oct, hex', '*' * 5)
print(bin(10))


# int - inna podstawa
print(int('10', 2))
print(int('655', 8))
print(int('FF', 16))

liczba = 10
print(f'{liczba} szesnastkowo to: {hex(liczba)}')
print(f'{liczba} ósemkowo to: {oct(liczba)}')
print(f'{liczba} binarnie to: {bin(liczba)}')

# reversed
print(list(reversed(lista)))
print(list(reversed('piąteczek')))
print(list(reversed('kajak')))

anagram = 'kajak'

if anagram == ''.join(reversed(anagram)):
    print(f'{anagram} to anagram!')