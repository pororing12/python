'''
tt = ((1, 2, 3),
      (4, 5, 6),
      (7, 8, 9))
for i in range(0, 3) :
    for k in range(0, 3) :
        print("%3d" % tt[i][k], end = "")
    print("")
'''

myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)
