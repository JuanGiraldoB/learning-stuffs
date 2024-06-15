# all()
# Returns True if all elements of an iterable are true or if it is empty
a = [1, 0, 1, 2, 3, -1]  # False, 0 is a falsy value
b = []  # True
print(all(b))
print()
# any()
# Returns True if at least one element of the iterable is true.
a = [1, 0, 1, 2, 3, -1]  # True
b = []  # False
print(any(b))
print()

# chr()
# Returns the string representing a character whose unicode code point is the integer i
A = 65
a = 97
print(chr(A))
print(chr(a))
print()

# enumerate()
# Returns a tuple containing a count starting from 0 and the values obtained from iterating over the iterable
values = ["a", "b", "c"]
for index, value in enumerate(values):
    print(index, value)
print()

# filter()
# Filter values in an iterable object


def filter_func(value):
    return value % 2 == 0


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, lst)
evens_2 = filter(filter_func, lst)
print(list(evens))
print(list(evens_2))
print()

# hash()
# Returns the hash value of the object, hash values are integers. Can only hash things that are inmutable
key = "randomstring"
print(hash(key))
print()

# map()
# Returns an interator that applies function to every item of itereable, yielding the results.
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = map(lambda x: x ** 2, vals)
print(list(squares))
print()

# range()
# Not a function but an immutable sequence type. This sequence has a start, stop and step value
r1 = range(1, 10, 2)
print(list(r1))

# reversed()
# Returns the a new iterable object reversed
lst = [1, 2, 3]
lst_reversed = reversed(lst)
print(id(lst))
print(id(lst_reversed))
print()

# slice()
# Returns an slice object representing the set of indices specified by range(start, stop, step)
lst = [2, 4, 6, 8, 10]
s = slice(1, 3)
lst_s = lst[1:3]
print(lst[s])
print(lst_s)
print()

# sorted()
# Returns a new sorted list from the items in the iterable object.
lst = [3, 4, 22, -9, 2, 44, 2]
sorted_lst = sorted(lst)
print(sorted_lst)
print()

# zip()
# Iterate over several iterables in parallel, producing tuples with an item from each one.
a = [4, 5, 6, 7]
b = ['a', 'b', 'c', 'd']
zipped = zip(a, b)
print(list(zipped))
