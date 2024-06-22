alien = {'color': 'green', 'speed': 'slow', 'size': 'lg'}
print(alien['color'])

#print(alien['size'])  #  error
print(alien.get('size')) # None
print(alien.get('size', 'there is not size')) # there is not size

print(len(alien)) # 2


# del alien['size'] # error
del alien['speed']

if 'color' in alien:
  print('has color')


for key, value in alien.items():
  print(f'key: {key}') # key: color key: size 
  print(f'value: {value}') # value: green  value: lg

users_colors = { "joan": 'red', 'smith': 'green' }
for key in users_colors.keys(): # ---> same that:   for key in alien:
  print(f'key: {key}') # key: joan key: smith

print(type(users_colors)) # <class 'dict'>

users_colors = { "joan": 'red', 'smith': 'green' }
for value in users_colors.values():
    print(f'value: {value}') # value: red value: green

## Execise:
favorite_languages = {'david': 'js', 'phil': 'py', 'edward': 'rust' }
friends = [ 'david','phil']

for name in favorite_languages:
  print(f'Hi {name.title()}')
  if name in friends:
      print(f'\tYou love {favorite_languages[name].title()}')
## end Execise

for name in sorted(favorite_languages):
  print(name) # david edward phil


### ---> SET
favorite_languages = {'david': 'js', 'phil': 'py', 'edward': 'rust', 'paul': 'rust' }

for lan in set(favorite_languages.values()):
  print(f'lan {lan}') # lan py lan js lan rust

languages = {'pyhon', 'rust', 'javascript'} # unique values