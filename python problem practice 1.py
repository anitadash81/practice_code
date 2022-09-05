#!/usr/bin/env python
# coding: utf-8

# ### PYTHON PROBLEM STATEMENT PRACTICE

# Q1.Say "Hello, World!" With Python
# Here is a sample line of code that can be executed in Python: print("Hello, World!") 
# You can just as easily store a string as a variable and then print it to stdout:

# In[ ]:


my_string = "Hello, World!"
    print(my_string)


# Q2.Python If-Else.....
#    Task: Given an integer, n , perform the following conditional actions: 
# i) If n is odd, print Weird If n is even and in the inclusive range of 2 to 5 , 
#    print Not Weird 
# ii) If n is even and in the inclusive range of 6 to 20, 
#     print Weird 
# iii)   If n is even and greater than 20,
#       print Not Weird
# ...Input Format: A single line containing a positive integer,  Constraints: 1<=n<=100

# In[ ]:


if __name__ == '__main__':
   n = int(input().strip())
   
   if n%2!=0:
      print("Weird")

   else:
       if n>=2 and n<=5:
           print("Not Weird")
       elif n>=6 and n<=20:
           print("Weird")
       elif n>20:
           print("Not Weird")
                       


# Q3.Arithmetic Operators....
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where: 1.The first line contains the sum of the two numbers. 2.The second line contains the difference of the two numbers (first - second). 3.The third line contains the product of the two numbers. Example: a=3 b=5 Print the following: 8 ,-2 ,15

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a+b
    d=a-b
    e=a*b
    print("%d\n%d\n%d"%(c,d,e))
                        


# Q4. Python: Division...
# The provided code stub reads two integers, a and b, from STDIN. Add logic to print two lines. 
# i.The first line should contain the result of integer division, a//b . 
# ii.The second line should contain the result of float division, a/b ...
# No rounding or formatting is necessary...
# Example: The result of the integer division 3//5=0. ..
#     The result of the float division is 3/5=0.6. P

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a//b
    d=a/b
    print("%d\n%f"%(c,d))
                        


# Q5.Loops...
# Task: The provided code stub reads an integer, n , from STDIN. 
#     For all non-negative integers i<n, print i^2. 
#     Example: n=3 The list of non-negative integers that are less than n=3 is [0,1,2] .
#         Print the square of each number on a separate line. 0 1 4 ...
#         Input Format: The first and only line contains the integer, n. Constraints: 1<=n

# In[ ]:


if __name__ == '__main__':
   n = int(input())
   for i in range(n):
       print(i*i)

