# Factorial of a number
a=input("Enter a number: ")
a=int(a)
def fact(n):

    if n<2:
        return 1
    else:
        return n*(fact(n-1))

result=fact(a)
a=str(a)
result=str(result)
print('Factorial of '+ a +' is: '+result)
