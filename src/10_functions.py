# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
    if(n % 2) == 0:
        print(f"\n {n} is Even \n")
        return True
    else:
        print(f"\n {n} is Odd \n")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
while num!= 777:
    num = int(num)
    is_even(num)
    num = input("Enter a number: ")

# YOUR CODE HERE

