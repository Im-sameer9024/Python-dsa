# Dictionary :- It is key , value pair in curly brackets .

# dic1 = {
#     'name':"Raj",
#     'age':12,
# }

# print(dic1) #{'name': 'Raj', 'age': 12}

# empty_dictionary = {}
# print(type(empty_dictionary)) # <class 'dict'>


# Element accessing in Dictionary 

# person = {
#     'name':"Raj",
#     'age':32,

# }

# print(person['age'])
# print(person.get('name'))
# person['demo'] = 'mello' # use to set key , value 
# print(person)
# print(person.get('age'))

# person['age'] = 56

# update the element value 
# print(person['age'])

# person.popitem() # use to remove last element from dictionary
# print(person)

# delete 
# del person['age'] # delete the element from dictionary
# print(person) {'name': 'Raj'}

# print(person.keys()) dict_keys(['name', 'age'])
# print(person.values()) dict_values(['Raj', 32])
# print(person.items()) dict_items([('name', 'Raj'), ('age', 32)])

# x = person.copy()
# print(x) #{'name': 'Raj', 'age': 32}

# Iterating over Dictonary 

# for key,value in person.items():
#     print(key,value)

# name Raj
# age 32

# Nested Dictionary 

# person = {
#     'name':'Rahul',
#     'age':23,
#     'address':{
#         'city':'Delhi',
#         'pincode':110011,
#     }
# }

# squares={x:x**2 for x in range(5)}
# print(squares) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# print(person['address']['city']) # Delhi
# print(person.get('address').get('city')) # Delhi

# numbers = [1,2,3,2,3,4,5,4,5]

# frequency ={}

# for value in numbers:
#     if value in frequency:
#         frequency[value] += 1
#     else:
#         frequency[value] = 1

# print(frequency)  {1: 1, 2: 2, 3: 2, 4: 2, 5: 2}

# dic1 = {"a":1,"b":2}
# dic2 = {"b":3,"c":4}

# print(dic1 | dic2) # {'a': 1, 'b': 3, 'c': 4}
# print({**dic1,**dic2}) # {'a': 1, 'b': 3, 'c': 4}