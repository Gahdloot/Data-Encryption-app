import onetimepad
import pandas as pd

# To create a encrypted CSV file directly from the terminal


# create a list that nest all column
Top_Data = []


#  Where data is inputted in a for-loop
while True:
    c = input('Enter name: ')
    d = input('Enter Surname: ')
    e = input('Enter Tribe: ')
    f = input('Enter Age: ')

    ligga = [c, d, e, f]
    zulu = []

    for i in ligga:
        encoding = onetimepad.encrypt(i, 'password')
        zulu.append(encoding)

    Top_Data.append(zulu)

    o = input('To quit, press   333 :')

    if o == '333':
        break

#a list of column
names = []
password = []
occupation = []
aab = []


for l in Top_Data:
    for k, o in enumerate(l):
        if k == 0:
            names.append(o)
        elif k == 1:
            password.append(o)
        elif k == 2:
            occupation.append(o)
        else:
            aab.append(o)


# creating the table
Data = pd.DataFrame({
    'Names': names,
    'Password': password,
    'Occupation': occupation,
    'Average AB': aab
})


print(Data)

Data.to_csv('Encrypted.csv')


