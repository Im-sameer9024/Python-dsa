# Set :- it contain a uniq element always .

# a = {'a','b','a'}
# print(a) # {'a','b'}

# nums = {1,2,3,4}
# print(type(nums))  #<class 'set'>

# my_empty_set = set()
# print(my_empty_set)

# set1 = set([3,4,5,3])
# print(set1) {3,4,5}


#------------ Set Operations -------

# my_set = {1,2,3,4,5}

# my_set.add(7)
# print(my_set) {1, 2, 3, 4, 5, 7}

# my_set.remove(3)
# print(my_set) {1, 2, 4, 5}

# my_set.clear() 
# print(my_set) set()

# my_set.discard(11) # check if it is available then it remove other wise no effect
# print(my_set)

# last = my_set.pop()
# print(last) #1
# print(3 in my_set) # True (check the element is available or not in list )


set1 = {1,2,3,4}
set2 = {5,4,8,7,2}

# union_set = set1.union(set2)
# print(union_set) {1, 2, 3, 4, 5, 7, 8}

# intersection_set = set1.intersection(set2)
# print(intersection_set) {2,4}

# x = set1.difference(set2)
# print(x) {1,3}

# y = set2.difference(set1)
# print(y) {8,5,7}

