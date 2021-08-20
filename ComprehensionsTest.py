nums = [1,2,3,4,5,6,7,8,9,10]


# 1. Beispiel: Quadrieren

my_list = []
for n in nums:
    my_list.append(n*n)
print (my_list)

# List comprehension: Alle n*n in nums
my_list = [n*n for n in nums]
print (my_list)


# 2. Beispiel: Nur gerade Zahlen

my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

    # Als List-Comprehensions
my_list = [n for n in nums if n % 2 == 0]
print(my_list)


# 3. Beispiel: verschachtelte For-Schleifen
my_list = []
for letter in 'abcd':
    for nums in range(4):
        my_list.append((letter, nums))
print(my_list)

    # Als List-Comprehensions
my_list = [(letter, nums) for letter in 'abcd' for nums in range(4)]
print(my_list)



# 4. Beispiel: Dictionary Comprehensions

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman', 'Superman', 'Spiederman','Wolverine', 'Deadpool']
print (zip(names,heros))

my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)

    # Als List-Comprehensions
my_dict = {name: hero for name, hero in zip(names,heros)}
print(my_dict)
    # Als List-Comprehensions ohne einen bestimmten Eintrag
my_dict = {name: hero for name, hero in zip(names,heros) if name != 'Peter'}
print(my_dict)
