print(8 >> 2)

print(3 << 2)

print(~3)

print(6 ^ 3)

print(6 | 3)

print(6 & 3)

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result

x = 5

print(x > 3 or x < 4)

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3

x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3

x = 5
y = 3

print(x > y)

x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3

x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3

print(x := 3)
3
x = 5

x <<= 3

print(x)

x = 5

x >>= 3

print(x)

x = 5

x ^= 3

print(x)

x = 5

x |= 3

print(x)

x = 5

x &= 3

print(x)

