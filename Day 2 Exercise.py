#!/usr/bin/env python
# coding: utf-8

# # DAY 2 EXERCISE

# ## Question 1

# In[8]:


def get_expected_cost(beds,baths):
    
# asumme the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000

    value = 80000
    
# add cost bedroom 30000

    value += beds * 30000
    
# add cost bathroom 10000

    value += baths * 10000
    
    return value


# ## Question 2

# In[9]:


# Calculate the expected cost of each option using the get_expected_cost() function

option_1 = get_expected_cost(2, 3)
option_2 = get_expected_cost(3, 2)
option_3 = get_expected_cost(3, 3)
option_4 = get_expected_cost(3, 4)

# Printing the expected cost of each option

print(option_1)
print(option_2)
print(option_3)
print(option_4)


# ## Question 3

# In[15]:



def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = math.ceil(total_sqft / sqft_per_gallon)
    cost = gallons_needed * cost_per_gallon
    return cost


# ## Question 4

# In[16]:


# paint usage
sqft_walls = 432
sqft_ceiling = 144
sqft_per_gallon = 400
cost_per_gallon = 15
cost = get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print(cost)

