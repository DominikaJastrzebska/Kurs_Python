
class Shop:

    def __init__(self, name, address, product):
        self.name = name
        self.address = address
        self.product = product

    def see(self):
        product = {
            'clothes': ['skirt', 'trousers', 'shirt', 'shoes'],
            'food': ['milk', 'cheese', 'apple', 'banana']
            'bookstore': ['books', 'paper', 'crayons']
        }
        question = input('What type of product do You want to see? C - clothes, F - food, B - bookstore ')
        if question.upper() == 'C':
            return product['clothes']
        elif question.upper() == 'F':
            return product['food']
        elif question.upper() == 'B':
            return product['bookstore']
        else:
            print('Put correct letter')

    def try_on(self):
        pass

    def buy(self):
        pass

    def give_back(self):
        pass
