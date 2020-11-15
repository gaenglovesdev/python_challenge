# <Function>
def say_hi():
    return "Hi!"


print(say_hi())  # "Hi!"


def add(a, b):
    return a + b


print(add(1, 2))  # 3
print(add(b=1, a=2))  # 3

# *args


def add_all(*args):
    result = 0
    for i in args:
        result = result + i
    return result


print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 45


def add_mul(type, *args):
    result = 1
    if type == "add":
        for i in args:
            result = result + i
    else:
        for i in args:
            result = result * i
    return result


print(add_mul("add", 1, 2, 3, 4, 5, 6, 7, 8, 9))  # 46
print(add_mul("mul", 1, 2, 3, 4, 5, 6, 7, 8, 9))  # 362880

# **kwargs


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name="cho", age=30)  # {'name': 'cho', 'age': 30}


# lambda

def plus(a, b): return lambda d, c: a+b+c+d


result = plus(1, 2)(3, 4)
print(result)  # 10


# <Input, Output>
#input_number = input("숫자를 입력하세요: ")
# print(input_number)


# <File>

file = open("./syntax/new.txt", "w")  # r 읽기 , w 쓰기 , a 추가
file.write("hello world, hello python")
file.close()


file = open("./syntax/new.txt", "a")
file.write("\nedit")
file.close()

# with
with open("./syntax/new2.txt", "w") as file2:
    file2.write("Life is too short, you need python")
