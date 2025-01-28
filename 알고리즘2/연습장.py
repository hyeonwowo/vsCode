class Student:
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print("=================")
        print(f"name {self.name}")
        print(f"age {self.age}")
        print(f"major {self.major}")
        print("=================")

    def changeMajor(self,new_major):
        print(f"change major : {self.major} -> {new_major}")
        self.major = new_major


student1 = Student("son",31,"LW")
student2 = Student("kane",30,"ST")
student3 = Student("kross",34,"MF")

student1.introduce()
student2.introduce()
student3.introduce()

student2.changeMajor("RW")
student2.introduce()