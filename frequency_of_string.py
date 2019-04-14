'''
Find the frequency of characters in string
'''
n = input("enter a string")
length = len(n)
for i in range(length):
   print(n[i],"is",n.count(n[i]),"times")
    
