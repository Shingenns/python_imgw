# zadanie 3


def top_n(liczby: list[int|float], n=1) -> list[int|float]:
    return sorted(liczby)[:-n-1:-1]


print(top_n(list(range(1, 11)), 4))


# zadanie 4

def group_types(lista: list):
    output = {}
    for obj in lista:
        name = obj.__class__.__name__
        if name in output:
            output[name].append(obj)
        else:
            output[name] = [obj]

    return output


def generuj_email(nazwisko: str, domena: str) -> str:
    # pozbywamy się polskich ogonków
    nazwisko = unidecode(nazwisko)
    return f"{nazwisko.replace(' ', '.').lower()}@{domena}"

# zadanie 12
def kolo_fortuny():
    from czwartek import parser
    import random

    def zamien(haslo: list[str]):
        zakodowane = []
        for letter in haslo:
            if letter != ' ':
                zakodowane.append('_')
            else:
                zakodowane.append(' ')
        return zakodowane

    # losujemy jedną wartość z listy
    lista = ['Hasło 1', 'Hasło 2', 'Hasło 3']
    haslo = list(random.sample(lista, 1)[0])
    zakryte = zamien(haslo)
    # wypisujemy zakrytą wersję
    while True:
        podana_litera = input('Podaj literę do odgadnięcia\n')[0]
        for i in range(len(haslo)):
            if haslo[i] == podana_litera:
                zakryte[i] = podana_litera
        print(''.join(zakryte))


if __name__ == '__main__':
    # mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0, print]
    # print(group_types(mieszana))

# kod wykorzystujący moduł timeit, którym możemy zmierzyć czas wykonania
# wybranego fragmentu kodu
#     from timeit import timeit


#     stmt1 = """
# lista = []
# for i in range(1000):
#     lista.append(i)
#     """
#     stmt2 = """lista = list(range(1000))"""
#     stmt3 = """[i for i in range(1000)]"""

#     print(timeit(stmt1, number=10000))
#     print(timeit(stmt2, number=10000))
#     print(timeit(stmt3, number=10000))

    # from unidecode import unidecode

    # # print(unidecode('zażółć gęślą jaźń'))
    # print(generuj_email('Jan Kowalski', 'imgw.pl'))

    kolo_fortuny()
