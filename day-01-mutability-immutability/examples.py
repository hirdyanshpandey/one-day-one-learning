# Immutable example
s = "hello"
print(id(s))

s = "Hello"
print(id(s))


# Mutable example
lst = [1, 2, 3]
print(id(lst))

lst.append(4)
print(id(lst))


# Function behavior
def modify_list(data):
    data.append(100)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)
