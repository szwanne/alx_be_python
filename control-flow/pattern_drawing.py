pattern = int(input("Enter the size of the pattern:"))
count = 0

while count < pattern:
    for _ in range(pattern):
        print("*", end="")
    print()  # This will make the asterik to move to the next line
    count += 1
