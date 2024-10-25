# TODO
def is_perfect(n):
    def proper_divisors(num):
        return [i for i in range(1, num) if num % i == 0]
    
    return sum(proper_divisors(n)) == n


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)
