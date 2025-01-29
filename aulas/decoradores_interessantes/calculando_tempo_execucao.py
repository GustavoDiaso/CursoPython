from decorators.timing import get_time

@get_time
def my_function():
    for _ in range(0,1_000_000):
        print('')

my_function()