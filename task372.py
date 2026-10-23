
s = input()

max_zeros = 0
count = 0

for char in s:
    if char == "0":
        count += 1
        if count > max_zeros:
            max_zeros = count
    else:
        count = 0

print(max_zeros)
  