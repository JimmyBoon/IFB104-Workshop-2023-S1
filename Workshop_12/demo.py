from enum import Enum

# class syntax

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

print(Color['RED'].value)
my_selector = Color['GREEN']

match my_selector.value:
    case 1:
        print("Do the Red thing")
    case 2:
        print("Do the Green thing")
    case _:
        print("Do Nothing") 


