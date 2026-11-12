#!/usr/bin/python3


#open() read() close() write()
file = open("cds.fna", "r")
content = file.read()
file.close()
print(content)

