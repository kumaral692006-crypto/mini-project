class stu:
    def __init__(self,name,regno,phone,address,branch):
        self.name=name
        self.regno=regno
        self.phone=phone
        self.address=address
        self.branch=branch
    
    def display(self):
        print("name",self.name)
        print("regno",self.regno)
        print("phone",self.phone)
        print("address",self.address)
        print("branch",self.branch)
    
a=stu("prabu","19231011","9710462461","chennai","bme")
b=stu("kumara","19231019","6382651627","chennai","bme")
c=stu("rahul","19231010","8825909204","chennai","bme")

a.display()
b.display()
c.display()