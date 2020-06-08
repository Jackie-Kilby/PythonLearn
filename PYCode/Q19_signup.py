print("--------------Welcome to Sign up---------------")
database = []
while True:
    username = input('User name:')
    password = input('Password:')
    repassword = input('Please repeat password:')
    email = input('Email:')
    phone = input('Phone Num:')
    
    user = {}

    if password == repassword:
        user['password'] = password
    else:
        print('Password is not the same, pls input again')
        continue

    user['name'] = username
    user['email'] = email
    user['phone'] = phone

    database.append(user)

    another = input('Sign up another? (y/n):')
    
    if another!='y':
        break
        
print(database)
