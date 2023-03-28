
# 0, 1, 1, 2, 3, 5, 8, 13 ...

def fiboForLoop(number):
    prev2 = 1
    prev1 = 1

    for _ in range(number):
        current = prev1 + prev2

        print(current)
        
        prev2 = prev1
        prev1 = current


def fiboWhileLoop(number):
    prev2 = 0
    prev1 = 1
    counter = 0
    while counter < number:
        current = prev1 + prev2

        print(current)
        
        prev2 = prev1
        prev1 = current

        counter += 1

def fiboWhileLoopWithContinue(number):
    prev2 = 0
    prev1 = 1
    counter = 0
    second = False
    
    while True:
        current = prev1 + prev2

        if second:
            prev2 = prev1
            prev1 = current

            counter += 1
            second = False
            continue

        second = True
        print(current)
        prev2 = prev1
        prev1 = current
        counter += 1

        if counter > number:
            break



def fiboRec(number):
    print(number)
    #Base Cases:
    if(number == 0):
        return 0

    if(number == 1):
        return 1

    #General Case:
    return fiboRec(number - 1) + fiboRec(number - 2)


def simpleRec(number):

    if(number == 0):
        print("Done")
        return

    print(number)
    simpleRec(number - 1)

simpleRec(10)

    
## Out of scope for this unit:
def fibo_gen():
    prev2 = 0
    prev = 1
    yield 0
    yield 1
    while True:
        current = prev + prev2
        yield current
        prev2 = prev
        prev = current

##gen = fibo_gen()
##
##    
##for i,v in enumerate(gen):
##    if i < 20:
##        print(v)
##    else:
##        break

## END Out of scope for this unit:
