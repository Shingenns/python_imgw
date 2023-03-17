# # # # def dodaj(a, b):
# # # #     return a + b

# # # # # print(dodaj(1, 2))


# # # # def witaj(imie='Jan'):
# # # #     return f'Witaj {imie}!'

# # # # witaj()
# # # # print(witaj('Adam'))

# # # # def bez_return(parametr):
# # # #     # ustaw jakiś globalny parametr
# # # #     pass

# # # # print(bez_return('precisio'))



# # # # def rozdziel(imie_i_nazwisko):
# # # #     rozdzielone = imie_i_nazwisko.split()
# # # #     return rozdzielone[0], rozdzielone[1]


# # # # print(rozdziel('Jan Kowalski'))




# # # # def kwadrat(n=4):
# # # #     for i in range(n):
# # # #         # print(str(n) * n)
# # # #         print(f'{n}' * n)

# # # # kwadrat()
# # # # kwadrat(5)
# # # # kwadrat(9)

# # # def ciag(*liczby):
# # #     # jeżeli nie ma argumentów to
# # #     if len(liczby) == 0:
# # #         return 0.0
# # #     else:
# # #         suma = 0.0
# # #     # sumujemy elementy ciągu
# # #     for i in liczby:
# # #         suma += i
# # #     # zwracamy wartość sumy
# # #     return suma

# # # ciag(4, 5, 6)
# # # ciag(4, 5, 6, 7,8)
# # # ciag(4, 4)




# # # params = {'end': '', 'sep': '|'}
# # # print('jeden', 'dwa', **params)
# # # # czyli
# # # # print('jeden', 'dwa', 'end'='', 'sep'='|')
# # # params = {'end': ''}
# # # print('jeden', 'dwa', **params)


# # def policz_sume(lista: list[int]) -> int:
# #     return sum(lista)

# # print(policz_sume([1,2,3]))


# # class Osoba:
# #     pass

# # o = Osoba()
# # o.imie = 'Jan'
# # o.nazwisko = 'Kowalski'

# # print(o.__dict__)

# def licz_punkty(**dane):
#     # dane to slownik
#     # policzyć sumę z wartości slownika
#     return sum(dane.values())

# print(licz_punkty(FcBarcelona=10, RealMadryt=5))

import pakiet.moj_modul as moj_modul

# mm.kwadrat(5)
# kwadrat(5)