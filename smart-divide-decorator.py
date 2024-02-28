def smartdivide(func):
    def inner(a,b):
        if b==0:
            print("Whoops, can't divide by zero.")
            return
        return func(a,b)
    return inner

@smartdivide
def divide(a,b):
    print(a/b)

divide(8,3)

# if @smartdivide not used for divide function
#myfunc = smartdivide(divide)
#myfunc(4,0)
