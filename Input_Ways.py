'''Input() by default it specified as strings,it can take any type of value(eg: int,float,str)'''
# a=input() # 3
# b=input() # 4
# print(a+b) # 34

'''to add two numbers'''
# a,b=[int(x) for x in input().split()] # a value(2) space b value(6)
# print(a+b) # 8

'''to add multiple numbers'''
# a=[int(x) for x in input().split()]
# print(sum(a)) # 2 3 4 5 6 7 8 
                # 35

'''to multiply numbers'''

# a=[int(x) for x in input().split()]
# print(prod(a)) # it won't work, first wright import math 

# import math
# a=[int(x) for x in input().split()]
# print(math.prod(a))  # 2 2 2
#                      # 8


# a=input()  # 421
# print("My Rollnumber is",a) # My Rollnumber is 421
# print("My Rollnumber is",a,sep="-")  # My Rollnumber is-421
# print("My Rollnumber is",int(a))  # My Rollnumber is 421
# print("My Rollnumber is",float(a)) # My Rollnumber is 421.0
# print("My Rollnumber is"+' '+str(a)) # My Rollnumber is 421
# print("My Rollnumber is"+' '+a) # My Rollnumber is 421

'''Int(Input())-it allows only int values'''
# a=int(input('Enter the Rollnumber')) # 419
# print("My Rollnumber is",a) # My Rollnumber is 419
# print("My Rollnumber is",a,sep="-")  # My Rollnumber is-419
# print("My Rollnumber is",int(a))  # My Rollnumber is 419
# print("My Rollnumber is",float(a)) # My Rollnumber is 419.0
# print("My Rollnumber is"+' '+str(a)) # My Rollnumber is 419

# a=int(input('Enter the Rollnumber')) # 407.0 (It does n't allow float and string values)
# print("My Rollnumber is",a)
# print("My Rollnumber is",a,sep="-")
# print("My Rollnumber is",int(a))  
# print("My Rollnumber is",float(a)) 
# print("My Rollnumber is"+' '+str(a)) 


'''Float(Input())-it allows only float values'''
# a=int(input('Enter the Rollnumber'))  #418
# print("My Rollnumber is",a) # My Rollnumber is 418
# print("My Rollnumber is",a,sep="-")  # My Rollnumber is-418
# print("My Rollnumber is",int(a))  # My Rollnumber is 418
# print("My Rollnumber is",float(a)) # My Rollnumber is 418.0
# print("My Rollnumber is"+' '+str(a)) # My Rollnumber is 418


# Bird=input('Enter the bird name: ')  # parrot
# Count=int(input('Enter the count: ')) # 2
# Price=float(input('Enter the price: ')) # 500

# print(Bird,Count,Price) # parrot 2 500.0
# print(Price,Bird,Count) # 500.0 parrot 2
# print(Bird,Count) # parrot 2

# Bird=input('Enter the bird name: ')   # parrot
# Count=int(input('Enter the count: '))   # 2
# Price=float(input('Enter the price: ')) # 500

# print('My favourite bird is',Bird,'Number of birds are',Count,'Price of birds',Price) # My favourite bird is parrot Number of birds are 2 Price of birds 500.0

# print('My favourite bird is',Bird,'Number of birds are',Count,\
# 'Price of birds',Price) # My favourite bird is parrot Number of birds are 2 Price of birds 500.0

# print("Bird name is %s and Number of birds are %d.\
# Price of birds %f"(Bird,Count,Price)) 

# print("My favourite bird is {} Number of birds are {}. \
# Price of birds {}".format(Bird,Count,Price)) # My favourite bird is parrot Number of birds are 2. Price of birds 500.0

# print("My favourite bird is {1} Number of birds are {2}. \
# # Price of birds {0}".format(Price,Bird,Count)) # My favourite bird is parrot Number of birds are 2. Price of birds 500.0

# print(f"My favourite bird is {Bird} Number of birds are {Count}. \
# # Price of birds {Price}") # My favourite bird is parrot Number of birds are 2. Price of birds 500.0

