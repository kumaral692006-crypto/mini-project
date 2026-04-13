try:
    username=input("enter username")
    password=input("enter password")

    if username=="admin"and password =="1234":
        print("login successful")

    elif username== "" or password=="":
        raise ValueError("empty input kindly fill something")
    
    else:
        print("invalid username & password")

except ValueError as j:
    print("ERROR,j")