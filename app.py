
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as err:
    print("Yo, yo, yo! You didn't enter a number... why tho?")
    print(err)