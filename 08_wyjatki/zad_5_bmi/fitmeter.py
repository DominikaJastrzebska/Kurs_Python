import bmi


def advice(filename):
    with open(filename + '.txt') as f:
        content = f.read()
    print(content)


def main():
    try:
        w = float(input('Give me your weight [kg]: '))
    except ValueError as e:
        print('Err1', e)
        w = 0
    try:
        h = float(input('Give me your height [m]: '))
    except ValueError as e:
        print('Err2', e)
        h = 1

    bmi_result = bmi.bmi_calculator(w, h)
    bmi_stan = bmi.bmi_status(bmi_result)
    print('BMI status: ', bmi_stan)
    advice(bmi_stan)


if __name__ == '__main__':
    main()