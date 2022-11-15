# 11.Write a Python script to merge two Python dictionaries
dic1={"mayu":"m.sc","raje":"m.ca","vaibhav":"poltecnic"}
dic2={"viraj":"doploma","sharad":"m.pharm"}
d={}
# for i in dic1:
d.update(dic1)
d.update(dic2)
print(d)