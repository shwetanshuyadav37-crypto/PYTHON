email = input('Enter email:')
password = input('Enter password:')
if email == 'login@gmail.com' and password == '898989':
    print('login succesfull')
elif  email == 'login@gmail.com' and password != '898989':
    print('password is incorrect')
    password = input('Enter the password again:')
    if email == 'login@gmail.com' and password == '898989':
        print('login successfull,finally')
    else:
        print('Tmse na ho payega!') 
else:
    print('login failed')
    
