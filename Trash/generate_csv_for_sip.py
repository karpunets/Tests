import random

f = open("data.csv", "w")

count = random.randint(1,9999999)
f.write("SEQUENTIAL\n")
if count%2 == 0:
    count+=1
for i in range(90000):
    phone ="SEP" + "0"*(12-len(str(count))) + str(count)
    if count%2 != 0:
        xrefci = str(12345 + count)
        field1 = "x-nearend"
    else:
        field1 = "x-farend"
    f.write(xrefci+";"+field1+";"+phone+";"+"\n")
    count+=1

f.close()