
s = input()

numbers = s.split("*")
result = 1

for num in numbers:
    result *= int(num)

print(result)
