number = int(input("Enter a number to see its multiplication table:"))
print(number)
numbers = 1
for num in range(1, 11):
    numbers = number*num
    print(numbers)
