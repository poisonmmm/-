class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.sex)


class Student(Person):
    def __init__(self, name, age, sex, college, class_num):
        Person.__init__(self, name, age, sex)
        self.college = college
        self.class_num = class_num

    def personInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.sex)
        print("学院：", self.college)
        print("班级：", self.class_num)

    def study(self, Teacher):
        x = Teacher.teachObj()
        print("老师", x, "我终于学会了！")


class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        Person.__init__(self, name, age, sex)
        self.college = college
        self.professional = professional

    def personInfo(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.sex)
        print("学院：", self.college)
        print("专业信息：", self.professional)

    def teachObj(self):
        return "今天讲了如何用面向对象设计程序"


student1 = Student("mike", 18, "男", "计算机学院", "1班")
student2 = Student("jack", 17, "男", "计算机学院", "2班")
student3 = Student("lucy", 18, "女", "计算机学院", "3班")
teacher1 = Teacher("bob", 35, "男", "计算机学院", "智科")
student1.personInfo()
student2.personInfo()
student3.personInfo()
teacher1.personInfo()
student1.study(teacher1)
