##string --- sequence of characters
##string -- it is immutable(unchangable) --- add, remove ,delete , update , sort
##string -- it is ordered

## string is denoted by -- single cots '' , double cots "", Triple cots """ """
## triple cots -- used for writing multiline of code 
 
name = "Kamlesh"
n1 = " saini"
print(name)
 
text = "my name is "+ name
print(text)
 
 # to add two variables 
print(name + n1)
 
name = " kamlesh saini "
print(name.upper())# convet in upper case
print(name.lower())#convert in lower case

print(name.swapcase())# convert upper case to lower case and lower vasee to upperr case

print(name.title())#captilized first letter of every word
print(name.capitalize())# captilized firts letter of string
print(name.casefold()) # it is used to perform caseless comparesion -- it convert all the letters in lower case
print(name.strip()) ## it is used to remove sapce from both side ( only white space(lesf right space not centre space))
print(name.lstrip())## it remove only left space
print(name.rstrip())# it is remove right space
print(name.replace("saini","kumar"))# it is used to replace the word from string
print(name.split(" ")) # break the string
print(name.partition(" "))# it is divide the string into three parts
print(name.center(50,"*"))# incrase the string and take main string in centre
print(name.ljust(50,"*"))# it take the main string in left side 
print(name.rjust(50,"*"))# it take right 
print(name.count("a"))# count the letter in the whole string
print(name.endswith("a"))# it give answer in tru false -- check that syring end with that perticular character 
print(name.startswith("a"))# it check that the string is start with rhat perticular character
print(name.rpartition("saini"))# divide the string into three parts from rigth side
#print(name.removeprefix())# if anything remove from front ( aaga sa ) 
#print(name.removeprefix())# if remove anything from behind( peecha sa)
print(name.isalpha())# check alphabat
print(name.isdigit())
print(name.isalpha())
# is sa strt hona vala sb true false ma answer data h -- ya chek krna ka use ma aata h 
print(name.encode("ascii"))

age = 10
# text = " my age is + age"
# formatted string // f- string
text = f"my age is {age}"
print(text)

text = " my name is \" kamlesh\""
print(text)

## indexing and slicing 
# indexing -- access only single character
# slicing -- access multiple chaaracter
# " hello"
# 0 1 2 3 4 5 -- positive
# -5 -4 -3 -2 -1 --- neative
# h e l l o

fruit = "mango"
print(fruit[4]) # indexing  --- it print o
print(fruit[-3]) # negative indexing ---  it print n
print(fruit[0:4]) # slicing --it print mang
print(fruit[0:5]) # print mango
print(fruit[0:-3]) # negative slicing -- print ma
print(fruit[-5: ]) # print mango
print(fruit[:]) # print mango




def addfuntionisinstr(a,b):
 return a+b