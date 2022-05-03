
from main import Encore

filetype = input('What file type do you plan to work with')

fileName = input('Enter filename : ')
KeyValue = input('Enter key value: ')


print('Use the keywords  for commands e.g ENCf')
print("For Encrypting the full file: keyword 'ENCF' \nFor Decrypting the full file: keyword 'DECF'")
# print("for Encrprying one row: keyword 'ENCO' \nfor Decrypting one row: keyword 'DECO'")
# print("for Encrprying one column: keyword 'ENCC' \nfor Decrypting one column: keyword 'DECC'")
# print("for Encrypting more than one row: keyword 'ENCRS' \nfor Decrypting more than one row keyword: 'DECRS' ")
# print("for Encrypting more than one column: keyword 'ENCCS' \nfor Decrypting more than one row keyword: 'DECCS' ")

command = input('what do you plan to do with the file : ').upper()

ENDE = ['ENCF', 'DECF', 'ENCO', 'DECO', 'ENCC', 'DECC', 'ENCRS', 'DECRS', 'ENCCS', 'DECCS']

# multiple = ['ENCRS', 'DECRS', 'ENCCS', 'DECCS']


while command not in ENDE:
    print(f'command {command} not a valid request')
    command = input('what do you plan to do with the file : ').upper()

ecd = Encore('csv')
ecd.dataframe('annual-enterprise-survey-2020-financial-year-provisional-csv.csv')

Dict = {
    ecd.lock_allAph(KeyValue) : 'ENCF',
    ecd.unlock_allAph(KeyValue) : 'DECF'
}

print('running code .....')