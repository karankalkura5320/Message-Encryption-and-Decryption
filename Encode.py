#Encoder

shift = int(input('enter the shift:'))

data= input('enter the data:')

for i in data:
    if i==' ':
        print('', end='')
    else:
        if i.isupper():
            if (ord(i)+shift) < 91:
                print(chr(ord(i)+shift), end='')
            elif (ord(i)+shift) >= 91:
                print(chr(ord(i)+shift-26), end='')
        elif i.islower():
            if (ord(i)+shift) < 123:
                print(chr(ord(i)+shift), end='')
            elif (ord(i)+shift) >= 123:
                print(chr(ord(i)+shift-26), end='')
