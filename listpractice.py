squares = [x**2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(11) if x % 2 == 0]
print(evens)

list1 = [1,2,3]
# list2 = list1[:]
# list2 = list(list1)
list2 = list1.copy()
# print(list2)

list2.append(4)
# print(list1)

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matrix2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]


my_lst = []
for i in range(len(matrix)): 
    for j in range(len(matrix)):
          my_lst.append(matrix[i][j] + matrix2[i][j])
    
print(my_lst)


# print(matrix[0][0]) # 1
sentence = "My name is Brian"
word = "Brian"
print(sentence.split())
print(word.split())
print(list(word))
