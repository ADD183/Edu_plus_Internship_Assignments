# 1. Create a set containing five different country names and print it.
country={'India','USA','UK','Russia','China'}
print(country)  # 1

# 2. Create a set with duplicate numbers and print it to see how duplicates are handled.
country2={"UK","UAE","USA","UK"}
print(country2)  # 2

# 3. Use the set() constructor to create a set from a list of fruits.
fruits=set(["apple","banana","cherry","apple"])
print(fruits)  # 3

# 4. Add a new element into an existing set using add() method.
country2.add("Germany")
print(country2)  # 4

# 5. Add multiple elements into a set using update() method.
country.update(country2)
country.update(["Spain","Italy"])
print(country)  # 5

# 6. Try adding a duplicate element to the set and check if it changes.
fruits.add("cherry") #6
print(fruits)   #positions changes

# 7. Remove an element from a set using remove() method.
country.remove("Russia")
print(country)  # 7

# 8. Remove an element safely using discard() without raising an error.
country.discard("Spain") #8
print(country)  # no error

# 9. Remove a random element using pop() and print both removed and remaining elements.
popped=fruits.pop()
print("Popped fruit:",popped)
print(fruits) # 9

# 10. Clear all elements from a set using clear() and print it.
country.clear()
print(country)  # 10

# 11. Create two sets of numbers and perform union operation.
A={1,2,3,4,5}
B={4,5,6,7,8}
C={2,3,4}

print("Union:", A | B) # 11

# 12. Perform intersection between two sets to find common elements.
print("Intersection:", A & B) # 12

# 13. Perform difference between two sets to find unique elements from the first set.
print("First Set- Second Set:",A - B) # 13

# 14. Perform symmetric difference between two sets and print the result.
print("Symmetric Difference:", A ^ B) # 14

# 15. Check if one set is a subset of another using issubset() method.
print("C is subset of A?",C.issubset(A)) # 15

# 16. Check if one set is a superset of another using issuperset() method.
print("A is superset of C?",A.issuperset(C)) # 16

# 17. Check if two sets have no common elements using isdisjoint() method.
print("Doesn't A and B have common ?",A.isdisjoint(B)) # 17

# 18. Use in keyword to check if a particular element exists in a set.
print("Is India present in country?","India" in country) # 18

# 19. Use not in keyword to check if an element does not exist in a set.
print("Is UAE not present in country?","UAE" not in country) # 19

# 20. Find the total number of elements in a set using len().
print("Lenght of country2 set:",len(country2)) # 20

# 21. Find the maximum and minimum element from a numeric set using max() and min().
print("Max value:",max(A)) # 21
print("Min value:",min(A))  # 21

# 22. Find the sum of all elements from a numeric set using sum().
print("Sum of A set:",sum(A)) # 22

# 23. Convert a set into a sorted list in ascending order using sorted().
sort=sorted(B)  #Needed varible because set are immutable
print("Ascending order of B set:",sort) # 23

# 24. Sort a set in descending order using sorted() with reverse=True.
rev_sort=sorted(B,reverse=True)
print("Descending order of B set:",rev_sort) # 24

# 25. Use any() to check if at least one True value exists in a Boolean set.
bool={1,1,1}
print("Any element is true:",any(bool) ) # 25

# 26. Use all() to check if all values in a Boolean set are True.
print("All element are true:",all(bool)) # 26

# 27. Copy a set using copy() and verify both sets are independent.
D=C.copy()
print(C)
print(D) # 27

# 28. Delete a set completely using del keyword and observe the result.
del D
#print("D after deletion:",D) # Error because D is deleted # 28

# 29. Convert a list with duplicate values into a set to remove duplicates.
list=[1,2,2,3,4,4,5]
X=set(list)
print(X) # 29

# 30. Create two sets of student names (from two different classes) and find:

class_A={"Alice","Bob","Charlie"}
class_B={"Bob","David","Eve"}

#     a) Common students (intersection)
print("Same students:", class_A & class_B) # 30

#     b) Students only in class A (difference)
print("Class A sudents:",class_A - class_B) #30

#     c) All unique students (union)
print("All students:", class_A | class_B) #30


