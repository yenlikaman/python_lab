x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
True
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
True
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
True
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
{'microsoft', 'banana', 'google', 'cherry'}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
{'cherry', 'banana'}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
{'cherry', 'banana'}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
{'apple'}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
{'apple'}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
{'apple'}
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
{1, 2, 3, 'a', 'b', 'c'}
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
{'b', 1, 2, 3, 'c', 'a'}
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
{'b', 1, 2, 3, 'c', 'a'}
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
set()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
apple
{'cherry', 'banana'}
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
{'apple', 'cherry'}
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
{'apple', 'cherry'}
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
{'apple', 'cherry', 'mango', 'banana', 'pineapple', 'papaya'}
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
{'orange', 'apple', 'cherry', 'banana'}
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
False
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
True
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
apple
cherry
banana
myset = {"apple", "banana", "cherry"}
print(type(myset))
<class 'set'>
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
{True, 2, 'apple', 'cherry', 'banana'}