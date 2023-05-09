class MyError(Exception):
    pass
    

def givemethree():
    return 3

def giveme4(a):
    if type(a) != int:
        raise MyError("a is not an int")

    try:
        a = int(a)
    except:
        print("a is not an int")
    return a

def test_givemethree():
    assert givemethree() == 3

def test_giveme4():
    assert giveme4("four") == 4


giveme4("four")