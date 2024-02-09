import os
import re

for folder, subfolders, files in os.walk('C:\\Users\\RajanJasani\\Desktop\\Udemy Python BootCamp Course\\instructions'):
    flag = 0
    for f in files:
        with open(f'{folder}\\{f}','r') as sf:
            for line in sf.readlines():
                if re.search(r'\d{3}-\d{3}-\d{3}', line ):
                    flag = 1
                    number = re.search(r'\d{3}-\d{3}-\d{3}', line )
                    Number = number.group()
                    break
        
        if flag == 1:
            break

    if flag == 1:
        print('!TelePhone Number FOUND!')
        print(Number)
        break
