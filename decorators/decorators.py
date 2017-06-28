import time
import random
# ============================
# Function name and args
# ============================
def name(f):
    def inner( *arg ):
        r =  f.func_name + "    Arguments: ("
        for x in arg:
            r += str(x) + ","
        r += ")"
        # r += "\nOutput: "
        # r += str(f(*arg))
        return r
    return inner

@name 
def lala(s):
	return s 

@name 
def haha(x,y):
	return x + y

print lala('hi')
print haha(1,2)
print "==========================================="
# ============================
# Timetest
# ============================
def timetest(f):
    def run_f(*arg):
        begin = time.time()
        f(*arg)
        close = time.time()

        return "Function " + f.func_name + ": " + str(close - begin) + " seconds"
    return run_f

@timetest
def sum_l(l):
    total = 0
    for i in l:
        total += i
    return total

@timetest
def quicksortH(l):
    l = quicksort(l)
    return l
        
def quicksort(l):
    if len(l) <= 1:
       return l
    pivot = random.choice(l)
    lower = [ a for a in l if a < pivot ]
    upper = [a for a in l if a > pivot]

    return quicksort(lower) + ([pivot] * l.count(pivot)) + quicksort(upper)
        
print sum_l([1, 2])
print quicksortH([int(random.random() * 1000) for num in range(100)])
