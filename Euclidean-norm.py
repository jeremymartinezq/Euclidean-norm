# Program Summary: This script includes three functions to check distinct numbers, compute dot product, and calculate the Euclidean norm.

# Function 1: Check if all elements are distinct
def distinct(data):
    """Returns True if all numbers in the sequence are distinct, False otherwise."""
    return len(set(data)) == len(data)

# Function 2: Dot product of two arrays
def dot_product(a, b):
    """Returns the dot product of two arrays."""
    return [a[i] * b[i] for i in range(len(a))]

# Function 3: Norm (Euclidean norm where p=2)
def norm(v, p=2):
    """Returns the Euclidean norm of a vector."""
    return sum(abs(x) ** p for x in v) ** (1 / p)

# Driver Code (Example execution for testing the functions)
list1, list2 = [1, 3, 4, 5], [2, 6, 6, 7]
print(distinct(list1))  # True
print(distinct(list2))  # False

print(dot_product(list1, list2))  # [2, 18, 24, 35]

vector1, vector2 = (3, 4), (5, 12)
print(norm(vector1))  # 5.0
print(norm(vector2))  # 13.0
