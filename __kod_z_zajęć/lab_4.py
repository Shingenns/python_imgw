# # # moduł 4
# # # zadanie 1

# # # zdanie = input('Wpisz dowolne zdanie:\n')
# # # print(f'W zdaniu jest/są {zdanie.count(" ")} spacje/-i')

# # # zadanie 2
# # import sys

# # # liczba_1 = sys.stdin.readline()
# # # liczba_2 = sys.stdin.readline()

# # # sys.stdout.write(str(int(liczba_1) * int(liczba_2)))

# # wersja skrócona, ale mniej czytelna
# # # sys.stdout.write(str(int(sys.stdin.readline()) * int(sys.stdin.readline())))

# # # zadanie 3
# # # a = int(input())
# # # b = int(input())
# # # c = int(input())
# # # lub przez rozpakowanie krotki (tuple unpacking)
# # # a, b, c = int(input()), int(input()), int(input())

# # # if a in range(1, 11) and (a > b or b > c):
# # #     print('Wszystkie warunki sa spełnione.')
# # # else:
# # #     print('Warunki nie zostały spełnione.')


# # # zadanie 4
# # # 50 iteracji
# # for i in range(0, 51):
# #     if i % 5 == 0:
# #         print(i)

# # # 11 iteracji
# # for i in range(0, 51, 5):
# #     print(i)


# # # zadanie 5
# # # Napisz pętle (while), która pobiera liczby od użytkownika i wyświetla ich
# # #  kwadraty na ekranie. Liczby pobierane są w postaci oddzielonej spacjami. 
# # # Pętla kończy działanie po wpisaniu słowa quit.

# # # # krok 1 - pętla while
# # # while True:
# # #     # krok 2 - pobierz wejście przez input
# # #     wejscie = input('Wpisz liczby oddzielnone spacjami:\n')
# # #     # krok 3 - jeżeli wejście to quit - przerwij pętle (zakończ skrypt)

# # #     if wejscie == 'quit':
# # #         break
# # #     else:
# # #         # w przeciwnym wypadku wyświetl kwadraty pobranych liczb
# # #         # przykład wejścia: 1 2 334
# # #         lista_liczb = wejscie.split(' ')
# # #         # pętla for w postaci pętli for each
# # #         for liczba in lista_liczb:
# # #             print(int(liczba) ** 2)

# # # for i in range(len(lista_liczb)):
# # # pętla for ala c++ style
# # # for(int i=0;i<10;i++){
# # #     zrób coś
# # # }

# # # for lokalna_zmienna in obiekt_iterowalny (np. str, list, tuple, dict, set, range()):
# # #     # zrób coś
# # #     pass


# # # lista = [[1,2,3], [4,5,6]]
# # # for elem in lista:
# # #     print(elem) # [1,2,3] przy pierwszej iteracji
# # #     print(elem) # [4,5,6] przy drugiej iteracji


# # # zadanie 6

# # # Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Liczby dodajemy do momentu wpisania słowa 'stop' zamiast liczby. Wykorzystaj pętle while.
# # # lista = []
# # # import string

# # # while True:
# # #     wejscie = input()
# # #     sprawdzenie czy zmienna wejście zawiera tylo cyfry i nie zawiera
# # #     znaków niedrukowalnych
# # #     if not wejscie.isdigit() and wejscie not in string.whitespace:
# # #         break
# # #     dodajemy element do listy
# # #     lista.append(wejscie)

# # # print(lista)

# # # zadanie 7
# # liczba = input('Wpisz liczbę\n')

# # i = 0
# # suma = 0
# # while i < len(liczba):
# #     suma = suma + int(liczba[i])
# #     i += 1

# # print(suma)

# # # z pętlą for
# # for cyfra in liczba:
# #     suma += int(cyfra)

# # # zadanie 8
# # wysokosc = int(input('Podaj wysokość < 10\n'))

# # if wysokosc <= 10:
# #     # rysuj wieżę
# #     for w in range(1, wysokosc+1):
# #         print('A' * w)

# # zadanie 9
# # krok 1 - wypisanie etykiet w pierwszym wierszu
# # print('  ', end='')
# # for etykieta in range(1, 11):
# #     print(f'{etykieta:>4}', end='')
# # print()
# # # krok 2 - wypisać mnożenie w pierwszym wierszu
# # for wiersz in range(1, 11):
# #     # etykieta w wierszu
# #     print(f'{wiersz:>2}', end='')
# #     for kolumna in range(1, 11):
# #         print(f'{wiersz * kolumna:>4}', end='')
# #     print()

# # zadanie 10
# w = int(input())

# if w in range(3, 9+1, 2):
#     for i in range(1, w + 1, 2):
#         print(f'{"o" * i:^{w}}')
#     for i in range(w - 2, 0, -2):
#         print(f'{"o" * i:^{w}}')

# # lub troszkę krócej
# if w in range(3, 9+1, 2):
#     for i in list(range(1, w + 1, 2)) + list(range(w - 2, 0, -2)):
#         print(f'{"o" * i:^{w}}')


# print('\u201F')
# print('\u1000')

# print([f'{x:_>5}' for x in range(5)])

# lista = [
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
#     [1, 2, 3, 4],
# ]
# print(lista[2][2])

# import random

# macierz = [[random.random() for _ in range(4)] for _ in range(4)]
# print(macierz)

# for wiersz in macierz:
#     print(wiersz)

# print([macierz[i][i] for i in range(len(macierz))])
# import math
# import random

# f = filter(lambda x: math.sqrt(x) > 2, [random.randint(1, 10) for _ in range(5)])
# print(list(f))

produkty = {
    'jaja': 'szt',
    'ziemniaki': 'kg',
    'cukier': 'kg',
    'jabłko': 'kg',
    'arbuz': 'szt'
}
# lista = []
# for key, value in produkty.items():
#     if value == 'szt':
#         lista.append(key)

lista = [key for key, value in produkty.items() if value == 'szt']
print()
