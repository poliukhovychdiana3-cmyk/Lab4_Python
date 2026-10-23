
s = input()

result = 0
number = 0
sign = 1

for char in s:
    if char.isdigit():
        number = number * 10 + int(char)
    else:
        result += sign * number
        number = 0

        if char == "+":
            sign = 1
        else:
            sign = -1

result += sign * number

print(result)
