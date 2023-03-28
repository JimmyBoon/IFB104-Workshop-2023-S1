##import time
##
##print("Hello, everybody")
##
##while True:
##    print("we will start soon")
##    time.sleep(2)
##    for i in range(0,10):
##        print(".")
##        time.sleep(2)
##    

container = "String"
listContainer = [1,2,3,4]

container = 10

#print(listContainer)

listContainer[0] = 10

#print(listContainer)

myOtherContainer = container

print(myOtherContainer)
print(container)
myOtherContainer = 20
print(myOtherContainer)
print(container)

my_new_list = listContainer
print(f"my list: {listContainer}")
print(f"my new list: {my_new_list}")

my_new_list[3] = "Cat in the Hat"

print(f"my list: {listContainer}")
print(f"my new list: {my_new_list}")
