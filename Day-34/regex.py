import re

# pattern = r'[0-9]'
# text = 'codegnan'
# res = re.match(pattern,text)
# print(res.group() if res else "Pattern not found")

# pattern = r'[0-9]'
# text = 'codegnan2026'
# res = re.search(pattern,text)
# print(res.group() if res else "Pattern not found")

'''list of output'''

# pattern = r'[0-9]'
# text = 'codegnan 2026 python version 3.14'
# res = re.findall(pattern,text)
# print(res if res else "Pattern not found")

'''list of output'''

# pattern = r'[a-z]'
# text = 'codegnan 2026 python version 3.14'
# res = re.findall(pattern,text)
# print(res if res else "Pattern not found")

'''output and index of the output values'''

# pattern = r'[0-9]'
# text = 'codegnan 2026 python version 3.14'
# res = re.finditer(pattern,text)
# for i in res:
#     print(i.group(),i.start())

'''fullmatch text must equal to {10}'''

# pattern = r'[0-9]{10}'
# text = '9876543210'
# res = re.fullmatch(pattern,text)
# print(res.group() if res else "pattrn not found")

'''fullmatch text must equal to {5}'''

# pattern = r'[0-9]{5}'
# text = '9876543210'
# res = re.fullmatch(pattern,text)
# print(res.group() if res else "pattrn not found")

'''Split method using pattern'''

# pattern = r'[,(#]'
# text = 'java,python(html#css'
# res = re.split(pattern,text)
# print(res)

'''sub used to replace text with others'''

# pattern = r'[a-z]'
# text = 'python version 3.14, batch-63'
# res = re.sub(pattern,'*',text)
# print(res)

''''''

# pattern = r'e.t'
# text = 'e@t eaat eet eat ect Eghffjdt hjdfhgfj'
# res = re.findall(pattern,text)
# print(res)

'''^ chacks text starting with pattern or not'''

# pattern = r'^(91)'
# text = '9198765432'
# res = re.findall(pattern,text)
# print(res)

'''$ chacks text ending with pattern or not oterwise it give empty list[]'''

# pattern = r'32$'
# text = '9198765432'
# res = re.findall(pattern,text)
# print(res)


'''* gives the output according to the pattern text 
           if [to*] atleast it checks t and give t remove other char after t '''

# pattern = r'to*'
# text = 'to rtdjcjcn too tooo tooooo'
# res = re.findall(pattern,text)
# print(res)

# pattern = r'ab*'
# text = 'ab abb a abbbb abbbbb'
# res = re.findall(pattern,text)
# print(res)

'''+ gives the output according to the pattern text'''

# pattern = r'to+'
# text = 'to rtdjcjcn too tooo tooooo'
# res = re.findall(pattern,text)
# print(res)

pattern = r'91|0'
text = '05678'
res = re.findall(pattern,text)
print(res)

pattern = r'[aeiouAEIOU]'
text = 'codegnan programming'
res = re.findall(pattern,text)
print(res)





