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


magicians = ['alice', 'carol', 'paul']
for magician in magicians:
  print(f'This is {magician}')

for val in range(2,6):
  print(val) # 2 3 4 5 (6 is not printed )

  print(range(6)) #  = print(range(0, 6))

numbers_list = list(range(0,6))
print(numbers_list) # [0, 1, 2, 3, 4, 5]

event_numbers = list(range(2, 11, 2)) # starts in 2 and add +2 until 11 (not included)
print(event_numbers) # [2, 4, 6, 8, 10]

digits = [1,2,3,4,5,6]
print(min(digits)) # 1
print(max(digits)) # 6
print(sum(digits)) # 21

square = [value**2 for value in range(1, 11)]
print(square) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

###

desserts = ["1 - cake", "2 - lemon pie", "3 - cheekcase", "4 - muffin"]
print(desserts[0:2]) # "1 - cake", "2 - lemon pie"
print(desserts[:2]) #  "1 - cake", "2 - lemon pie"
print(desserts[2:]) # "3 - cheekcase", "4 - muffin"
print(desserts[-3:]) # "2 - lemon pie", "3 - cheekcase", "4 - muffin"
print(desserts[:]) # ["1 - cake", "2 - lemon pie", "3 - cheekcase", "4 - muffin"]

# my_favorite_dessert = desserts[:].append('macarrons') # DOESN'T WORK : None
my_favorite_dessert = desserts[:]
my_favorite_dessert.append('macarrons')

print(desserts)
print(my_favorite_dessert)

### TUPLAS
dimension = (20, 40)
dimension = (20,)
dimension = 20,
print(type(dimension)) # <class 'tuple'>

toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in toppings) # True
print('sugar' not in toppings) # True

user_list = []
if not user_list:
  print('Is a empty list')