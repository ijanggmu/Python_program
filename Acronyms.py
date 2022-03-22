user_input=str(input("Enter the phrase\n"))
text=user_input.split('.')
print(text)
a=" "
for i in text:
    a=a+str(i[0]).upper()
print(a)