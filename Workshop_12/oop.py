class Worker():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def do_work(self, job):
        print(f"{self.name} is doing some good work with {job}")


james = Worker("James", "Old")

print(james.name)
print(james.age)

james.do_work("Coding")

tim = Worker("Tim", "Not so old")

tim.do_work("Cleaning")