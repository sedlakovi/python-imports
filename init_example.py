print('Initializing module', __name__)


def func1():
    print('I can call', func2)


def func2():
    print('I can call', func1)


if __name__ == '__main__':
    print('I\'m the main!')
    func1()
    func2()
