import re

string1 = 'hello how are you'
output = re.match('[h]', string1)
print(output)

# Match string if first character is starting with h or i or j
match_char = re.findall("^[hij]", string1)
print(match_char)

# Match string if first character is small a to z
match_char = re.findall("^[a-z]", string1)
print(match_char)

# Match string if first character is small a to z , capital A to Z or 0 to 9
match_char = re.findall("^[a-zA-Z0-9]", string1)
print(match_char)

# Match if string starts with one or more occurrence of a
# For example string ab valid, string aaaab valid, string ba not valid
match_char = re.findall("^[a+]", string1)  # Method 1
match_char = re.match("a+", string1)  # Method 2
print(match_char)

# Match if string starts with zero or more occurrence of a
# For example string ab valid, string aaaab valid, string ba valid
match_char = re.match("a*", string1)
print(match_char)

# Match if strings first character is a rest is anything :=> aaahvu  > valid
match_char = re.match("a.", string1)
print(match_char)

# Match if string starts with hi
match_char = re.match("hi", string1)
print(match_char)

# Match if string starts with hello or hi
match_char = re.match("^hi|hello", string1)
print(match_char)

# Match if strings first 2 characters are small.
match_char = re.match("[a-z][a-z]", string1)
print(match_char)

# Mobile number : Match  if first digit is 6 or 7 or 8 or 9, remaining between 0 to 9. ( Total length must be 10 )
match_char = re.match("[6-9][0-9]{9}", string1)
print(match_char)

# match string if first 5 to 7 charatcters must be digit rest anything
print(re.match('[0-9]{7}?', string1))

# match if first 5 to 7 characters must not be digit rest anything
print(re.match('![0-9]{7}?', string1))

# match if first must be word
print(re.match('[a-zA-Z]', string1))

# match if first not word
print(re.match('[0-9]', string1))

# match if first character must not a
print(re.match('[^a]', string1))

# fIRST WORD OF STATEMENT must not be hello
print(re.match('[^(hello)]', string1))

# first character must not be a or b
print(re.match('[^ab]', string1))

# String starts with word "you" valid
print(re.match('\Ayou', string1))

# string ends with word "you" valid
print(re.findall(r'you\b', string1))

# Search word hello anywhere in string
print(re.findall('hello', string1))

# Search any where wh** wh** ( what, when )
print(re.findall('wh*', string1))

# number plate validation GJ25CL2356
print(re.findall('[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$', string1))

# accept age between 50 to 99
print(re.match('[5-9][0-9]$', string1))

# 18 - 99 age validation
print(re.match('1[8-9]$|[2-9][0-9]$', string1))

# find space in statement
print(re.findall(' ', string1))  # we can use \s inside ' ' like '\s'

# split statement by 2 spaces:
# 	example : hi how are you
# 	hi, ho , are you?
print(re.split(' ', string1, 2))

# split by specific word : word how
# 	hello how are you
# 	hello, are you
print(re.split('how', string1))
