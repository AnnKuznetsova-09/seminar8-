#!/usr/bin/python3


#open() read() close() write()

records = []  #создаем пустой список 

with open("gene.fna", "r") as file:
    for line in file:  #файл читается по строчкам
        line = line.strip() #убираются лишние пробелы

        if line.startswith(">"):
            record = {
                    "metadata": line[1:],
                    "data": ""
            }

            records.append(record)
       
        else:
            records[-1]["data"] += line

print(records)
