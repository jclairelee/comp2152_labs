class Person:
    def __init__(self, name, age, height):
        print("Constructing the Person object")
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

    # regular getter/setter
    # def get_name(self):
    #     return self.__name

    # def set_name(self, name):
    #     self.__name = name

    # Magic getter/setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height



    def __del__(self):
        print("The garbage collector is automatically deleting the Person object")


# Create an instance of Person
p1 = Person("Mark", 20, 6)

# Access public property
print(p1.public_prop)  # Should work

# Try accessing private property directly
try:
    print(p1.__name)  
except AttributeError as e:
    print("Error:", e)

# Use magic getter and setter
print("Name before:", p1.name)
p1.name = "Anna"
print("Name after:", p1.name)

# Create another instance to demonstrate property
p2 = Person("John", 25, 5.9)
print("Using property - Name:", p2.name)
p2.name = "Johnny"
print("Modified Name:", p2.name)
