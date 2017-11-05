def get_square_digit_sum(number):
    return sum([int(x)**2 for x in '{0}'.format(number)])

def is_lucky(number):
    """
    calculate sum of digits until lucky or already processed
    """
    processed = []
    x = number
    while True:
        r = get_square_digit_sum(x)
        if r == 1:
            return True

        if r in processed:
            return False

        processed.append(r)
        x = r

for n in range(20):
    print("{0} - {1}".format(n, is_lucky(n)))

is_lucky(19)