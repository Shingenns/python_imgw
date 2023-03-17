def kwadrat(n=4):
    for i in range(n):
        print(f'{n}' * n)


def licz_punkty(**dane):
    return sum(dane.values())


def main():
    # np. kod testujący
    kwadrat(5)
    print(licz_punkty(FcBarcelona=10, RealMadryt=5))


if __name__ == '__main__':
    main()
