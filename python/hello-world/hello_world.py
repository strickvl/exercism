#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name == '':
        return "Hello, World!"
    if name == None:
        return "Hello, World!"
    if not name and name.strip():
        return "Hello, World!"
    else:
        string = "Hello, "+ name+"!"
        return string
