role = input().strip()
if role == "admin":
    print("Full access")
elif role == "user":
    print("Limited access")
else:
    print("Guest")