# # # # # # # # lista = []

# # # # # # # # lista.append(1)
# # # # # # # # lista.append(2)
# # # # # # # # lista.append(3)
# # # # # # # # print(lista)

# # # # # # # # lista.extend([5, 4])

# # # # # # # # print(lista)
# # # # # # # # lista.sort(reverse=True)
# # # # # # # # print(lista)

# # # # # # # # print(lista.pop())
# # # # # # # # print(lista)
# # # # # # # order = [1, 2, 3]
# # # # # # # first, second, third = order
# # # # # # # first, *second = order
# # # # # # # print(1 in order)
# # # # # # # print('a' in 'Abraham')
# # # # # # # slownik = {'jeden': 1, 'dwa': 2, 'trzy': 3}
# # # # # # # print('jeden' in slownik)
# # # # # # # print(1 in slownik.keys())
# # # # # # # slownik['cztery'] = 4
# # # # # # # print(slownik.keys())

# # # # # # k = (1)
# # # # # # k2 = (1,)

# # # # # # print(type(k))
# # # # # # print(type(k2))
# # # # # # print(k2)
# # # # # # print(len(k2))
# # # # # # czar = set('czabunagunga')
# # # # # # print(czar)
# # # # # # # {'u', 'a', 'z', 'b', 'n', 'g', 'c'}

# # # # # print(list(range(1, 8, 2)))
# # # # # print(list(range(0, -10, -2)))

# # # # # # zadanie 1

# # # # lista = list(range(1,21))
# # # # print(lista[:10]) # start 0, stop 10
# # # # print(lista[::-1]) # start 0, stop ostatni_element, step -1
# # # # print(lista[::2]) 

# # # miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

# # # slow = dict(zip(range(1, len(miesiace) + 1), miesiace))
# # # print(slow)

# # # print(list(zip(range(5), 'ABCDE')))
# # # print(list(zip(range(5), 'ABCD')))
# # # print(list(zip(range(4), 'ABCDE')))


# # # # lista_2 = [[1,2,3], [4,5,6]]
# # # # krotka_2 = ((1,2,3), (4,5,6))
# # # # slow_2 = {'pl':
# # # #           {1: 'styczeń',
# # # #            2: 'luty',}
# # # #           }

# # # # miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień']
# # # # indeksy = list(range(1, len(miesiace) + 1))

# # # # slow = dict(zip(indeksy, miesiace))
# # # # slow = dict(zip(range(1, len(miesiace) + 1), miesiace))
# # # # print(slow)




# # # from datetime import datetime, date

# # # print(datetime.now().month)
# # # print(datetime.now().timetuple())


# # slow = {}
# # print(slow.fromkeys('Marianna', 1))
# # print({}.fromkeys('Marianna', 1))
# # print(dict.fromkeys('Marianna', 1)) # statyczne
# # # 'A'.lower

# # class Osoba:

# #     # self.imie = ''

# #     def __init__(self, imie):
# #         self.imie = imie

# #     def wypisz_imie(self):
# #         return self.imie


# # print('A'.lower()) # wywołanie dla obiektu
# # print(str.lower('A')) # wywołanie dla klasy



# # lista = list(range(1, 11))
# # lista_kopia = lista.copy()

# # print(id(lista))
# # print(id(lista_kopia))


# # lista_kopia.sort(reverse=True)
# # print(lista)
# # print(lista_kopia)


# # liczba = 1
# # liczba2 = 1

# # print(id(liczba))
# # print(id(liczba2))
# # # 1884906127600
# # # 1884906127600
# # liczba2 = liczba2 + 1
# # print(id(liczba))
# # print(id(liczba2))

# lista = [list(range(5)), list(range(5, 10))]

# lista_kopia = lista.copy()

# print(lista)
# print(lista_kopia)

# print(id(lista))
# print(id(lista_kopia))
# # 2567776491520
# # 2567776660864

# lista[0][0] = 100
# print(lista)
# print(lista_kopia)

# print(id(lista[0]))
# print(id(lista_kopia[0]))

# import copy

# lista_kopia = copy.deepcopy(lista)
# lista[0][0] = 999
# print(lista)
# print(lista_kopia)

# zadanie 1
lista = list(range(1, 11))

lista2 = lista[5:]
lista = lista[:5]
print(lista, lista2)

# zadanie 2

polaczona = [0] + lista + lista2
print(polaczona)
posortowana = polaczona.copy()
posortowana.sort(reverse=True)
print(posortowana)

# zadanie 3

# wejscie = input()
# wejscie = set(input().lower())
# lista_liter = list(wejscie)
# lista_liter.sort()
# print(lista_liter)

# import this # manifest

# zadanie 4

months_pl = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
    }

# zadanie 5

months_en = ['January', 'February', 'March', 'April']

months_en = dict(zip(range(1, len(months_en) + 1), months_en))
print(months_en)


months = {
    'pl': months_pl,
    'en': months_en}

print(months['pl'][4])
print(months['en'][4])

# zadanie 6

slow = {}
print(slow.fromkeys('Marianna', 1))

# zadanie 7
import string

wejscie = input()

unikalne = set(wejscie.lower())
print(f'Liczba unikalnych liter: {len(unikalne)}')
print(f'pokrycie: {len(unikalne)}/{len(string.ascii_lowercase)}')
print(f'pokrycie %: {len(unikalne)/len(string.ascii_lowercase)*100:.2f} %')
