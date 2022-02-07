# create

a = [1, 2, 3]
b = list("abc") # b = ['a', 'b', 'c']

# insert
a.insert(2, "a") # a is [1, 2, 'a', 3] now <== insert "a" to index 2

# remove
a.remove(2) # a is [1, 'a', 3] <== remove value 2
a.append(3) # a is [1, 'a', 3, 3]
a.remove(3) # a is [1, 'a', 3] <= only remove the first occurrence

# iterate
for index, value in a:
    print(index, value)
