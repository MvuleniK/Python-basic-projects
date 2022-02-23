#Password Authentication System

# A password authentication system is designed to autheticate
# a user through a logical based system. In addtion, this logical
# based system also identifies the user with respect to the account



import getpass # this calls the respective library for this code

# The databased of the user
userdatabase = {'mjili@gmail.com':'2468','jackvi@gmail.com': '36912'}
username = input('Enter Your Username: ')

userpassword = getpass.getpass('Enter Your Password:')

for i in userdatabase.keys():
    if username == i:
        while userpassword != userdatabase.get(i):
            userpassword = getpass.getpass('Enter Your Password Again:')
        break
print('Verified')