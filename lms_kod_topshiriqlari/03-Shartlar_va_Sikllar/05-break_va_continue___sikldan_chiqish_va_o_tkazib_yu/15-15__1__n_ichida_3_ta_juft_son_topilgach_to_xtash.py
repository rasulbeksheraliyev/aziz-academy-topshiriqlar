n = int(input())
count = 0
last_even = 0
found = False
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
        last_even = i
        if count == 3:
            found = True
            break
if found:
    print(last_even)
else:
    print("No")