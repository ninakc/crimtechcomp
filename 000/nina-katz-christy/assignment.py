from math import sqrt
def say_hello():
	print("Hello, world!")

# Color: blue

# TODO: implement
def echo_me(msg):
    print(msg)

# TODO: understand formatting - can you eliminate the redundancy here?
def append_msg(msg):
    print("Your message should have been: {}!".format(msg))

# TODO: understand class (an introduction)
class QuickMaths():
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

# TODO: implement - can you do this more efficiently?
def increment_by_one(lst):
    def increment(x):
        return x + 1
    new_lst = map(increment, lst)
    #for x in lst:
      #  new_lst.append(x + 1)
    
    return new_lst

# TODO: implement - do we need a return statement here? why?
def update_name(person, new_name):
    person["name"] = new_name

    return person

# TODO: implement - these are still required, but are combinations of learned skills + some
def challenge1(lst):
    lst.reverse()
    def reverse_string(str):
        return str[::-1]
    lst = map(reverse_string, lst)
    return lst

# TODO: implement
def challenge2(x):
    lst = list()
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            lst.append((i, x / i))
    return lst


