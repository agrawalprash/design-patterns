####### Calling functions using *args ########################################

def add(x, y):
    return x + y

print add(1,3)

def stupid_add(x, y, z, w):
    return x + y + z + w

print stupid_add(1,3,4,5)

def ok_add(add_list):
    result = 0
    for item in add_list:
        result += item

    return result

items = [1,2,3,4]
print ok_add(items)

def smart_add(*args):
    """ `args` is a tuple containing all the positional arguments supplied
    to the function."""
    result = 0
    for item in args:
        result += item

    return result

print smart_add(1,2,3,4)
print smart_add(*items)


####### Calling functions using **kwargs #####################################

def names(name1='', name2=''):
    return name1 + ', ' + name2

print names(name2='Shashank', name1='Prashant')

def smart_names(**kwargs):
    names = kwargs.values()
    result = ''
    for name in names:
        result += name + ', '

    return result

print smart_names(name1='Shashank', name2='Prashant', name3='Bhabhi')


#### Combining *args and **kwargs ############################################

def plot(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs
    things_to_plot = args
    for thing in things_to_plot:
        _add_to_figure(thing)

    if kwargs.get('xlabel') is not None:
        add_x_label()

# This is usually documented as:
#
# def plot(x, [y, [z,... ]], xlabel='', ylabel='')

# This will print:
#
# args: ([1, 2], [3, 4])
# kwargs: {'xlabel': 'hello'}
x = [1, 2]
y = [3, 4]
plot(x, y, xlabel='hello')
