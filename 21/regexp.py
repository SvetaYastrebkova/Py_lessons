import re


# methods:
'''
search() -> get first match
match() -> get first match from string first symbol
fingall() -> get list of tuples -> groups
finditer() -> iterator for all mantches
'''

# pattern string:
EMAIL_PATTERN_STR = r'([\w\.-]+)@([\w\.-]+)'
TARGER_STRING = '''
id,first_name,last_name,email,gender,ip_address
1,D'arcy,Benge,dbenge0@friendfeed.com,Male,93.228.107.140
2,Kelcy,Hakonsson,khakonsson1@washingtonpost.com,Female,181.93.173.27
3,Jerrilee,Velasquez,jvelasquez2@dell.com,Non-binary,212.142.76.100
4,Carola,Pirri,cpirri3@techcrunch.com,Female,220.2.253.47
5,Even,Butterly,ebutterly4@bloglines.com,Male,230.206.172.123
6,Leisha,Shellibeer,lshellibeer5@java.com,Female,82.210.124.168
7,Abdul,Garlette,agarlette6@flickr.com,Male,166.95.106.164
8,Arther,Samet,asamet7@icq.com,Male,190.183.101.142
9,Ev,Mewrcik,emewrcik8@archive.org,Male,49.75.241.142
10,Enrico,Lambin,elambin9@moonfruit.com,Male,5.104.249.62
'''

# search
# version 1
res = re.search(EMAIL_PATTERN_STR, TARGER_STRING)  # -> match object Match[str]
print(res) # <re.Match object; span=(64, 86), match='dbenge0@friendfeed.com'>
print(type(res)) # <class 're.Match'>
print(res.start()) # 64
print(res.end()) # 86
print(res.span()) # (64, 86)
print(res.group()) # dbenge0@friendfeed.com
print(res.group(0)) # dbenge0@friendfeed.com
print(res.group(1)) # dbenge0
print(res.group(2)) # friendfeed.com
print(res.groups()) # ('dbenge0', 'friendfeed.com')

EMAIL_PATTERN_STR = r'(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+)'
for group in re.search(EMAIL_PATTERN_STR, TARGER_STRING).groups():
    print(f'{group=}') 
    '''
    group='dbenge0'
    group='friendfeed.com'
    '''
    pass

print(re.search(EMAIL_PATTERN_STR, TARGER_STRING).group('username')) # dbenge0


# filndall

find_all_res = re.findall(EMAIL_PATTERN_STR, TARGER_STRING)
print(type(find_all_res)) # <class 'list'>

for res in find_all_res:
    print(type(res))
    print(f'Username = {res[0]:20}  domain = {res[1]}  ')

'''
Username = dbenge0               domain = friendfeed.com  
Username = khakonsson1           domain = washingtonpost.com  
Username = jvelasquez2           domain = dell.com  
Username = cpirri3               domain = techcrunch.com  
Username = ebutterly4            domain = bloglines.com
Username = lshellibeer5          domain = java.com
Username = agarlette6            domain = flickr.com
Username = asamet7               domain = icq.com
Username = emewrcik8             domain = archive.org
Username = elambin9              domain = moonfruit.com
'''    

# finditer
for next_match in re.finditer(EMAIL_PATTERN_STR, TARGER_STRING):
    print(type(next_match))
    print(next_match)
    pass


# flags
'''
re.DEBUG
re.MULTILINE
re.ASCII vs re.UNICODE
re.IGNORECASE
'''

for next_match in re.finditer(EMAIL_PATTERN_STR, TARGER_STRING, flags=re.DEBUG):
    print(type(next_match))
    print(next_match)
    pass


# functions sub()   , split()

res = re.sub(EMAIL_PATTERN_STR,'****', TARGER_STRING)
print(res)
'''
id,first_name,last_name,email,gender,ip_address
1,D'arcy,Benge,****,Male,93.228.107.140
2,Kelcy,Hakonsson,****,Female,181.93.173.27
3,Jerrilee,Velasquez,****,Non-binary,212.142.76.100
4,Carola,Pirri,****,Female,220.2.253.47
5,Even,Butterly,****,Male,230.206.172.123
6,Leisha,Shellibeer,****,Female,82.210.124.168
7,Abdul,Garlette,****,Male,166.95.106.164
8,Arther,Samet,****,Male,190.183.101.142
9,Ev,Mewrcik,****,Male,49.75.241.142
'''

res = re.split(r'\n?\d+,', TARGER_STRING)
print(res)


text = "Python is Great and Powerful"
result = re.findall(r"[A-Z][a-z]+", text)
print(result)  # 👉 ['Python', 'Great', 'Powerful']


text = "test@mail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, text):
    print("Valid email")
else:
    print("Invalid email")

#Замена всех цифр на #
text = "My number is 12345"
new_text = re.sub(r"\d", "#", text)
print(new_text)  # 👉 My number is #####


