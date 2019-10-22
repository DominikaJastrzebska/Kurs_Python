# def mood():
#     print('How are you?')
#
# mood()
#
# def my_mood(answer):
#     print('My mood today: ')
#     print(answer)
#
# resp = input('How are you? ')
# my_mood(resp)

def my_mood(answer):
    return answer * 2

resp = input('How are you? ')
twiced = my_mood(resp)              #przypisanie funkcji do zmiennej
print('My mood is like', twiced)