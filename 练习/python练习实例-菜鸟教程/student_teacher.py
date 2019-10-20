class people():
    def __init__(self, name):
        self.name=name
    def get_details(self):
        print(self.name)

class student(people):
    def __init__(self, name, branch,age):
        people.__init__(self,name)
        self.branch=branch
        self.age=age
    
    def get_details(self):
        print(self.name)
        print(self.branch)
        print(self.age)
    @property
    def getAge(self):
        return self.age

student1=student("zwish","college",12)
student1.get_details()
print("年龄:{0}".format(student1.getAge))