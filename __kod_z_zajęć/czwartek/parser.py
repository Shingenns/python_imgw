from datetime import datetime


def otworz_plik_csv(sciezka: str, separator: str = ',') -> list[list[str]]:
    """otwieramy plik csv"""
    zawartosc_pliku = []

    try: 
        with open(sciezka, 'r', encoding='utf-8', errors='ignore') as file_reader: 
            for linia in file_reader: 
                zawartosc_pliku.append(linia.split(separator)) 
    except OSError as er:
        print(f'Wystąpił wyjątek OSError: {er}')

    return zawartosc_pliku


def zapisz_dane_do_pliku(sciezka: str, dane: list[list[str]], sep=','):
    try:
        with open(sciezka, 'w', encoding='utf-8') as file_writer:
            # można przenieść do comprehension
            for wiersz in dane:
                file_writer.write(f'{sep}'.join([f'{elem}' for elem in wiersz]) + '\n')
    except OSError as er:
        print(f'Wystąpił wyjątek OSError: {er}')


def get_float_from_str(text: str, sep: str = '.') -> float:
    f = ''.join([z for z in text if z.isdigit() or z == sep]).replace(sep, '.')
    return float(f)


if __name__ == '__main__':
    plik = otworz_plik_csv('zamowienia.csv', separator=';')
    # oczyszczanie danych
    for wiersz in plik[1:]:
        wiersz[4] = get_float_from_str(wiersz[4], ',')
        wiersz[2] = datetime.strptime(wiersz[2], '%d.%m.%Y').strftime('%Y-%m-%d')

    # podzielenie zbioru na dwie części
    # w "kolumnie" kraj to Polska lub Niemcy
    # polska = []
    # niemcy = []
    # for wiersz in plik[1:]:
    #     if wiersz[0] == 'Polska':
    #         polska.append(wiersz)
    #     elif wiersz[0] == 'Niemcy':
    #         niemcy.append(wiersz)
    # jako comprehension
    # polska = [wiersz for wiersz in plik[1:] if wiersz[0] == 'Polska']
    # niemcy = [wiersz for wiersz in plik[1:] if wiersz[0] == 'Niemcy']

    # zapisanie danych do plików
    # zapisz_dane_do_pliku('zamowienia_polska.csv', polska)
    # zapisz_dane_do_pliku('zamowienia_niemcy.csv', niemcy)


    # krok 1 - jakich informacji potrzebuję?
    # zbiór unikalnych wartości z kolumny kraj
    dane = {}
    for wiersz in plik[1:]:
        # jeżeli klucz jest już w słowniku
        if wiersz[0] in dane.keys():
            dane[wiersz[0]].append(wiersz)
        # lub jeżeli tego klucza nie ma w słowniku
        else:
            dane[wiersz[0]] = [wiersz]
    
    # zapisujemy dane ze słownika do odpowiednich plików
    for klucz in dane:
        zapisz_dane_do_pliku(f'zamowienia_{klucz.lower()}.csv', dane[klucz])


    # docelowa struktura słownika
    # dane = {
    #     'Polska': [
    #         ['Polska', 'Kowalski', '2005-04-29', '11043', 210.00]
    #     ]
    # }


    # from tqdm import tqdm
    # import math

    # for i in tqdm(range(10_000_000)):
    #     math.sqrt(i)
