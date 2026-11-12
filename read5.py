 #!/usr/bin/python3

 #open() read() close() write()
 def read(filename):
     records = []

     with open("filename", "r") as file:
         for line in file:
             line = line.strip()

             if line.startswith(">"):
                 record = {
                         "metadata": line[1:],
                         "data": ""
                records.append(record)
            else:
            records[-1]["data"] += line
return records
def read(gene.fna):
print(records)
