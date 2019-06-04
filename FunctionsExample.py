from functools import reduce

lst = [1, 2, 3, 4, 5, 6]
print(lst)
"""
TEST CODE , PLEASE IGNORE
max = lst[0]
mini = lst[0]

def max_min(a,b):
    if a > b:
        max = a
    if a < b:
        mini = a
    return {max, mini} 

reduce(max_min, lst)

print(max)
print(mini)

"""
print("***EXAMPLE OF REDUCE ****")
print("Multiplication list is")
print(reduce(lambda a, b: a * b, lst))

print("***EXAMPLE OF FILTER ****")


print("Number in list greater  than 3 are ")
print(list(filter(lambda a: a > 3, lst)))

print("***EXAMPLE OF MAP ****")


print("Table of all Integer in list i.e first 10 multiples ")

for l in list(map(lambda a: [a*1, a*2, a*3, a*4, a*5, a*6, a*7, a*8, a*9, a*10], lst)):
    print(l)







