
s = input().upper()

counts = [0] * 26

for char in s:
    if 'A' <= char <= 'Z':
        index = ord(char) - ord('A')
        counts[index] += 1

max_count = max(counts)
letters = ""

for i in range(26):
    if counts[i] == max_count and max_count > 0:
        letters += chr(i + ord('A'))

print(letters)
print(max_count)
