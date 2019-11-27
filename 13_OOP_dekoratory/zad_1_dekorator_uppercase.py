def uppercase_decorator(func_text):
    def upper_text():
        text = func_text()
        text = text.upper()
        return text
    return upper_text

@uppercase_decorator
def text_giver():
    return 'Zwracam text'


print(text_giver())
