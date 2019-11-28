
class UsefulStaff:
    def __init__(self):
        print("I'm useful")


class Watch(UsefulStaff):
    def __init__(self):
        print("I can check what time is it")


class Phone(UsefulStaff):
    def __init__(self):
        print("I can call")


class SmartWatch(Watch, Phone):
    def __init__(self):
        print("I'm smartwatch")
        Watch.__init__(self)
        Phone.__init__(self)
        UsefulStaff.__init__(self)
        # super(Phone).__init__()
        # super(Watch).__init__()


u = UsefulStaff()
w = Watch()
p = Phone()
sw = SmartWatch()

