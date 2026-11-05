import os
name = input()
if not os.path.exists(name):
    print(-1)
else:
    with open(name, encoding="utf-8") as f:
        count = sum(1 for line in f if line.strip())
    print(count)