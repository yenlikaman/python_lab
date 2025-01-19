x = 5
print(type(x))
x = "Hello World" #str
print(type(x))
x = 20 #int
print(type(x))
x = 20.5 #float
print(type(x))
x = 1j #complex
print(type(x)) 
x = ["apple", "banana", "cherry"] #list
print(type(x))
x = ("apple", "banana", "cherry") #tuple
print(type(x))
x = range(6) #range
print(type(x))
x = {"name" : "John", "age" : 36} #dict
print(type(x))
x = {"apple", "banana", "cherry"} #set
print(type(x))
x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(x))
x = True #bool
print(type(x))
x = b"Hello" #bytes
print(type(x))
x = bytearray(5) #bytearray
print(type(x))
x = memoryview(bytes(5)) #memoryview
print(type(x))
x = None
print(type(x)) #NoneType
# SETTING THE SPECIFIC DATA TYPE
x = str("Hello World")
print(type(x))
x = int(20)
print(type(x))
x = float(20.5)
print(type(x))
x = complex(1j)
x = list(("apple", "banana", "cherry"))
print(type(x))
x = tuple(("apple", "banana", "cherry"))
print(type(x))
x = range(6)
print(type(x))
x = dict(name="John", age=36)
print(type(x))
x = set(("apple", "banana", "cherry"))
print(type(x))
x = frozenset(("apple", "banana", "cherry"))
print(type(x))
x = bool(5)
print(type(x))
x = bytes(5)
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))