# Decorators = a way of taking a function and modifying that function
# i.e. adding som additional behavior to that function
# The idea of a decorator is that it will be a function that takes a function as an input
# and returns a modified version of that function as output


def announce(f):
  def wrapper():
    print("About to run the function")
    f()
    print("Done with the function")
  return wrapper 

@announce
def hello():
  print("Hello World")

hello()