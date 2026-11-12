#!/usr/bin/python3
#open() read() close() write()

file = open("gene.fna", "r")
print(type(file))
content = file.read()
print(content[:10])


