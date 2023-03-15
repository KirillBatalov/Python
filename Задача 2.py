squares = []

num = int(input())
while num != 0:
    if num % 2 == 0:
        squares.append(num ** 2)
    num = int(input())
print(squares)
