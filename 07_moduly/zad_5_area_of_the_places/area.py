import figures

def main():
    figures_list = []

    while True:
        answer = input('Podaj figury, z jakich sklada sie pomieszczenie: ')
        figures_list.append(answer)
        if answer == 'quit':
            return False


if __name__ == '__main__':
    main()


for figure in figures_list:
    if figure == 'triangle':
        figures.triangle(float(input('Podaj podstawe: ')), float(input('Podaj wysokosc: ')))
    if figure == 'kwadrat':
        figures.square(float(input('Podaj podstawe: '))
