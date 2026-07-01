

# list1 = [] # list creation

# names = ["Krish","Jack","Jacob"]
# print(names)


# mixed_list = [1,"Hello",3.4,5,True]
# print(mixed_list)

# fruits = ["apple","banana","cherry"]

# print(fruits[0]) # apple
# print(fruits[2]) # cherry
# print(fruits[5])

# print(fruits[-1]) # cherry

# print(fruits[1:2]) # banana
# print(fruits[0:2]) # apple banana
# print(fruits[0:]) # apple banana cherry
# print(fruits[:]) # use to copy of list 
# print(fruits[0:-1]) # apple banana


# list1 = ["apple","cherry","demo","banana","watermelon","orange"]
# list1[3] = "xyz"

# print(list1) # banana is replace by xyz


# List methods 

# names = ["Raj","Rahul","Mehul","Sameer","Parvez"]

# names.append("demo") # add demo at the end of names list
# print(names)

# names.insert(2,"Sam") # insert the Sam at the 2 index.
# print(names)

# names.remove("Mehul") # remove the Mehul from the list
# print(names)

# poped_name = names.pop()  # remove and return last element of list
# print(poped_name)

# index = names.index("Raj") # return the index 
# print(index)

# counting = names.count("Sameer") # return count number of 
# print(counting)

# names.reverse() # use to reverse the list 
# print(names)

# names.clear() # use to make empty list 
# print(names)

# Slicing list 
# nums = [1,2,3,4,5,6]
# print(nums[2:5]) # [3, 4, 5]
# print(nums[:5]) # [1, 2, 3, 4, 5]
# print(nums[5:]) # [6]
# print(nums[::2]) # [1, 3, 5]
# print(nums[::-1]) # [6,5,4,3,2,1]
# print(nums[::-2]) # [6,4,2]


# Iterate on list 

# fruits = ["Gav","Ban","Oran"]

# for key,value in enumerate(fruits):
#     print(key,value)

# 0 Gav
# 1 Ban
# 2 Oran


# list =[]

# for x in range(10):
#     list.append(x)

# print(list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#---------- List comprehension 

# demo = [x**2 for x in range(10)]
# print(demo) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


