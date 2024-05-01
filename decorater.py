def decorater(func):
    def wrapper(message):
        print('-'*10)
        func(message)
        print('-'*10)
    return wrapper

@decorater                          #d = decorater(display)
def display(message):               #d()
    print(message)

display("welcome")