import sys
for line in sys.stdin:
    password = line.strip()
    if password == "1234":
        print("OK")
        break
    else:
        print("FAIL")