thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
3
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
('a', 'b', 'c', 1, 2, 3)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
apple
banana
cherry
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
apple
['mango', 'papaya', 'pineapple']
cherry
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
