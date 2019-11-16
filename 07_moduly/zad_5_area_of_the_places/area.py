import figures

def main():
    figures_list = []

    while True:
        answer = input('Podaj figury, z jakich sklada sie pomieszczenie: '
                       'trojkat, prostokat, kwadrat, rownoleglobok, romb, trapez, kolo, ')
        figures_list.append(answer)
        if answer == 'quit':
            return False


if __name__ == '__main__':
    main()


for figure in figures_list:
    if figure == 'triangle':
        figures.triangle(float(input('Podaj podstawe: ')), float(input('Podaj wysokosc: ')))
    if figure == 'square':
        figures.square(float(input('Podaj podstawe: '))
    # if figure == 'rectangle':
    #     figures.rectangle(float(input('Podaj podstawe: ')), float(input('Podaj wysokosc: ')))
    # if figure == 'parallelogram':
    #     figures.parallelogram(float(input('Podaj podstawe: ')), float(input('Podaj wysokosc: ')))
    # if figure == 'diamond':
    #         figures.diamond(float(input('Podaj podstawe: ')), float(input('Podaj wysokosc: ')))
