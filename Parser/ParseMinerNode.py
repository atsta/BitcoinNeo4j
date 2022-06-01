import gzip
import csv

blocks_csv = csv.writer(open('../Data/Miners.csv', 'w'))
header = ['guessed_miner_id:ID',':LABEL']
blocks_csv.writerow(header)
for i in range(10,31): 
    print(i)
    with gzip.open('../Data/Blocks/blockchair_bitcoin_blocks_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            row = [fields[-1], "Guessed_miner"]
            blocks_csv.writerow(row)