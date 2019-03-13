"""
Tests for decorators,
Mainly timing decorator and function
"""
from timeit import default_timer as timer



########## TIMINGS ##########
def times_function(func,no_times,*args,**kwargs):
    """
    Function for timing given function with given arguments
    Variable number of times it iterates
    """
    times = list()
    for x in range(no_times):
        st = timer()
        func(*args,**kwargs)
        tt = timer()
        times.append((st,tt))
    print("{} done {} times in {:.4}s".format(func.__name__,
                                              no_times,
                                              times[-1][1] - times[0][0]
                                              ))
    print("Average time: {}".format(sum([x[1]-x[0] for x in times])/len(times)))


def times(no_times):
    """
    Decorator for timer function
    It's only want to time function while changing parameters of it
    Takes argument for number of iterations it will do
    """
    def decor(func):
        def func_wrapper(*args,**kwargs):
            times_function(func,no_times,*args,**kwargs)
        return func_wrapper
    return decor


## Defining the function with and without decorators
## Both do the same, create a list of elements made from range()
@times(10**3)
def deco_arange(length):
    [x for x in range(length)]
    
def arange(length):
    [x for x in range(length)]


def timings():
    print("With decorator")
    deco_arange(1000)
    
    print("\nWithout decorator")
    times_function(arange,10**3,1000)
    


def main():
    timings()

    
if __name__ == "__main__":
    main()


