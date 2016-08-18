def super_sum(*args):
    total = 0
    for value in args:
        if type(value) == list:
            for number in value:
                total = total + number
        else:
            total = total + value
    return total
