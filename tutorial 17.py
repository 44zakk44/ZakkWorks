def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 12, 15)
add_numbers(3, 34, 6, 5)