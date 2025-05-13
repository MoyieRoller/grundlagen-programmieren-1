class MyClass:

    def __init__(self):
        self.__some_int = 0   # das soll immer ein integer sein... (warum auch immer...)

    @property
    def some_int(self):
        """Getter-Methode für some_int"""
        return self.__some_int

    @some_int.setter
    def some_int(self, value):
        """Setter-Methode für some_int"""
        print('Setter aufgerufen... böööööööh!')
        if isinstance(value, int):
            self.__some_int = value

if __name__ == '__main__':

    myClass = MyClass()
    print(myClass.__dict__)
    print(myClass._MyClass__some_int)
    # print(myClass.some_int)
    # myClass.some_int = 5
    # print(myClass.some_int)
    # myClass.some_int = 'fuenf'
    # print(myClass.some_int)
    # myClass.__some_int = 'vier'
    # print(myClass.__some_int)
    # print(myClass.some_int)

    myClass.some_int = 5
    print(myClass.__some_int)
    myClass.__some_int = 'vier'
    print(myClass.__some_int)
    print(myClass.some_int)

    print(myClass.__dict__)