

number3 = 10

def basic_func(number1 = 10, number2 = 99):
    global number3
    
    return number1 + number2 + number3


print(basic_func(1,2))


basic_lambda_func = lambda num1 = 90, num2 =10 : num1 + num2

print(basic_lambda_func())


number_list = [[10,2],[99,19],[33,99],[46,90]]

for little_list in number_list:
    number1 = little_list[0]
    number2 = little_list[1]
    result = basic_lambda_func(number1, number2)
    print(result)


def my_print_func(number):
    print(number)


my_print_func(10)

counter = 99

for i in range(0,10):
    counter -= 1
    my_lambda = lambda a = counter : my_print_func(a)
    my_lambda()


