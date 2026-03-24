class person:
    #class variable/properties
    head = 1
    legs = 2
    hands = 2

    #Instance variables
    #Constructor
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def modify(self):
       print("my old name is",self.name)
       new_name= input("enter new name:")

class mammal:
    Fur = True
    warm_blooded = True

    def __init__(self,legs,name,color):
        self.legs = legs
        self.name = name
        self.color = color

    def walk(self):
        print("I walk on my ",self.legs,"legs")


#object
human = mammal(2,"human","black")   
elephamt = mammal(4,"elephant","black")
whale = mammal(0,"whale","black")

class student:
    #class variable/school
    school = "Middle school"
    def __init__(self,grade,name,age):
        self.age = age
        self.name = name
        self.grade = grade

class shapes:
    #class variable
    def __init__(self,sides,name,):
        self.sides = sides
        self.name = name
#object
S1 = shapes(3,"Triangle")
S2 = shapes(5,"Pentagon")
S3 = shapes(6,"Hexagon")
S4 = shapes(8,"Octogon")
S5 = shapes(4,"Square")

#object
student1 = student(7,"Sebastian",13)
student2 = student(8,"Danstan",14)
student3 = student(6,"Barrack",13)
print(student1.name)

#object/instances
p1 = person("Sebastian",13,1.4)
p2 = person("Danstan",28,1.8)
p3 = person("Barrack",58,1.7)
p4 = person("Ian",19,1.6)
p5 = person("Abby",15,3.5)

name1 = "Sebastian"
name2 = "Dan"
name3 = "Barrack"
name4 = "Ian"
age1 = 13
age2 = 28
age3 = 58
age4 = 19


# print(p1.name)

p1.modify()