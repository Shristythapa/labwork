#Takeusername and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".
for i in range(3):
    username="username"
    password="password"
    a=input("enter username")
    b=input("enter password")
    if a==username and b==password:
        print("logged in sucessfully")
    else:
        print("invalid credintial")
print("attempt finished")
