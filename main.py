# list behave as a C pointer
lista = ['a', 'c', 'b', 'x']
new_list = lista
lista[0] = 'z'
print(new_list)

# list unpacking
a, b, *other, c = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(other)
print(c)
# dictionary declarations
user = {
    'basket': [1, 2],
    'greet': '',
    'age': 20
}

user2 = dict(name='Jones')

# set
my_set = {1, 2, 3}


print(1 in my_set)


a = [1, 2, 3]
b = a

print(a is b)
print(a == b)

# for loop in dict
for item in user.items():
    key, value = item
    print(key, value)

# In a more simple-way
for key, value in user.items():
    print(key, value)

for i, char in enumerate("Helloo"):
    print(i, char)

# While with else aplication
while i < 50:
    print(i)
    i += 1
    break
else:
    print('Done with all the work')

# break, continue and pass
for i, char in enumerate("Helloo"):
    continue
    print(i, char)

for i, char in enumerate("Helloo"):
    # THINKING ABOUT IT
    pass

# Default Parameters


def say_hello(name='Darth Vader', emoji='😈'):
    print(f'hello {name}{emoji}')


say_hello()


# Positional arguments
say_hello('😍', 'Didier')
say_hello('Didier', '😍')

# Keyword arguments
say_hello(emoji='😍', name='Rodrigo')
say_hello('Timmy')

# Return function


def sum_values(n1, n2):

    def another_func(n1, n2):
        return n1 + n2

    return another_func(n1, n2)


total = sum_values(10, 20)
print(total)


def sum_values_b(n1, n2):

    def another_func(n1, n2):
        return n1 + n2

    return another_func(n1, n2)


total = sum_values_b(10, 20)
print(total)

# Docstrings


def test(a):
    '''
    Info: This func. tests and print param a
    '''
    print(a)


# help(test)
print(test.__doc__)
test('ma oe')

# *args and **kwargs


def get_sum(*args):
    print(args)
    return sum(args)


print(get_sum(1, 2, 3, 4, 5))


def get_sum_2(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(get_sum_2(1, 2, 3, 4, 5, num1=1, num2=10))

# Scope
a1 = 1


def confusion1():
    a1 = 5
    return a1


print(confusion1())
print(a1)  # 1, 5

a2 = 1


def confusion2():
    a2 = 5
    return a2


print(a2)
print(confusion2())  # 5, 1

a3 = 1


def parent_confusion3():
    a3 = 10

    def confusion3():
        return a3

    return (confusion3())


print(parent_confusion3())
print(a3)  # 10 , 1
a4 = 1


def parent_confusion4():

    def confusion4():
        return a4

    return (confusion4())


print(parent_confusion4())
print(a4)  # 1 , 1


def parent_confusion5():

    def confusion5():
        return sum

    return (confusion5())


print(parent_confusion5())
print(a4)  # <built-im function sum>, 1

# Global Keyword
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# Non local keyword


def outer():
    x = 'local'

    def inner():
        nonlocal x  # call the parent x memory. Value x = 'local'
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
t

# %%


# %%
print("a")
# %%
print("a")

# OOP


class BigObject:  # class (planta de uma casa)
    # code
    pass
t

obj1 = BigObject()  # instanciate
obj2 = BigObject()  # instanciate
obj3 = BigObject()  # instanciate
obj4 = BigObject()  # instanciate
print(type(BigObject))
print(type(obj1))


# object for HP game

class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, age):
        if (self.membership):
            self.name = name  # atributes
            self.age = age

    def run(self):  # method
        print('run')
        return 'done'


player1 = PlayerCharacter('Rodrigo', 26)
player2 = PlayerCharacter('Camy', 16)
player2.attack = 50
print(player1.name)
print(player1)

print(player2.attack)


class PlayerChar2:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if(age > 18):  # check before instaciate
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_nums(cls, num1, num2):
        return num1 + num2

    @classmethod
    def add_instance(cls, num1, num2):
        return cls('Naruto', num1 + num2)

    @staticmethod
    def add_static_num(num1, num2):
        return (num1 + num2)


player3 = PlayerChar2()
player4 = PlayerChar2('rod', 19)  # if age < 18 -> AttributeError, else: print.
print(player4.shout())
print(player4.adding_nums(2, 3))
PlayerChar2.add_instance(4, 7)
PlayerChar2.add_static_num(3, 6)
#  print(player1.attack)

#  encapsulation

class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, age):
        if (self.membership):
            self.name = name  # atributes
            self.age = age

    def run(self):  # method
        print('run')
        return 'done'

#  inheritance
class User:
    
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
    #   super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print('ataque com: {}'.format(self.power))

class Archer(User):

    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print('atacando com arrows: arrows left de {}'.format(self.num_arrows))

archer1 = Archer('Robin',100)
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

print(wizard1.email)
print(archer1.attack())
archer1.attack()
print(wizard1.attack())

print(isinstance(wizard1,Wizard))

#polymorphism
# diferentes obj classes atributes 

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [archer1, wizard1]:
    char.attack()



#Encapsulation - Abstraction - inheritance - Polymorphism


# .super()

# introspection
print(dir(wizard1))
wizard1.__doc__

# dubder metods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return('yess??')

action_figure = Toy('red', 12)
print(action_figure.__str__())
print(str('action_figure'))
print(len(action_figure))

# some dunder methods have a special way to be called
print(action_figure())

