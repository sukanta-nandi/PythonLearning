# https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313

# https://www.geeksforgeeks.org/python-list-comprehension/


# using lambda to print table of 10
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
 
print(numbers)

lis = [num for num in range(100)
      if num % 10 == 0]
print(lis)


# Flattening a list
myList = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print([x for x in myList])
print([num for numbers in myList for num in numbers])


# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
  
print(matrix)