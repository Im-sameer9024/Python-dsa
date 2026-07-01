# function : - It is block of code which is used to perform a specific task. It is reusable block of code.

# def func(parameterh):
#     return parameterh

# def print_nums(*args):
#     for i in args:
#         print(i)

# print_nums(1,2,3,4,5,6,7,8,9,10)

# def func(**kwargs):
#     print(kwargs)

# func(name='Rahul', age=23, city='Pune')



# def is_strong_password(password):
#     if len(password) < 8:
#         return False
#     elif not any(char.isdigit() for char in password):
#         return False
#     elif not any(char.isupper() for char in password):
#         return False
#     elif not any(char.islower() for char in password):
#         return False
#     elif not any(char in '!@#$%^&*()_+' for char in password):
#         return False
#     else:
#         return True
    

# print(is_strong_password('Rahul123@'))


# def calculate_total_items(cart):
#     pass

  
    
#     total = {
#         'price':0,
#         'quantity':0
#     }
#     for item in cart:
#         total['price'] += item['price'] * item['quantity']
#         total['quantity'] += item['quantity']

#     return total



# print(
#     calculate_total_items(
# [
#        {'name': 'apple', 'price': 10, 'quantity': 2},
#        {'name': 'banana', 'price': 5, 'quantity': 3},
#        {'name': 'orange', 'price': 15, 'quantity': 1}
#      ]
#     )
# )

# addition =lambda x,y : x+y
# print(addition(10,20))
map(lambda x: x*2, [1,2,3,4,5])
print(list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9,10])))