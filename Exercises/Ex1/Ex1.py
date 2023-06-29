import sys

lines = sys.stdin.read().splitlines()

if not int(lines[0]) % 2:
    print("Bob")
else:
    print("Alice")
