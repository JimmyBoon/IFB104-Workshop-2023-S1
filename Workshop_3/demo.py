def test_func(thing):
    return (f"Hello {thing}")



resp = test_func("Dog")

print(resp)

def count_down(number, max_number):
    
    for i in range(1, number):
        print(f"Number is {i}")
        
        if i > max_number:
            return "Max number has been reached"

    return "All numbers are completed"

print(count_down(14, 10))
    
