string = str(input("Enter string: "))
string_formatted = "".join([x for x in string if not x.isdigit()]).replace(" ", "")
print(string_formatted)