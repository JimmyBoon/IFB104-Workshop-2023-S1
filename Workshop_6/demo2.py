instructions = [
    [0, "Write", 1234],
    [1, "Square", 888],
    [2, "Cube", 99]
]

def write(number):
    print(number)

def square(number):
    print(number**2)

def cube(number):
    print(number*3)

for instruction in instructions:
    if instruction[1] == "Write":
        write(instruction[2])
    if instruction[1] == "Square":
        square(instruction[2])
    if instruction[1] == "Cube":
        cube(instruction[2])

my_dict = dict({"Tom": 999, "Mary":888})

my_dict.update({"James" : 123, "Sarah":000})
my_dict.update({(10,99): "Smiley face"})

other_dict = my_dict

other_dict["James"] = "Not Sad"

for key, value in my_dict.items():
    print(f"The key was: {key}, the value was {value}")

