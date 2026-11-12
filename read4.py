#!/usr/bin/python3

#open() read() close() write()
records = []

with open("cds.fna", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):
            record = {
                    "metadata" : line[1:],
                    "data": ""
                }
            records.append(record)

        else:
            records[-1]["data"] += line

print(records)
