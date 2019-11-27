def example_function():  # taka funkcja to jest domkniecie, te dwie funkcje razem
    a = 7

    def nested_function(age):
        print('Jestem w środku zagnieżdżenia')
        return a * age

    return nested_function


new_function = example_function()  # nested function
print(new_function(20))


def closure():
    a = 'closure'

    def nested(b):
        return a * b

    return nested


new_function = closure()
print(new_function(4))