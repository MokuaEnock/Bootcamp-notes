#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


# how to convert a float to an integer with the int function.

y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))


# In[4]:



print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))


# # Question 2

# In[5]:


print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))


# # Question 3

# In[6]:


def get_expected_cost(beds, baths, has_basement):
    value = 80000
    # Additional cost of bedroom (defining beds)
    
    value += beds * 30000
    
    # Additional cost of bathroom (defining baths)
    
    value += baths * 10000
    
    # Additional cost of basement (defining has_basement)
    
    value += has_basement * 40000
    
    return value


# In[8]:


cost1 = get_expected_cost(1, 1, False)
cost2 = get_expected_cost(2, 1, True)

print(cost1)
print(cost2)


# In[ ]:




