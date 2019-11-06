# numbers = input('Give me a few numbers, put comma between: ')
# numbers = numbers.split(',')
#
# # def if_number():
# #     for number in numbers:
# #         if not number.isalnum():
#
# print(numbers)
#
#
#
# aver = 0
# for number in numbers:
#     aver += int(number)
#
# print(numbers)
# aver = aver/len(numbers)
# print(aver)


# numbers = input('Give me a few numbers, put comma between: ')
# numbers = numbers.split(',')
# print(numbers)

# numbers_as_float = []
# for i in numbers:
#     numbers_as_float.append(float(i))
#
# print(numbers_as_float)

# numbers = input('Give me a few numbers, put comma between: ')
# numbers = numbers.split(',')
# print(numbers)
#
# for index in range(len(numbers)):
#     numbers[index] = float(numbers[index])
# print(numbers)

numbers = input('Give me a few numbers, put comma between: ')
numbers = numbers.split(',')
print(numbers)

list_exceptions = []
for index, element in enumerate(numbers):
    # print(index, ':', element)
    try:
        numbers[index] = float(element)
    except (ValueError, TypeError) as e:
        print(e)
        list_exceptions.append(e)
        # numbers[index] = 0
        # del numbers[index]
        numbers[index] = '-'
print(numbers)

while '-' in numbers:
    numbers.remove('-')
print(numbers)

try:
    avg = sum(numbers)/len(numbers)
except (ValueError, TypeError) as e:
    print('error: ', e)
    avg = sum(numbers)/len(numbers)
print(avg)

print(list_exceptions)

with open('errors.txt', 'w') as f:
    f.write('Ha mamy bledy!\n')
    for i in list_exceptions:
        f.write(str(i) + '\n')


# with open('errors.txt', 'w') as f:
#     f.write('\n'.join(list_exceptions))


# def is_number(numbers):
#     for number in numbers:
#         if not number.isalnum():
#             print("not number")
#             raise ValueError
#
#
# is_number(numbers)