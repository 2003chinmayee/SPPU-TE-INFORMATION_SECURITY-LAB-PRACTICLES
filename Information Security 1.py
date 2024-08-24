#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Xor(str1, key):
    # store value of first character
    ans = ord(str1[0])
    for i in range(1,len1):
        # Traverse string to find the XOR
        ans = (ans ^ (ord(str1[i])))
    # Return the XOR
    return ans

def And(str1, len1):
    # store value of first character
    ans = ord(str1[0])
    for i in range(1,len1):
        # Traverse string to find the AND
        ans = (ans & (ord(str1[i])))
    # Return the AND
    return ans

def Or(str1, len1):
    # store value of first character
    ans = ord(str1[0])
    for i in range(1,len1):
        # Traverse string to find the OR
        ans = (ans | (ord(str1[i])))
    # Return the OR
    return ans
 
# Driver code
str1 = input("Enter your value: ") 
len1 = len(str1)
print(Xor(str1, 127))
print(And(str1, len1)) 
print(Or(str1, len1))

