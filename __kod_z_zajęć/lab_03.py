
# # # lista = list('abracadabra')


# # # for i in enumerate(lista):
# # #     # print(f'{index}: {value}') # jeżeli rozpakuję krotkę
# # #     print(f'{i[0]}: {i[1]}') # bez rozpakowania



# # imie = 'Zbyszek'

# # for litera in imie:
# #     print(litera)

# # # 1. zwrówcenie iteratora dla podanego obiektu
# # it = iter(imie)
# # # wywoływanie metody next() dopóki nie zostanie zgłoszony
# # # wyjątek StopIteration
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # # lub (ale lepiej nie)
# # print(it.__next__())

# import sys

# print("Podaj jakiś tekst")
# s = sys.stdin.readline() # Wczytuje wiersz
# print("Twój tekst to: " + s)
# # Do wydruku można użyć też komendy write np.
# sys.stdout.write(s)

# print(list(s)) # tu widać znak nowej linii na końcu (\n)
# inp = input()
# print(list(inp)) # input nie dodaje tego znaku

params = {'end': '', 'sep': '|'}
print('jeden', 'dwa', **params)

try: 
    with open('plik.txt', 'r', encoding='utf-8') as file_reader: 
        for linia in file_reader: 
            print(linia, end='') 
except OSError as er: 
    print(f'Wystąpił wyjątek OSError: {er}')


number = 1_000_000
print(number)
print(type(number))
