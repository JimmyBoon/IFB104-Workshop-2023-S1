counter = 0

while counter < 10:

    counter += 1
    print("While I am running")

mylist = [1, 2, "word", ["one",1]]

for i in mylist:
    if i == "word":
        break
    print(i)
