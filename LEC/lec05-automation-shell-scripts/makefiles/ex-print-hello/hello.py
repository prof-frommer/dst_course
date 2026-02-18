fileobj = open('name01.dat', 'r')

name = fileobj.readline().strip()

print(f"Hello, {name}!")

fileobj.close()