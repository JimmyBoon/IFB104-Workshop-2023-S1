
class InputIsNotInt(Exception):
    pass

def give_me_a_number(a):
    #Guard Clause
    if type(a) != int:
        print(f"{a} is not a number")
        try:
            a = int(a)
        except ValueError as e:
            print("Can not convert")
            return None
        except Exception as e:
            print(e)
            return None
        finally:
            print("I will do this no matter what")

    a = a * 99 // 30

    return a



def get_input():
    not_valid = True

    while not_valid:
        print("Please give me a number:")
        number = input()
        if give_me_a_number(number) == None:
            continue
        else:
            not_valid = False

# get_input()




def give_me_a_number2(number):
    assert type(number) == int, "Input was not of type int"
    return "Done"

#print(give_me_a_number2("1"))

def give_me_a_number3(a):
    #Guard Clause
    if type(a) != int:
        raise InputIsNotInt

    a = a * 99 // 30

    return a

give_me_a_number("dfsad")