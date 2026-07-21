class student:
    grade = 10
    name = "ibrahim"

    def introduction(self):
        print("Hi i am a student")

    def details(self):
        print("My name is", self.name)
        print("i study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()