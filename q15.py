fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        # print(fruit)
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print(len(fruit))
print(fruit)
