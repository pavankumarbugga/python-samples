# def f1():
#     print("Called f1")

# def f2(f):
#     f()

# print(f1)
# f2(f1)

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

# Avoids declaring this --> f = f1(f)
@f1         
def f():
    print("Hello")

# f = f1(f)
f()