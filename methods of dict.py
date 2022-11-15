#         METHODS

# DELETING METHODS FROM DOCTIONARY

# # 1.POP ()
# # it will delet specific key value pair
# a={1:"d",2:"s",3:"f"}
# a.pop(2)
# print(a)


# # 2.popitem ()
# #  also it will delet last element
# a={1:"d",2:"s",3:"f"}
# a.popitem()
# print(a)

# # 3. clear()
# # it will delet all elements from dictionary and gives empty dictionary {}.
# a={1:"d",2:"s",3:"f"}
# a.clear()
# print(a)


# # del keyword
# # it will delet the specific key value pair..
# a={1:"d",2:"s",3:"f"}
# del a[2]
# print(a)
# #  also it will delet the all dectionary and gives the element
# del a
# print(a)


# ACCESSING DICTIONARY METHODS

# # 4.   get()
# # it will access the specipic key and give the value .
# a={1:"d",2:"s",3:"f"}
# x= a.get(2)
# print(x)

# # we can access the key direct using the dictionary name and giving key in squrebracket[] it gives the value.
# a={1:"d",2:"s",3:"f"}
# x=a[3]
# print(x)

# # 5.    values()
# # it will gives the values
# a={1:"d",2:"s",3:"f"}      
# x=a.values()                 
# print(x)                     

# # also it add the newkey value pair in dictionry and gives the value
# a={1:"d",2:"s",3:"f"}
# x=a.values() 
# a[4]="m"
# print(x)
# print(a)


# # 6.   keys()
# # it will gives the keys 
# a={1:"d",2:"s",3:"f"}
# x=a.keys()
# print(x)

# # also we can add newkey value pair in dictionary.
# a={1:"d",2:"s",3:"f"}
# x=a.keys()
# a[4]="g"
# print(x)
# print(a)

# # also it will update the dictionary
# a={1:"d",2:"s",3:"f"}
# x=a.keys()
# a[2]="g"
# print(x)
# print(a)


# #    7. items()
# # it will give the ky value both .f
# a={1:"d",2:"s",3:"f"}
# x=a.items()
# print(x)

# # also it will update the dictionary 
# a={1:"d",2:"s",3:"f"}
# x=a.items()
# a[2]="m"
# print(x)



# #   UPDATING METHOD 

# #   8.  update()
# # it will update the element
# a={"x":2,"y":4,"z":6}
# a.update({"k":9})
# print(a)

# # this is 2nd method to update the dictionary
# a={"x":2,"y":4,"z":6}
# a["o"]=8
# print(a)

# a={"x":2,"y":4,"z":6}
# a["x"]=8
# print(a)



# #  9.copy
# # it will use to copy the element.
# a={"x":2,"y":4,"z":6}
# b=a.copy()
# print(b)
# print(id(a))
# print(id(b))


# #   10.formkeys
# # it is use to form the key,value pair. 
# a=[2,3,4]
# b=5
# c=dict.fromkeys(a,b)
# print(c)

# a=[2,3,4]d
# b=[3,4,5,6]
# c=dict.fromkeys(b,a)
# print(c)
# print(dict.fromkeys(a,b))

# a="mayu"
# b=4
# print(dict.fromkeys(a,b))


# # 11. setdefault
# it will give setdefult value
# a={1:"a",2:"b",3:"c"}
# b=a.setdefault(1)
# print(b)

# a={"x":2,"y":4,"z":6}
# a["x"]=8
# print(a)

# a={"x":2,"y":4,"z":6}
# a.setdefault("f",8)
# print(a)

 



















#           EXAMPALS
 # a={"a":"mayu","b":"jadhav","c":23}
# a.pop("a")
# print(a)


# a={"a":"mayu","b":"jadhav","c":23}
# a.popitem()
# print(a)

# a={"a":"mayu","b":"jadhav","c":23}
# a.clear()
# print(a)

# a={"a":"mayu","b":"jadhav","c":23}
# del a["b"]
# print(a)


# a={"a":"mayu","b":"jadhav","c":23}
# del a
# print(a)

# a={"a":"mayu","b":"jadhav","c":23}
# x= a.get("a")
# print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.keys()
# print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.values()
# print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.items()
# print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# a.update({"d":"raje"})
# print(a)

# a={"a":"mayu","b":"jadhav","c":23}
# a["d"]="raje"
# print(a)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.copy()
# print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.setdefault("b","kadam")
# # print(x)

# a={"a":"mayu","b":"jadhav","c":23}
# x=a.setdefault("e",90)
# print(x)
# print(a)
 

# a=(1,2,3,4)
# b=(12,34,34,45)
# x=dict.fromkeys(a,b)
# print(x)


# a=(1,2,3,4)
# b=(12,34,34,45)
# x=dict.fromkeys(b,a)
# print(x)