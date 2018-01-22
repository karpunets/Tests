import random

f1 = open("data1.csv", "w")
f2 = open("data2.csv", "w")

count = random.randint(1,9999999)
f1.write("SEQUENTIAL\n")
f2.write("SEQUENTIAL\n")

for i in range(50000):
    phone = "SEP" + "0" * (12 - len(str(count))) + str(count)
    xrefci = str(11111 + count)
    f1.write(xrefci+";"+"x-nearend;"+phone+";"+"\n")
    phone = "SEP" + "0" * (12 - len(str(count+1))) + str(count+1)
    f2.write(xrefci + ";" + "x-farend;" + phone + ";" + "\n")
    count+=1


# f = open("data.csv", "w")
#
# count = random.randint(1,9999999)
# f.write("SEQUENTIAL\n")
# if count%2 == 0:
#     count+=1
# for i in range(90000):
#     phone ="SEP" + "0"*(12-len(str(count))) + str(count)
#     if count%2 != 0:
#         xrefci = str(12345 + count)
#         field1 = "x-nearend"
#     else:
#         field1 = "x-farend"
#     f.write(xrefci+";"+field1+";"+phone+";"+"\n")
#     count+=1
#
# f.close()


