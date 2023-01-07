import bcrypt

password = password.encode('utf-8')

hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 

check = str(input("check password: ")) 
 
check = check.encode('utf-8') 

if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")