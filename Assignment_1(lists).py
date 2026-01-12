# 1. Create a list of 10 numbers and print the list.
num=[1,2,3,4,5,6,7,8,9,10]
print(num)      #1

# 2. Create a list containing different data types (integer, float, string, boolean) and print its type.
mix=[1,'ABC',3.5,True]
print(mix)         #2

# 3. Access and print the first, middle, and last elements from a list of your choice.
print(num[0],num[-1])
x=len(num)/2
print(num[int(x)])   #3

# 4. Slice the list to print the first 3 elements and last 3 elements separately.
print(num[0:3],num[-3::])   #4

# 5. Replace the second element of a list with a new value.
num[1]=15
print(num)      #5

# 6. Add a new element at the end of a list using append() and display the updated list.
num.append(20)
print(num)      #6

# 7. Insert an element at index 2 using insert() and print the updated list.
num.insert(2,16)
print(num)      #7

# 8. Extend the list with another list of your choice and display the final list.
num2=[30,40,50]
num.extend(num2)
print(num)      #8  

# 9. Remove a specific element by value using remove() and display the result.
num.remove(16)
print(num)      #9

# 10. Remove the element at index 3 using pop() and display which element was removed.
popped_element=num.pop(3)
print(popped_element)   #10

# 11. Delete the element at index 0 using del keyword and print the remaining list.
del num[0]
print(num)      #11

# 12. Clear all elements from the list using clear() and print the empty list.
num.clear()
print(num)      #12 

# 13. Recreate a list and check whether a specific element (for example "apple") exists in the list using the 'in' operator.
num=[1,2,3,4,5,6,7,8,9,10,9,5,9]
print(5 in num)   #13

# 14. Find the index position of a specific element in the list using the index() method.
print(num.index(10))   #14

# 15. Count how many times a specific value appears in the list using count().
print(num.count(9))    #15

# 16. Sort a list of numbers in ascending order using sort() and display the result.
num.sort()
print(num)      #16

# 17. Sort a list of strings in descending order using sort(reverse=True) and display the result.
num.sort(reverse=True)
print(num)      #17

# 18. Reverse the order of a list using reverse() and print the updated list.
num.reverse()
print(num)      #18

# 19. Copy the contents of one list to another using the copy() method and modify one list to see if it affects the other.
num2=num.copy()
del num2[2:7]    
print(num2)     #19

# 20. Combine two lists using the + operator and print the combined list.
num3=[20,30,40,50]
print(num+num3)  #20