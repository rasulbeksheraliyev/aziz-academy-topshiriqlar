a, b, c = map(int, input().split())
if a == b == c:
    print("All equal")
elif a == b or b == c or a == c:
    print("Partially equal")
else:
    print("Not equal")