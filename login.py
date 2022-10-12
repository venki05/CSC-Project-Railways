import random
def login_credentials():
    while True:
        uid=input("enter the user id: ")
        pwd=input("enter the password: ")
        if uid=="irctc" and pwd=="railway":
            print("login successful")
            return
        else:
            continue

def pnr():
    s=''
    for i in range(10):
        s+=str(random.randint(0,10))
    return s

        
