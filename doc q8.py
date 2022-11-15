# Q8.Write a Python program to check whether a given key already exists in a dictionary.
new={1:10,2:20,3:30,4:40,5:50}
for i in new:
    print(i)
    key=(input("enter key"))
    if key in new[i]:
        print(key,"already exist in dictionary")
    else:
        new.update(key
















# for i in new:
#     b=(input("enter key"))
#     c=new.keys()
#     for b in :
#         print("yes this key in dictionary")
#         new.update(c)
#     print(c)
#     # else:
#     #     print("no this not in dictionary")
#     # new.update(b)
#     # print(new)