import gzip
import csv

miner_ids = []
for i in range(10,21): 
    print(i)
    with gzip.open('../Data/Blocks/blockchair_bitcoin_blocks_202104' + str(i) + '.tsv.gz', "rt") as f:
        f.readline()
        for line in f:
            fields = line.strip().split('\t')
            miner_id = fields[-1]
            if miner_id in miner_ids:
                continue
            miner_ids.append(miner_id)

importcsv = csv.writer(open('../Data/ImportData/Miners.csv', 'w'))
header = ['guessed_miner_id:ID',':LABEL']
importcsv.writerow(header)
for miner_id in miner_ids:
    row = [miner_id, "Guessed_miner"]
    importcsv.writerow(row)