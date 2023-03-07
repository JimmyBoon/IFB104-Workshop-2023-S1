
def am_or_pm(hour):
    return hour > 12

def hello(hour):

    greeting = "Good morning"

    if am_or_pm(hour):
        greeting = "Good afternoon"
        
    return greeting


name = "Damien"

print(f"{hello(14)} {name}, how are you today?")




