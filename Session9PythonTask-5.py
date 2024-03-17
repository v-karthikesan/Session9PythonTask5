#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Program for the function filters out elements from the list which are greater than 4
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))


# In[4]:


#Program for the Lambda function to check every element of a List is an Integer or String
data = [10, 'hello', 2, 'world', 37, 'python']
result = all(map(lambda x: isinstance(x, (int, str)), data))
print(result)


# In[5]:


#Program for using Lambda function to creating a fibonacci series from 1 to 50 elements 
from functools import reduce

fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fibonacci_series(50))


# In[6]:


#Program for the function to validate Regular Expressions
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_bangladeshi_mobile_number(number):
    pattern = r'^\+?(88)?01[3-9]\d{8}$'
    return re.match(pattern, number) is not None

def validate_usa_telephone_number(number):
    pattern = r'^\+?1?\s*\(?(\d{3})\)?[-.\s]*(\d{3})[-.\s]*(\d{4})$'
    return re.match(pattern, number) is not None

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(pattern, password) is not None

# Test the functions
print(validate_email("example@example.com"))  # Output: True
print(validate_bangladeshi_mobile_number("+8801712345678"))  # Output: True
print(validate_usa_telephone_number("123-456-7890"))  # Output: True
print(validate_password("Abc123@$!%*?&5678"))  # Output: True


# In[ ]:




