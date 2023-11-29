# Find maximum element in each iteration and put it in last index


lst = [-1, -3, 20, 9, 4, 5, 6, 2, 3, 7, 1, 8, 10, 11]
maxPos = 0
pos = len(lst) - 1

while pos > 0:
    max = float("-inf")
    for i in range(pos + 1):
        if lst[i] > max:
            max = lst[i]
            maxPos = i

    lst[maxPos], lst[pos] = lst[pos], lst[maxPos]
    pos -= 1

print(lst)
