import random

def union_sets(A, B):
    result = [element for element in A if element not in B]
    return [element for element in B if element not in result] + result 
    
def intersection_sets(A, B):
    return [element for element in A if element in B]

# complement of A in U
def set_diff(U, A):
    return [element for element in U if element not in A]

def symmetric_diff(A, B):
    combined = A + B
    return [element for element in combined if (element not in A or element not in B)]  
    
def cartesian_product(A, B):
    return [(element_A, element_B) for element_A in A for element_B in B]        

# A = [random.randint(0, 10) for r in range(10)]
# B = [random.randint(0, 10) for r in range(10)]
# A = random.sample(range(10), 5)
# B = random.sample(range(10), 5)

# print sorted(A)
# print sorted(B)
# print "================================="

# print "Union: " + str(sorted(union_sets(A, B)))
# print "Intersection: " + str(sorted(intersection_sets(A, B)))
# print "Set diff: " + str(sorted(set_diff(A, B)))
# print "Symmetric diff: " + str(sorted(symmetric_diff(A, B)))
# print "Cartesian product: " + str(cartesian_product(A, B))
# print "Cartesian product length: " + str(len(cartesian_product(A, B)))
