# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def assert_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return None  # Return None instead of 0
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value < 0:
                return None  # Return None instead of 0
        return func(*args, **kwargs)
    return wrapper

@assert_positive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Adapt this function if you need to test decorator
@assert_positive
def run(x, y):
    return x + y

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
