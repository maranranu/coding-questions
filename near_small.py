n = int(input())
arr = (input()).split(" ")
arr = [int(a) for a in arr]

h = {}
for i in range(len(arr)):
    h[arr[i]] = i

output = {}
arr.sort()
for i in range(1, len(arr)):
    a1 = arr[i-1]
    a2 = arr[i]
    if (a1 < a2 and h[a1] < h[a2]):
        output[a2] = a1
    else:
        output[a2] = -1
print(output)
