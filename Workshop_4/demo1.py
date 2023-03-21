

var_a = 10 >= 99
var_b = True

if var_a:
    print("True")
elif var_b:
    print(f"var_b is true, but var_a is false")
else:
    print("Nothing is true")

def something(a):
    if type(a) != int:
        print ("a not an int")
        return None

    return a**2

print(something("Water"))

def parent_function():

    print("Start of parent")

    def take_input():
        a = None
    
        while type(a) != int:
            print("Please enter a number:")
            a = input()

            try:
                a = int(a)
            except:
                print("That is not a number")

        print(f"You have entered the number {a}")
        return a
    
    take_input()



parent_function()

def take_input():
    a = None
    
    while type(a) != int:
        print("Please enter a number:")
        a = input()

        try:
            a = int(a)
        except:
            print("That is not a number")

    print(f"You have entered the number {a}")
    return a

def loop_over_evens(number_list):
    results = []

    for number in number_list:
        if number % 2 == 0:
            results.append(number)
            print(f"We added the number {number}")

        else:
            print(f"We rejected the number {number}")

    return results

print(loop_over_evens([1,2,3,4,5,6,7,8,9,0,99,123]))

        


