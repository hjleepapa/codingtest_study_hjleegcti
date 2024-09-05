def add_three(x):
    return x + 3

def square(x):
    return x * x

# 3을 더한 후, 제곱근을 하고 싶을 때
compose_func = lambda x :  square(add_three(x))

print(compose_func(5))