filename = 'aoc9data1.txt'
inf = open(filename)
for line in inf:
    m = line.strip()
inf.close()

print(m)

# create the string
arr = []
for i in range(len(m)):
    if i % 2 == 0:
        arr.extend([int(i / 2)] * int(m[i]))
    else:
        arr.extend('.' * int(m[i]))

# swap spaces for digits
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

# compute checksum
total = 0
for i in range(len(arr)):
    if arr[i] != '.':
        total += i * int(arr[i])
print(total)

# 6332189866718
