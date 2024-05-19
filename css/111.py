class Department:
    def __init__(self, s):
        self.semester = s
        self.name = "Default"
        self.id = -1
    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")

class CSE(Department):
    def __init__(self,n, i, s):
        super().__init__(s)
        self.name = n
        self.id = i
    def courses(self, *args):
        print("Courses Approved to this CSE student in", self.semester,"semester :")
        for i in args:
            print(i)

s1 = CSE("Rahim", 16101328,"Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
