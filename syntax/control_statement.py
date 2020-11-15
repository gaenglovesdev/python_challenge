# <If>

handsome = True

if handsome:
    print("부럽다!")
else:
    print("ㅋㅋㅋ")


if handsome:
    pass
else:
    print("ㅋㅋㅋ!")

# 비교연산자

#  x < y  // x가 y보다 작다
#  x > y  // x가 y보다 크다
#  x == y  // x가 y와 같다
#  x != y  // x가 y와 같지 않다.
#  x >= y  // x가 y보다 크거나 같다
#  x >= y  // x가 y보다 작거나 같다

# and or not

money_in_pocket = 2000
card = True

if money_in_pocket >= 3000 or card:
    print("택시를 타세요.")
else:
    print("걷기!")


# x in s, x not in s

print(1 in [1, 2, 3])  # True
print(1 not in [1, 2, 3])  # False


# 삼항연산자

print(10 - 20 if 10 == 20 else 10+20)


# <While>
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# <For>

animals = ['dog', 'cat', 'snake']
for i in animals:
    print(i)  # dog , cat , snake

add = 0
for i in range(1, 11):
    add = add + i

print(add)  # 55
