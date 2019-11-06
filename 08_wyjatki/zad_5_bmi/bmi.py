def bmi_calculator(weight, height):
    try:
        return round(weight / height ** 2, 3)
    except ValueError as e:
        print('Error: ', e)


def bmi_status(bmi):
    if bmi < 19:
        return 'severely_underweight'
    elif bmi < 25:
        return 'healthy'
    elif bmi < 30:
        return 'overweight'
    else:
        return 'severely_overweight'


def main():
    print('************************')
    result = bmi_calculator(80, 1.6)
    print(bmi_status(result))
    print('************************')


if __name__ == '__main__':
    main()



