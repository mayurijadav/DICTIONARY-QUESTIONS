# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196
# 15: 225}
num=int(input("enter num"))
dic={}
for i in range(1,num+1):
    dic.update({i:i*i})
    # print(i,i*i)r
print(dic)