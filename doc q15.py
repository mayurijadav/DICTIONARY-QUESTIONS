# Q15.Write a Python program to remove a key from a dictionary.
dic={"a":1,"b":2,"c":3}
dic.clear()
print(dic)

# 2nd method
dic={"a":1,"b":2,"c":3}
if 'b' in dic:
    del dic['b']
print(dic)



# dic={"a":1,"b":2,"c":3}
# dic2={}
# for i in dic:
#     if dic[i] not in dic2:
#         print(dic2)

# dic={"a":1,"b":2,"c":3}
# dic2={}
# for i in dic:
#     if i!="b":
#         dic2.update(dic)
#     print(dic)


 