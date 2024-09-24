# marcus # is 11
# Gio # is 852

# write a program that will count as close as possible to 852 by 11
increment = int(input("Enter a number to count by"))
goal = int(input("Enter a number to count up to as close as possible"))
total = 0
while total + increment < goal:
    total += increment
print(total)