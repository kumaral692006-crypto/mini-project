def stu(name,mark):
    if mark>=50:
        print(name,'pass')
    else:
        print(name,"fail")

a= input("enter ur name")
b=int(input("enter teh mark"))

print(stu(a,b))