
slots = 2

def toaster(ingredient):
    global slots
    slots = 3
    for i in range(0,len(ingredient)):
        if i > (slots - 1):
            return ingredient
        
        if ingredient[i] == "bread":
            ingredient[i] = "toast"
    

    return ingredient
    


loaf = ["bread", "bread","bread","ham","banana", "bread","bread","ham"]

print(toaster(loaf))
print(f"slots: {slots}")


##a = 10
##b = 99
##
##def mathsomething(num1, num2):
##    a = num2
##    b = num1
##
##    print(f"a inside function {a}")
##
##    result = a + b
##    return result
##
##print(mathsomething(a,b))
##print(f"a: {a}")
