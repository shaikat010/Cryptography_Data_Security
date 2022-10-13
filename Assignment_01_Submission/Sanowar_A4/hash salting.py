passwords = ['pass', 'password', 'senha', 'password', 'picture', 'python', 'shaikatsir', 'pass', 'newpass', 'passsenha']
pass_list = len(passwords)

hashed_passwords_list = []
for i in range(pass_list):
    # the added i acts as a salt to prevent collisions
    hashed_passwords = hash(passwords[i]) + i
    hashed_passwords_list.append(hashed_passwords)

# this method checks for any collision occurrence
l1 = []
for i in hashed_passwords_list:
    if i not in l1:
        l1.append(i)
    else:
        print(i, end=' ')
