filename = 'aoc9data1.txt'
inf = open(filename)
for line in inf:
    m = line.strip()
inf.close()

print(m)

# create the string
s = ''
for i in range(len(m)):
    if i % 2 == 0:
        s += str(int(i / 2)) * int(m[i])
    else:
        s += '.' * int(m[i])
print(s)

# swap spaces for digits
arr = [c for c in s]
arr.append('.')
print(arr)
j = len(arr) - 1

for i in range(len(arr)):
    if arr[i] == '.':
        while arr[j] == '.':
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

print(arr)

# convert back to string
s = ''.join(e for e in arr).rstrip('.')
print(s)

total = 0
for i in range(len(s)):
    if s[i] != '.':
        total += i * int(s[i])
print(total)



# i = 0
# j = len(s) - 1
# # countj = 0
# s1 = ''
# while i < len(s):
#     if s[i] == '.':
#         s1 += ''
#     else:
#         s1 += s[j]
#         # countj += 1
#         j -= 1
#         s = s[:-1]
#     i += 1

# 90489586600   incorrect
