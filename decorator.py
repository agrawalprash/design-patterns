def logging(f):
    def wrapped(*args):
        result = f(*args)
        print f.__name__, args, ':',  result
        return result
    return wrapped

# This is same as: add = logging(add)
@logging
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

add(1, 2)
subtract(1, 2)
