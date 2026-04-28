

class newclass :
    def omer(self):
        print("mkna")

walking = newclass()
print(walking)

def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("After")
        return val
    return wrapper



@logtime
def hello():
    print("hello")

hello()