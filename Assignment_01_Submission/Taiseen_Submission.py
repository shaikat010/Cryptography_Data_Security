'''
Origination : Creative It Institute
Subject     : Blockchain
Assignment  : Cryptography | Assignment number 04
Teacher     : Shaikat Majumder
Student     : Md Taiseen Azam
'''

import hashlib
import random
import json
import sys


'''
Question 3. 

'''

total_hash_collisions = {}
user_name_and_password = {}
user_name_and_hash_password = {}
temporary_save_hash_passwords = []

username = ['Jon', 'Sam', 'Max', 'Zen', 'Ben',
            'Raj', 'Bob', 'Tom', 'Neo', 'Taj']

passwords = [
    '12345678',  # 01
    '00000000',  # 02
    '12345678',  # 03
    '22227777',  # 04
    '12345678',  # 05
    '11111111',  # 06
    'abcdefgh',  # 07
    '00000000',  # 08
    '22227777',  # 09
    '11111111',  # 10
]

# by 2 list, make a user name & password (key:value) pair dictionary
for index in range(len(username)):
    user_name_and_password[username[index]] = passwords[index]

print(json.dumps(user_name_and_password, indent=2))


# creating hash ==> from simple string password
for single_password in passwords:

    hashPass = hash(single_password)

    # prevent being for negative password hashing number...
    if hashPass < 0:
        hashPass += sys.maxsize
        temporary_save_hash_passwords.append(hashPass)
    else:
        temporary_save_hash_passwords.append(hashPass)


# count how many hash collisions happen in password hash list...
def detects_hash_collisions(hash_list):

    for single_hash in hash_list:

        # if multiple number occurs found...
        if hash_list.count(single_hash) > 1:
            
            duplicateHash = ('happen {t} times').format(t = hash_list.count(single_hash))

            total_hash_collisions[single_hash] = duplicateHash


# function call for hash collisions detection...
detects_hash_collisions(temporary_save_hash_passwords)

print('=================================================================> Answer 3')
print(json.dumps(total_hash_collisions, indent=2))
print('Total number of password hash collision found :',
      len(total_hash_collisions))


'''
Question 4. 

'''


def prevent_hash_collisions(hash_pass_list):

    for index in range(len(hash_pass_list)):

        salt = random.randint(100, 999)

        saltPass = str(hash_pass_list[index]) + str(salt)

        hashPass = hashlib.md5(saltPass.encode())

        user_name_and_hash_password[username[index]] = hashPass.hexdigest()


print('=================================================================> Answer 4')
prevent_hash_collisions(temporary_save_hash_passwords)
print(json.dumps(user_name_and_hash_password, indent=2))



'''
Question 5. 

'''


def possible_number_of_keys(key_length, choices_per_key):

    possible_unique_keys = choices_per_key ** key_length

    return 'Possible unique number of keys : {:,}'.format(possible_unique_keys)


print('=================================================================> Answer 5')
print(possible_number_of_keys(3, 26))
print(possible_number_of_keys(6, 26))
print(possible_number_of_keys(8, 36))
