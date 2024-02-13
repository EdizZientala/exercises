def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    if n == 0:
        return n
    else:
        return last_digit(n) + digit_sum(remove_last_digit(n))
