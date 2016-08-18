def super_sum(*args):
    total = 0
    for value in args:
        if isinstance(value, list):
            for number in value:
                total = total + number
        elif isinstance(value, str):
        	continue
        else:
            total = total + value
    return total

print (super_sum(2, 3.5))