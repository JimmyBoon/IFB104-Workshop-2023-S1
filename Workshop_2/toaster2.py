def jam(func):
    def wrap_func(*args, **kwargs):
        toast = func(*args, **kwargs)
        for i in range(0,len(toast)):
            if(toast[i] == 'toast'):
                #toast it
                toast[i] = 'toast with jam'
        return toast
    return wrap_func

@jam
def toaster(ingredents):
    for i in range(0,len(ingredents)):
        if(ingredents[i] == 'bread'):
            #toast it
            ingredents[i] = 'toast'
    return ingredents

bread = ["bread", "bread"]

print(toaster(bread))
