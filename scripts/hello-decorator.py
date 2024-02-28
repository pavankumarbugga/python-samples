def say_twice(name):
    print("Hello ", name)

def smart(func):
    def inner(name):
        for i in range(1,2):
            print("Hello ", name)
        return func(name)
    return inner

say_twice = smart(say_twice)
say_twice("Pavan Kumar")