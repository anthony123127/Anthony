def print_reverse_centered_triangle(n):
    for i in range(n, 0, -1):

        print(' ' * (n - i) + '*' * (2 * i - 1))


n = 5
print_reverse_centered_triangle(n)
