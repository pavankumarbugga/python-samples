def greet(name):
    print("Hello ", name)

def smart(func):
    def inner(name):
        for i in range(1,3):
            #print("Hello ", name)
            func(name)
        #return func(name)
    return inner

greet = smart(greet)
greet("Pavan Kumar")