string = str(input("Enter string: "))
str_abc = 'abc'
str_www = 'www'
str_zzz = 'zzz'
str_slice = string[0:3]
if str_abc in str_slice:
    print(string.replace(str_abc, str_www))
else:
    print(string + str_zzz)
