#!/usr/bin/python3
#open() read() close() write()
def count_gc(sequence):
    if len(sequence) == 0:
        return 0.0
    else:
        gc_count = sequence.count("G") + sequence.count("C")
        gc_percent = (gc_count / len(sequence)) * 100
        print(gc_count)
        print(gc_percent)
        return True
records = []
with open("gene.fna", "r") as file:
      for line in file:
        line = line.strip()

        if line.startswith(">"):
            record = {
                    "metadata": line[1:],
                    "data": ""
                    }
           
            records.append(record)
       
        else:
           records[-1]["data"] += line
    
for i in records:
    count_gc(i['data'])
     

