# last one
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # specialized

empty_bicycles = []
# print(empty_bicycles[-1]) # error IndexError: list index out of range

motorcycles = ['yamaha']
motorcycles.append('triumph')
print(motorcycles)  # ['yamaha', 'triumph']

cars = []
cars.insert(-1, 'honda')
print(cars) # ['honda']
cars.insert(0, 'bmw')
print(cars) # ['bmw', 'honda'] 

del cars[1] # -1 or index should be in the range to prevent Error
print(cars)  # ['bmw']

colors = ['red', 'blue' , 'green']
poped_color = colors.pop() # can't be empty list
print(colors)  # ['red', 'blue']
print(poped_color)  # ['green']
colors.pop(0) #-1 or index should be in the range to prevent Error
print(colors) # ['blue']

numbers = ['one', 'two' , 'three', 'two']
numbers.remove('two') # Error if it is not in the list
print(numbers)  # ['one', 'three', 'two']


print(len(numbers))  # 3


users = ['joshep', 'claire' , 'david']
users.sort()
print(users)  # ['claire', 'david', 'joshep']
users.sort(reverse=True)
print(users)  # 'joshep', 'david', 'claire']

users_id = [10, 0 , 7]
users_id.sort()
print(users_id)  # [0, 7, 10]

users_id = [10, 0 , 7]
users_id_sorted = sorted(users_id) # keep the original inmutable
users_id_sorted_inverse = sorted(users_id, reverse=True) # keep the original inmutable
print(users_id)  # [10, 0, 7]
print(users_id_sorted)  # [0, 7, 10]
print(users_id_sorted_inverse)  # [10, 7, 0]

clients = ['joshep', 'claire' , 'david',  'zoe']
clients.reverse()
print(clients) # ['zoe', 'david', 'claire', 'joshep'] NO ALPHABETICAL, just reverse order