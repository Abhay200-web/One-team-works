###loops




"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)"""
"""
my_dic={"name":"abhay","age":65,"place":"thrissur"}
for n in my_dic:
    print(n,end="")
    """
"""v={"name":"abhay","age":77}
print(v.items())
for k in v.keys():### keys willcome as the result ###
    print(v[k])"""

"""v={"name":"abhay","age":77}
print(v.values())
for k in v.values():### values print ayiverum###
    print(k)"""

"""v={"name":"abhay","age":77}
for k in v:
    print(k,v[k])"""

"""my_list=[65,56,57,87,78]
print(list(enumerate(my_list,3)))
for c,k in enumerate(my_list,0):
   print(c,k)"""
    

"""range"""
"""print(list(range(3,50,3)))"""# repeats the
""""num=int(input("Enter the number:")) """
"""for j in range(1,11):
    print(f"{j}*{num} = {j*num}")"""
"""
for num in range(1,27):
    if num%2==0:
        print(num)"""

"""
word=["bca","Bca","balu","buddy"]
for w in word:
    if w.lower()[0]=='b':
        print(w)    
"""    

"""words=["abhay","column","Abcd","Wrong"]
for G in words:
    if G.lower()[1]in'b':
        print(G)"""


"""words=["abhay","eli","io","bha","oww","unity"]
for g in words:
    if g.lower()[0]in'aeiou':
        print(g)
"""


"""for num in range(1,11):
    if num==3:
        continue  ## will continue after deleting the number 
    print(num)"""
    
"""for num in range(1,10):
    if num==9:
        break  # will exit the loop at this point 
    print(num)"""


"""for r in range(1,4):
    for j in range(1,r+1):
        print(j, end="")

    print("")"""



"""a=1
while a<=4:
    if a==4:
        num=6  
    else:
        num=a
    col=1
    while col<=a:
        print(num * col, end=" ")
        col+= 1
    print()
    a+=1"""

"""for r in range(1,5):
    for j in range(1,r+1):
        print(end=" * ")
    print(" ")"""
    

""""
for r in range(1,6):
    for ap in range(5-r):
        print(" ",end="")
    for st in range(r):
        print("*",end="")
    print("")"""


"""for r in range(1,5):
    for j in range(1,r+1):
        print(end="*")
    print(" ")"""

"""for r in range(5,0,-1):
    print(" "*int(0-r),"*"*r)"""


"""for r in range(1,6):  # rnage 1 to 5 ie:1 2 3 4 
    for k in range(1,r+1):  # k new variable in range 1 to when r =1, r+1=2 so on 
        print(r*k,end=" ") # prints r * k first r will be 1 and k is 1 so it prints 1 and secondly when the  r is 2 and k is 2 it prints 4 and 2 
    print()
"""


 
for i in range(1, 5 + 1):
    num = i
    diff = 5 - 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num + diff
        diff -= 1
    print()
