# *args: f takes variable number of positional (from left to right) arguments -> function is variatic)
# *kwargs: keyword arguments (from right to left) -> dictionary with all name arguments
def f(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Named: {kwargs}")


f(100, 50, 25, 5)  # positional arguments
print("-------------------------------")
f(galleons=100, sickles=50, knuts=25, pennies=5)  # named arguments