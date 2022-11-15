a={"pooja":23,"mayuri":21,"shivani":24,"simmi":20}
b={"pooja":23,"mayuri":21,"shivani":24,"simmi":20,"virpal":22}
c={}
for i in a:
    # print(a)
    print(i)
    print(a[i])
    a.items()
print(a)
a.update(b)
print(b)
