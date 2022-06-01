import gzip
import csv

blocks_csv = csv.writer(open('../Data/Blocks/Blocks.csv', 'w'))

#print("blockId:ID,hash,time,:LABEL")
header = ['blockId:ID','hash','time',':LABEL']
blocks_csv.writerow(header)

for i in range(10,31): 
    print(i)
    with gzip.open('../Data/Blocks/blockchair_bitcoin_blocks_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[0], fields[1], fields[2], "Block"]
            #print("%s,%s,%s,Block" % (fields[0], fields[1], fields[2]))
            blocks_csv.writerow(row)