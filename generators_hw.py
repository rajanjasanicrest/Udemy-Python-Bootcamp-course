import random
# Q. Create a generator that generates the squares of numbers up to some number N
def gen_squares(m, n):
    for i in range(m,n):
        yield i**2
# for x in gen_squares(1,10):
#     print(x)
        
#q2. Create a generator that yields 'n' random numbers between a low and high number (that are inputs)
def gen_random(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
low = int(input("Enter the lower bound"))
high = int(input("Enter the upper bound"))
n = int(input("How many Random integers you need?"))
for x in gen_random(low,high,n):
    print(x)
