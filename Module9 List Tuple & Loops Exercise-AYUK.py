#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1
# Ask a user for 5 names and place each one in to a list called <i>names</i>. Then, print <i>names</i>.

# In[2]:


names = ["Dora","Paul","Dean","Joe","Mike"]
#x = input("Enter a name: ")
#names.append(x)
#print(names)
print(names)


# ### Exercise 2
# Print out a randomly selected name in the names list from exercise 1.

# In[3]:


import random
random_index = random.randint(0, len(names)-1)
print(names[random_index])


# ### Exercise 3: 
# Fix bugs in the next cell.  It is trying to create a list for even numbers between two numbers provided by a user.
# 

# In[11]:


no1 = int(input("Enter a starting number: "))
no2 = int(input("Enter an ending number: "))

numbers = []
evens = []

for i in range(no1, no2) :
    numbers.append(i) 
    if (i%2 == 0):    # even number
        evens.append(i)
    
print(numbers)    
print(evens)


# ### Exercise 4
# Finish writing a program to generate 10 random numbers between 1 and 100 and save it to a list.
# Finally, print out the original numbers followed by the smallest, largest, and average number.

# In[19]:


import random as rand

numbers = []
total = 0

for i in range(1, 100) :
    numb = rand.randint(1, 100)
    total += len(numbers)
    numbers.append(numb)
    if total == 10:
        print(numbers)

    
# some code needed here to find the smallest, largest, and average number





"""
print(f"Org Numbers are {org_numbs}")
print(f"Sorted numbers are {numbers}")
print(f"Largest number is {largest}")
print(f"Smallest number is {smallest}")
print(f"Average is {avg}")
"""


# ### Exercise 5
# 
# Write a function called <b>draw_triangle()</b> to draw a right triangle where the base of the triangle is the number passed in as an arguement. Call <b>draw_triangle()</b> to show it works.
# 
# e.g. <b>draw_triangle(7)</b> draws as below:
# 
#     *
#     **
#     ***
#     ****
#     *****
#     ******
#     *******
# 

# In[18]:


# write code for draw_triangle() function

x=int(input("Enter row number=\n"))
for i in range(x):
    for j in range(i+1):
        print("*",end='')
    print("")


# In[ ]:


base = int(input("Enter a number: "))

draw_triangle(base)

