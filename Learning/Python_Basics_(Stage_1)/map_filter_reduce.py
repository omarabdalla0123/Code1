from functools import reduce
# map(), filter(), reduce()
# are global scope vairables 
# map() :  " iterable ", run each item on a list
print("# ----1 map ----")

numbers = [1, 2, 3]

result = map(lambda a : a * 2, numbers)
print(list(result))


# filter(), " iterable " return a filter object.
print("# ---- 2 filter ----")


result2 = filter(lambda n : n % 2 == 0, numbers)

print(list(result2))

# reduce(), used to calculate the a value out of sequence like a list
print("# ---- 3 reduce ----")




expenses = [
    ('lanuch', 120),
    ('breakfast', 50)
]


sum2 = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum2)

print("# ---- without reduce ----")
sum = 0

for expense in expenses :
    sum += expense[1]

print(sum)    
