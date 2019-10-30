import bmi

def advice(filename):
    with open(filename + '.txt') as f:
        content = f.read()
    print(content)


def main():
    w = float(input('Give me your weight [kg]: '))
    h = float(input('Give me your height [m]: '))
    bmi_result = bmi.bmi_calculator(w, h)
    bmi_stan = bmi.bmi_status(bmi_result)
    print('BMI status: ', bmi_stan)
    advice(bmi_stan)


if __name__ == '__main__':
    main()