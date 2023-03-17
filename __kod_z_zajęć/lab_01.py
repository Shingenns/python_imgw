# # # print('Witaj')

# # # # dodanie komentarza Ctrl + /
# # # liczba = 1
# # # print(type(liczba))
# # # liczba = 'Ala'
# # # print(type(liczba))
# # # liczba = 0.0
# # # print(type(liczba))
# # # # <class 'int'>
# # # # <class 'str'>
# # # # <class 'float'>

# # # liczba = 1
# # # liczba = int(1)
# # # liczba = int('1') # rzutowanie typów (zamiana)
# # # liczba = int('1sfsdfs')

# # # print((0.1 + 0.2) == 0.3)

# print(f'{0.1:.32}')




# # imie = 'Abraham'
# # print(imie[0])
# # print(imie[-1]) # ostatni element
# # # imie[0] = 'a' błąd!
# # # imie = imie.lower()
# # print(imie.count('a')) # Python jest case sensitive (cs)
# # print(imie[1].islower())
# # print(imie.index('k'))
# # print(imie.find('k'))

# # lancuch = """
# # hgshd
# # dfsdfsd

# # sdfsdfsd
# # """

# # sciezka = 'Recenzja \'Wladcy Pierścieni\''





# # def funkcja():
# #     """
# #     funkcja, która zwraca nic
# #     """
# #     pass


# # wycinki - ang. slice
# imie = 'Abraham'
# print(imie[0:2]) # start=0, stop=2
# print(imie[2:4])

# print(imie[2::2])
# print(imie[::2]) 

# print(imie[::-2]) 
# print(type(imie[::-2]))
# print(imie[0:5] + imie[-1]) # konkatenacja (złączanie)
# print(str(1) + imie[0])
# print(1)
# print('\n\n')
# print(1,1,1, end='', sep='|') # 1|1|111
# print(1, end='')
# print(1, end='')
# print(1,1,2, sep='|')

# print(str(5))
# print(5)
# print(int(5).__str__())
# print(print)
# sentence = input('Wpisz dowolne zdanie:\n')
# sentence = sentence.strip()
# sentence = sentence.lstrip()
# sentence = sentence.rstrip()
# sep = input('Podaj separator:\n')
# words = sentence.split(sep)
# print(words)
# Ctrl + / - dodanie komentarza/usunięcie komentarza
# sentence = sentence.replace(',', ';')
# print(sentence)

# num = input('Wpisz dowolną liczbę:\n')
# print('Czy liczba jest liczbą całkowitą? -> ', num.isdigit())
# # 7 - jak wprowadzone zostaną instrukcje warunkowe i pętle to będzie łatwiej :)
# # sprawdzimy, czy wartość była podana jako docelowy float (separator . )
# print('Czy liczba jest liczbą zmiennoprzecinkową? -> ', num.replace('.','',1).isdigit())
# print(num.zfill(5))


print('{:>10}'.format('100'))
print(f'{"100":>10}')

from datetime import datetime
print(datetime.now())
# 1. wypisać tylko datę
# 2. wypisać datę i czas z zaokrągleniem do 10 minut
teraz = datetime.now()
print(f'{teraz.year: >10}')
print(dir(teraz))

# 3. Pobierz dowolną liczbę poprzez funkcję input i sformatuj
# ją do postaci wyrównującej ją do strony prawej na liczbie
# pozycji dłuższej o 2 niż liczba cyfr pobranej liczby 
# uzupełniona znakami _ np.
# wprowadzona liczba to 1, wypisana to __  1 
# wprowadzona liczba to 123, wypisana to __  123
# wprowadzona liczba to 5555, wypisana to __  5555

# len('Ala') # ilość znaków (dla typu str)
liczba = input('Podaj liczbę:\n')
print(f'{liczba:_>5.{len(liczba)}f}')




