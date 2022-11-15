# Q5.Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2:

d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a={k: v for k, v in sorted(d.items(),key=lambda item:item[1])}
b=a.items()
print(b)
    





































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