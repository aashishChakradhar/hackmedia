'''
    stores like in dictionary
    {
        'ram':
            {
                'maths' : 20,
                'science': 30,
            }
    }
'''

import json
'''
Example program
'''
# toSave = {
#     'student':['ram','shyam','hari','gita'],
#     'marks':[10,20,30,40]
# }
# with open ('fileHandeling/database_json.json','w') as jsfw:
#     json.dump(toSave,jsfw)

# with open('fileHandeling/database_json.json','r') as jsfr:
#     loadJson = json.load(jsfr)
# print(loadJson)

'''
    Task 3: WAP that first gives 2 options: 
    1. Sign up 
    2. Sign in 

    when 1 is pressed user needs to provide following information 
    1. Username, 2. Password, 3. Mobile number 
    All this information is saved in a file everytime a new user signs up the same file is updated 
    (hint Append over the same file)

    when 2 is pressed 
    User needs to provide username and password 
    this username and password is checked with username and password in the database
    if matched: 
    welcome to the device and show their phone number 
    else: 
    terminate the program saying incorrect credentials 


    Do it using json files, save everything to json and load from json 
'''

detail = {}
while True:
    found = False
    print('----'*20)
    choice = int(input('1. Sign Up\n2. Sign In\n0. Exit\nEnter your choice: '))
    print('----'*20)
    if choice == 1:
        username = input('username:\n')
        password = input('password:\n')
        phone = input('phone:\n')
        
        try:
            with open ('fileHandeling/user_json.json','r') as jsonRead:
                userDetail = json.load(jsonRead)
            userDetail.update({
                username : {
                    'password' : password,
                    'phone' : phone,
                },
            })
        except:
            print(f'File not found!!')

        with open ('fileHandeling/user_json.json','w') as jsonWrite:
            json.dump(userDetail,jsonWrite)

    elif choice == 2:
        print('----'*20)
        username = input('username:\t')
        password = input('password:\t')
        print('----'*20)
        with open('fileHandeling/user_json.json','r') as jsonRead:
            detail = json.load(jsonRead)

        for db_username,db_auth in detail.items():
            if db_username == username:
                found = True
                if db_auth['password'] == password:
                    print(f'Welcome to this device!!!\nPhone number: {db_auth['phone']}')
                    break
                else:
                    print(f'Invalid Password')
                    break
        if not found:
            print(f'User Not Found')
    else:
        break
