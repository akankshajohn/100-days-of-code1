text = input('Enter a String:')
print(text)

length = len(text)
text_rev = ""
while length>0:
   text_rev += text[length-1]
   length = length-1

print(text_rev)
