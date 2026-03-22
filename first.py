import os
# password =   input("Enter your password: ")
# if  password == "dev_ops":
#    print("welcome user !")
# else:
#    print("Wrong password !")+

# internet_avalible =  True
# if internet_avalible:
#    print("play valorant ")
# else:
#    print("read a book !")

# furniture = input("Choose type of furnitures you want to buy \nGold, \nuchtalik, \nbeshtalik \n: ")
# furniture = furniture.lower()

# if furniture == "gold":
#    print("price is 3000 0000 uzs")
#    print("color is brown ")
#    print("size is 3x2 ")

# elif furniture == "uchtalik":
#    print("price is 4000 000 uzs")
#    print("color is black")
#    print("size is 2x1")

# elif furniture == "beshtalik":
#    print("price is 600 000  uzs")
#    print("color is seri")
#    print("size is 3x4")
# else:
#    print("we dont have thise type of furniture !")

# is_door_open = False
# if is_door_open:
#    print("go in and get lunch")
# else:
#    print("call mom and ask the keys")

# fruits = ["apple","pomegranate","banana", "date", "orange", "apelsin"]
# if len(fruits) >= 5:
#    print("you must minimize the list")
# else:
#    print("that's fine")

# english = input("Do you know english ? (yes/no): ")
# age = int(input("Enter your age: "))

# if age >30:
#     print("you are too old to apply")
# elif english == "yes" and age >= 18:
#     print("you can aplly")
# elif age <18:
#       print("you are too young to apply")

# elif english == "no":
#     print("you should know english to apply")
# else:
#     print("please recheck your answers")

# print("Welcome to the store")
# payment = input("Choose your payment method \ncash, \ncard \n: ")
# if payment == "cash" or payment == "card":
#     print("accept payment")
# else:
#     print("reject the payment")

# is_pepsi =False
# money = 6000
# if money >= 7000 and is_pepsi:
#     print("get !")
# else:
#     print("leave !")

# username = ""
# password = ""
# is_active = False
# if username:
#     if password:
#         if is_active:
#             print("login succesfull")
#         else:
#             print("account is not active")
#     else:
#         print("password required")
# else:
#     print("username required")


# names = ("sam","tom","leo","john","sam")
# print(names)

# books = {
#     bool : {
#         "name" : "metammorfoz",
#         "author" : "frans kafka",
#         "year" : 1918

#     },
#     book2 : {
#         "name" : "hundred years of loneliness",
#         "author": "ernest heminguey",
#         "year" : "1920"
#     },
    
# }


# my_dict = dict(book)
# print(my_dict)

# for x in book.items():
#     print(x)

# book.clear()
# print(book)

# book.update({"year": 1920})
# print(book)
# x = book.values()
# print(x)
# book["genre"] = "novel"
# print(x)

# y = book.items()
# print(y)

# if 1918 in book:
#     print("it is in the dict")
# else:
#     print("it not in the dict")

# fruits = ["apple", "peanut", "peach", "kiwi"]
# name = input("Enter your name to get the list: ")

# while not name != "xabibillo":
#     print("name is not valid")
#     name = input("Enter your name to get the list: ")

# location = input("Enter the city you live in: ")
# while not location != "andijon":
#     print("location is not valid")
#     location = input("Enter the city you live in: ")

# for x in fruits:
#     print(x)

# fruits = ["apple", "peanut", "peach", "kiwi"]

# # Validate name
# name = ""
# while name != "xabibillo":
#     name = input("Enter your name to get the list: ")
#     if name != "xabibillo":
#         print("name is not valid!")

# # Validate location
# location = ""
# while location != "andijon":
#     location = input("enter the city you live in: ")
#     if location != "andijon":
#         print("location is not valid!")

# # Print fruits
# print("\nHere are the fruits:")
# for x in fruits:
# #     print(x)

# fruits = ["apple","banana","cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
    
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2024
# }

# print(car["model"])

# car["color"]  = "red"

# car.pop("brand")
# print(car)
# def  movie_info(name, director, year):
#     print(f"{name} ,directed by {director}, released in {year}")
# movie_info(director="christopher nolan", year = 2010, name = "inception")

# def multiply_all(*numbers):
#     result = 1
#     for n in numbers:
#         result *= n
#     print(result)
# multiply_all(2,3,4)

# x = 10
# def my_func():
#     y = 5
#     print("inside function:", x, y)
# my_func()
# print("outside function:", x)

# f = open("fruits.txt")
# # print(f.readline())
# # print(f.readline())
# for line in f:
#     print(line)
# f.close()

# f = open("fruits.txt", "a")
# f.write("banana\n") 
# f.close()

# f = open("fruits.txt")
# print(f.read())
# f.close()

# f = open("fruits2.txt", "w")
# f.write("i've deleted all items !")
# f.close()

# f = open("fruits2.txt")
# print(f.read())
# f.close()

# with open("fruits.txt", "w") as f:
#     f.write("ooh i deleted the content !")


# with open("fruits.txt") as f:
#     print(f.read())jechgfxwud


#from laptop import Laptop
# laptop_1 = Laptop("hp",  "amd ryzen", "amd vega radeon", "8 gb", True)
# laptop_2 = Laptop("dell",  "intel cor i 5", "intel uhd graphigs", "16 gb", True)
# laptop_3 = Laptop("macBook",  "amd ryzen 7", "rtx 5060", "32 gb", True)

# laptop_1.watch()
# laptop_1.turn_off()

# is_weekend = False
# is_sunny = True
# have_money = True

# if is_weekend and is_sunny and have_money:
#     print("hang out with friends")
#     print("play football")
#     print("go to bar")
# elif is_weekend == False and is_sunny and have_money:
#     print("go to work")

# elif is_weekend and is_sunny and have_money == False:
#     print("go to grandma's house !")
# elif is_weekend and is_sunny == False and have_money:
#     print("take a bath")
# else:
#     print("stay at home")     
  
# import turtle
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(0)
# turtle.title("my shape")

# colors = ["blue", "red", "green", "white"]
# for i in range(500):
#     t.color(colors[i % len(colors)])
#     t.forward(i)
#     t.backward(100)
#     t.left(100)
# t.done()
''' inheritence = allows a class inherit attributes and methods from another class
                  and helps with code reusibilty and extensibility '''
# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def studying(self):
#         print(f"{self.name} is studying")

# class Child1(Parent):
#     def hobby(self):
#         print(f"{self.name}'s hobby is reading !")

# class Child2(Parent):
#     def hobby(self):
#         print(f"{self.name}'s hobby is drawing!")

# child1 = Child1("sam", 13)

# child2 = Child2("emy", 16)

# print(child2.name)
# print(child2.age)
# child2.studying()
# child2.hobby()



# multiple inheritence =  child classes can inherit attributes and methods from multiple parent classes
# multilevel inheritence = parent classes can inherit from parent classes
# class Grandparent():
#     def __init__(self, name):
#         self.name = name
#     def go(self):
#         print(f" {self.name}  can go to grandparent's house")

# class Mother(Grandparent):
#     def hug(self):
#         print(f" {self.name} can hug the mother")
    
# class Father(Grandparent):
#     def talk(self):
#         print(f" {self.name}  can talk to a father")

# class Daughter(Mother):
#     pass

# class   Boy(Father):
#     pass
# class Baby(Mother, Father):
#     pass

# daughter = Daughter("emy")
# boy = Boy("sam")
# baby = Baby("little john")

# baby.hug()

# super() = 
# class Person:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location

# class Student(Person):
#     def __init__(self,name, grade, location):
#      super().__init__(name,location)
#      self.grade = grade
#     def __str__(self):
#         return f"name: {self.name} | Grade: {self.grade}, | University: {self.location}"
# student = Student("ali", 4, "priston university")

# print(student)
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

# class Car(Vehicle):
#     def __init__(self, brand, speed, num_doors):
#         super().__init__(brand, speed)
#         self.num_doors = num_doors

#     def __str__(self):
#         return f"brand: {self.brand} | speed: {self.speed} | number of doors: {self.num_doors}"

# car = Car("bmw", "100 mph", 4)

# print(car)

# from abc import ABC , abstractmethod

# class User(ABC):
#     def __init__(self,name):
#         self.name = name

#     @abstractmethod
#     def login(self):
#         pass

# class Seller(User):
#     def login(self):
#         print(f"{self.name} logged in as seller")
    
# class Buyer(User):
#     def login(self):
#         print(f"{self.name} logged in as buyer")

# seller = Seller("xurshidbek")
# seller.login()

# buyer = Buyer("xabibillo")
# buyer.login()
# class Car:
#     def move(self):
#         print("you moved the car")

# class Bike:
#     def move(self):
#         print("you moved the bike")
# class Bout:
#     def move(self):
#         print("you are driving the bout")

# class Bus:
#     def move(self):
#        print("you are driving the bus")

# class Person:
#     def move(self):
#         print("person is walking")
# vehicles = [Car(), Bike(), Bout(), Bus(), Person()]

# for vehicle in vehicles:
#     vehicle.move()

# class Author:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"title: {self.title} | author: {self.author.name} | age: {self.author.age}"
 
# author = Author("azz", 27)
# print(author.name)
# print(author.age)
# book = Book("red hand", author)
# print(book)


# class Chapter:
#     def __init__(self, title):
#         self.title = title


# chapter = Chapter("olle")

# print(chapter.title)
# magic methods == Dunder methods (double underscore) __init__, __str__, __eq__, __lt__, __gt__, __add__, __contains__, __getitem__,
#       they are automatically called by python's built-in opartions
#        they allow developers to define or customize the behavior of objects
# class Club:
#     def __init__(self, name, nums_league_title, nums_super_league_title):
#         self.name = name
#         self.__nums_league_title = nums_league_title
#         self.nums_super_league_title = nums_super_league_title
   
 
#     def __str__(self):
#         return f" '{self.name}',  {self.nums_league_title},   {self.nums_super_league_title}"

#     def __eq__(self, other_club):
#         return self.nums_league_title == other_club.nums_league_title and self.nums_super_league_title == other_club.nums_super_league_title

#     def __gt__(self, other):
#         if self.nums_league_title > other.nums_league_title:
#             return f"{self.name} is better than {other.name}"

#     def __lt__(self, other):
#         if self.nums_super_league_title < other.nums_super_league_title:
#             return f"{self.name} is smaller club than {other.name}"

#     def __add__(self, other):
#         return f"{self.nums_super_league_title + other.nums_super_league_title} numbers of super league titles"

#     def __contains__(self, keyword):
#         return keyword in self.name

#     def __getitem__(self, key):
#         if key == "name":
#             return self.name
#         elif key == "nums_league_title":
#             return self.nums_league_title
#         elif key == "nums_super_league_title":
#             return self.nums_super_league_title
#         else:
#             return f"key '{key}' is not found !"
# club_a = Club("real madrid", 20, 15)
# club_b = Club("barcelona", 10, 5)
# club_c = Club("man city", 7, 5)

# print(club_c["nums fan"])

# class Shopping_cart:
#     def __init__(self, price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price

#     @staticmethod
#     def is_valid_price(amount):
#         return amount > 0

#     @classmethod
#     def create_empty_list(cls):
#         return cls(2)

# # static method
# print(Shopping_cart.is_valid_price(800))   # True
# print(Shopping_cart.is_valid_price(-100))  # False

# # class method
# empty = Shopping_cart.create_empty_list()
# print(empty.price)  # 0

# # property
# cart = Shopping_cart(700)
# print(cart.price)  # 
with open("main.py","w") as f:
    f.write()