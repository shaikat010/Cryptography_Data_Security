userhash = ['user1','user2','user3','user4','user5','user6','user7','user8','user9','user10']


passhash = ['pass1','pass2','pass3','pass4','pass5','pass6','pass7','pass8','pass9','pass10']

passconverthash = []
passlength = len(passhash)
# print(passlength)
# print("The string hash value is : " + str(hash(str_val)))

for i in range(passlength):
    passconverthash.append(str(hash(passhash[i])))

print(passconverthash)


def checkhashcollision():
    for i in passconverthash:
        res = []
        idx = passconverthash.index(i)
        for j in range(len(passconverthash)):
            if idx == j:
                continue
            res.append(i == passconverthash[j])
    print(res)


print(checkhashcollision())