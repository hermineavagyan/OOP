locaL_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        return "hello"
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
print(locals())
print(__name__)
if __name__ == "__main__":
    print("the file is executed deirectly")
else:
    print("The file is being executed because it is imported by another file. This file name is:", __name__)