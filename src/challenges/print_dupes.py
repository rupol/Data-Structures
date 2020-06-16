# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
# Input:
# [4,3,2,7,8,2,3,1]
# Output: 
# [2,3]

def print_dupes(list):
    seen = []
    dupes = []
    for num in list:
        if num in seen:
            dupes.append(num)
        else:
            seen.append(num)
    return dupes

a = [4,3,2,7,8,2,3,1]
b = ["hi", "hello", "hi", "howdy"]
c = [4, "hello", 8, 7, 4, "hi", 5, 2, 2, "hi"]

print(print_dupes(a))
print(print_dupes(b))
print(print_dupes(c))
