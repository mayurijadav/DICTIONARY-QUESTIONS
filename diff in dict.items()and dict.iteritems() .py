# 	dict.items() 	                                          dict.iteritems()
#1.The dict.items() method returns a view object.	   The dict.iteritems() function returns an iterator of the dictionary’s list. 
#2.Its syntax is-:# dictionary.items()            .   The dict.iteritems() is a generator that yields 2-tuples
#3.It does not take any parameters.	                    It does not take any parameters.
#4.Its return value is a list of tuple pairs.	        Its return value is the iterator on list of key value pairs.
#If the input list is empty then it returns an empty list.	It is the feature of python2 version but gets removed in python3 version.


# Python3 code to demonstrate
# d.items()
 
# d ={
#   "fantasy": "harrypotter",
#   "romance": "me before you",
#   "fiction": "divergent"
#   }
 
# # saves as a copy
# print(d.items())

# OUTPUT:dict_items([(‘fantasy’, ‘harrypotter’), (‘fiction’, ‘divergent’), (‘romance’, ‘me before you’)])

# If we try to run the dict.iteritems() in Python v3.x, we will ecounter with an error



# Python3 code to demonstrate
# d.iteritems()
 
 
# d ={
#   "fantasy": "harrypotter",
#   "romance": "me before you",
#   "fiction": "divergent"
#   }
 
# print("d.items() in (v3.6.2) = ")
# for i in d.items():
 
#     # prints the items
#     print(i)
 
# print("\nd.iteritems() in (v3.6.2)=")
 
# for i in d.iteritems():
 
#     # prints the items
#     print(i)

# Output:

# d.items() in (v3.6.2) = 
# ('fiction', 'divergent')
# ('fantasy', 'harrypotter')
# ('romance', 'me before you')

# d.iteritems() in (v3.6.2)=

# Traceback (most recent call last):
#   File "/home/33cecec06331126ebf113f154753a9a0.py", line 19, in 
#     for i in d.iteritems():
# AttributeError: 'dict' object has no attribute 'iteritems'











