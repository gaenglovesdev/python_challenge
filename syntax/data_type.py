# <숫자형>

a = 1  # int
b = 2  # int
print(a, b)  # 1 2

c = 3.12  # float
d = 1.11  # float
print(c, d)  # 3.12 1.11


e = 0o177  # Octal
print(e)  # 127

f = 0x8ff  # Hex
print(f)  # 2303


# <연산자>

# + - * / 사칙연산

# 제곱 연산자 **
print(3 ** 3)  # 27

# 나머지 연산자 %
print(7 % 3)  # 1

# 나눗셈 몫 연산자 //
print(4 // 2)  # 2


# <자료형>

# 문자열

hello_python = "hello Python!"
i_am_beginner = 'I am beginner'
life_is_too_short = """Life is too short, You need python"""
print(hello_python)
print(i_am_beginner)
print(life_is_too_short)


# 리스트

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
days = ['mon', 'tue', 'wed', 'thur', 'fri']

print(odd)  # [1, 3, 5, 7, 9]
print(even)  # [2, 4, 6, 8, 10]
print(days)  # ['mon', 'tue', 'wed', 'thur', 'fri']
print(odd[0])  # 1
print(odd[0] + even[0])  # 3
odd.append(11)
print(odd)  # [1, 3, 5, 7, 9, 11]
print(odd[0:3])  # [1, 3, 5]
print(odd[-1])  # 11
print(odd[0:-1])  # [1, 3, 5, 7, 9]

# 튜플
tuple_test = (1, 2, 3, 4)
# del tuple_test[0]  :: 'tuple' object doesn't support item deletion

print(tuple_test + tuple_test)  # (1, 2, 3, 4, 1, 2, 3, 4)
print(tuple_test * 3)  # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)


# 딕셔너리
cho = {
    "name": "cho",
    "age": "30",
    "language": ['css', 'js']
}

print(cho)  # {'name': 'cho', 'age': '30', 'language': ['css', 'js']}
print(cho["age"])  # 30

cho["city"] = "suwon"
print(cho)
# {'name': 'cho', 'age': '30', 'language': ['css', 'js'], 'city': 'suwon'}

cho["language"].append("python")
print(cho)
# {'name': 'cho', 'age': '30', 'language': ['css', 'js', 'python'], 'city': 'suwon'}


# 집합

set1 = set([1, 2, 3, 4, 5])
set2 = set([3, 4, 5, 6, 7])
print(set1)  # {1, 2, 3, 4, 5}
print(set1 & set2)  # 교집합 {3, 4, 5}  or set1.intersection(set2)
print(set1 | set2)  # 합집합 {1, 2, 3, 4, 5, 6, 7} or set1.union(set2)
print(set1 - set2)  # 차집합 {1, 2} or set1.difference(set2)

# 불

bool1 = True


print(bool1)  # True
print(2 > 1)  # True
print(2 < 1)  # False
print(0)  # False
print(1)  # True
print([])  # False
print({})  # False
