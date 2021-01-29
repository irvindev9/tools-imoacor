import random

dtlz = 3
dimension = 3

f = open(f"instances/{dimension}D/DTLZ{dtlz}.dat", "r")
cont = 0
for x in f:
  cont+=1

dmlist = []
dms = 0

while dms < 10:
    n = random.randint(1,cont)

    if n not in dmlist:
        dmlist.append(n)
        dms+=1

# print(dmlist)

f.close()

fout = open("output/DTLZ1.txt", "a")

contifs = 0
for i in range(len(dmlist)):
    filetoread = open(f"instances/{dimension}D/DTLZ{dtlz}.dat", "r")
    cont = 1
    fout.write(f"if(dm_num == {contifs})\n")
    fout.write("{\n")
    for x in filetoread:
        if cont == dmlist[i]:
            values = x.strip().split()
            for inde in range(len(values)):
                fout.write(f"\tdm[{inde}] = {values[inde]};\n")
            fout.write(f"\tdm_line = {dmlist[i]};\n")
        cont+=1
    fout.write("}\n")
    contifs+=1
    filetoread.close()


fout.close()