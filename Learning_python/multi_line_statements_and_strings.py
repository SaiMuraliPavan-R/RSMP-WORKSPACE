#multi line statements and strings 

a = [1,2,3,4]
print(a)

#multi line 
a= [1,2,
    3,4]
print(a)

a = [1,2, #items
     3,4 #item2 
]
print(a)

#tuples
a = (1,
     2,
     3)
print(a)

a = (1, #item1
     2, #item2
     3
     )
print(a)
#dict
a  = {
    '1': 1,#value for 1
    '2':2 #value for 2
    }
print(a)
#sets
a = {
    1,
    2,
    3
}
print(a)

#functions
def my_func(age,#first ARg pass numebr
            name, #second arg pass string 
            hegight
            ):
    print(age,name,hegight)

my_func(
    1, #age
    'sai', #name
    5.5 #height
)

#Eplict line conversion 

a = 10
b = 20 
c = 30 


if a > 5 and b > 10 and c > 20: 
    print('yes')
else: 
    print('no')

#can be written in mutliple lines usign contintion cahrecter \

if a > 5\
   and b >10 \
   and c > 20 : 
     print('yes')
else:
    print('No')

a = """
this is a string 
  called in 3 quotes """

print(a) #all spaces, tabs, new lines everythign is preserved nothing is reset to normal line 

a = a.upper()
print(a)

#same multipel string as a docstring in class and function 

def my_doc_strN():
    ''' this function print something '''
    a = '''multipe lines 
            example of the doc string '''
    print(a)
    return a

print(my_doc_strN()) #as decleared in the intial fucntion same way it will get returned. 
