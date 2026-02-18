fileobj = open("data01.dat", "r")

line = fileobj.readline()
line = line.strip()
y = [int(i) for i in line.split()]
for n in y:
    print(n * n)

fileobj.close()